from rest_framework import serializers

from posts.models import Post, Comment


class PostSerializer(serializers.HyperlinkedModelSerializer):
    # provides user to see 'children' comments
    comments = serializers.HyperlinkedRelatedField(
        many=True, view_name='comment-detail', read_only=True
    )

    class Meta:
        model = Post
        fields = '__all__'
        read_only_fields = ['creation_date']


class CommentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'
        read_only_fields = ['creation_date']
