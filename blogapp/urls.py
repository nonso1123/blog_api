from django.urls import path
from .views import register_user, create_blog, blog_list, update_blog, delete_blog, update_profile, get_blog, get_username, get_userInfo

urlpatterns = [
    path('register_user/', register_user, name='register_user'),
    path('create_blog/', create_blog, name= 'create_blog'),
    path('blog_list', blog_list, name='blog_list'),
    path('blogs/<slug:slug>/', get_blog, name='get_blog'),
    path('update_blog/<int:pk>/', update_blog, name='update_blog'),
    path('delete_blog/<int:pk>/', delete_blog, name='delete_blog'),
    path('update_profile/', update_profile, name='update_profile'),
    path('get_username', get_username, name='get_username'),
    path('get_userInfo/<str:username>', get_userInfo, name='get_userInfo'),
]
