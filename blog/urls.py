from django.urls import path

from . import views


app_name = 'blog'
urlpatterns = [
    path('', views.index, name='index'),
    path('posts/', views.posts, name='posts'),
    path('posts/<int:post_id>', views.post, name='post'),
    path('new_post/', views.new_post, name='new_post'),
    path('edit_post/<int:post_id>', views.edit_post, name='edit_post'),
    path('del_post/<int:post_id>', views.del_post, name='del_post'),
]
