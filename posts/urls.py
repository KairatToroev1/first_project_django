from django.urls import path
from posts.views import (
    posts_list_view, 
    post_detail_view, 
    PostCreateView, 
    PostUpdateView,
    PostDeleteView
)


urlpatterns = [
    path('', posts_list_view, name='posts_list_url'),
    path('<int:id>/', post_detail_view, name='post_detail_url'),
    path('create/', PostCreateView.as_view(), name='post_create_url'),
    path('<int:id>/update/', PostUpdateView.as_view(), name='post_update_url'),
    path('<int:id>/delete/', PostDeleteView.as_view(), name='post_delete_url'),
]
