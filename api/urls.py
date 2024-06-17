from django.urls import path
from .views import post_list, post_detail, PostListCreate, PostDetail, post_create, comment_create

urlpatterns = [
    path('posts/', PostListCreate.as_view(), name='post-list-create'),
    path('posts/<int:pk>/', PostDetail.as_view(), name='post-detail'),

    # Для рендеринга шаблонов
    path('post-list/', post_list, name='post_list'),
    path('post-detail/<int:pk>/', post_detail, name='post_detail'),
    path('post-create/', post_create, name='post_create'),
    path('comment-create/<int:pk>/', comment_create, name='comment_create'),
]
