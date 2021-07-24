from django.urls import path
from tags.views import tags_list_view, tag_detail_view, TagCreateView, TagUpdateView, TagDeleteView


urlpatterns = [
    path('', tags_list_view, name='tags_list_url'),
    path('<int:id>/', tag_detail_view, name='tag_detail_url'),
    path('create/', TagCreateView.as_view(), name='tag_create_url'),
    path('<int:id>/update/', TagUpdateView.as_view(), name='tag_update_url'),
    path('<int:id>/delete/', TagDeleteView.as_view(), name='tag_delete_url'),
]
