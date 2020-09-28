from django.urls import path, include
# from rest_framework.routers import DefaultRouter
from posts import views


# create a router and register our viewsets with it

# router = DefaultRouter()
# router.register(r"posts", views.PostViewSet)
# router.register(r"comments", views.CommentViewSet)

# app_name = "posts"
# urlpatterns = [
#     path("", include(router.urls)),
# ]

post_list = views.PostViewSet.as_view({
    'get': 'list',
    'post': 'create'
})

post_detail = views.PostViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy',
})

post_upvote = views.PostViewSet.as_view({
    'get': 'post_upvote'
})

comment_list = views.CommentViewSet.as_view({
    'get': 'list',
    'post': 'create'
})

comment_detail = views.CommentViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})


urlpatterns = [
    # get root links
    path('', views.api_root),

    # api endpoint for posts
    path('posts/', post_list, name='post-list'),
    path('posts/<int:pk>/', post_detail, name='post-detail'),

    # api endpoint to upvote post
    path('posts/<int:pk>/upvote', post_upvote, name='post_upvote'),

    # api endpoints for comments
    path('comments/', comment_list, name='comment-list'),
    path('comments/<int:pk>/', comment_detail, name='comment-detail')
]
