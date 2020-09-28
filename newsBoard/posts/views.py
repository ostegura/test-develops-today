# from django.shortcuts import render
# from django.http import Http404, HttpResponse

from posts.models import Post, Comment
from posts.serializers import PostSerializer, CommentSerializer

from rest_framework.response import Response
from rest_framework.decorators import action, api_view
from rest_framework import viewsets
from rest_framework.reverse import reverse
from rest_framework import permissions
# Create your views here.


class PostViewSet(viewsets.ModelViewSet):
    # This viewset automatically provides CRUD actions.

    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (permissions.AllowAny,)

    @action(detail=True, name='Upvote')
    def post_upvote(self, request, pk=None):
        """Upvotes selected post."""
        post = Post.objects.get(pk=pk)
        post.amount_of_upvotes += 1
        post.save()
        serializer = self.get_serializer(post, many=False)

        return Response(serializer.data)


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = (permissions.AllowAny,)


@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'posts': reverse('post-list', request=request, format=format),
        'comments': reverse('comment-list', request=request, format=format)
    })
