from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('add', views.add, name='add'),
    path('blog/<slug:slug>', views.blog, name='blog'),
    path('update/<slug:slug>', views.update, name='update'),
    path('delete/<slug:slug>', views.delete, name='delete'),
    
    path('author/<str:username>', views.authors, name='author'),
    path('profile/<str:username>', views.updateProfile, name='update_profile'),
    path('author-lists', views.authorList, name='author_lists'),
    
    path('signup', views.signup, name='signup'),
    path('login', views.user_login, name='login'),
    path('logout', views.user_logout, name='logout'),
]
