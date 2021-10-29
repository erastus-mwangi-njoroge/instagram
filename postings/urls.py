from django.contrib.auth.decorators import login_required

from postings.models import Post
from . import views
from django.conf.urls import url
from . import views
from django.contrib.auth import views as auth_views
from django.urls import path

app_name = 'postings'

urlpatterns = [
    path(r'',views.PostFeedView.as_view(),name='feed'),
    path(r'posts/new/',views.CreatePostView.as_view(),name='create_post'),
    path(r'posts/<int:pk>/',views.PostDetailView.as_view(),name='post_detail'),
    path(r'profile/<str:username>/',views.UserDetailView.as_view(),name='user_detail'),
    path(r'login/',auth_views.LoginView.as_view(), name='login'),
    path(r'logout/',views.LogoutView.as_view(),name='logout'),
    path(r'signup/',views.SignupView.as_view(),name='signup'),
    path(r'me/profile/',views.UpdateProfileView.as_view(),name='update'),
]
