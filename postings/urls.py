from django.contrib.auth.decorators import login_required

from postings.models import Post
from . import views
from django.conf.urls import url
from . import views

app_name = 'postings'

urlpatterns = [
    url(r'^$',views.PostFeedView.as_view(),name='feed'),
    url(r'posts/new/',views.CreatePostView.as_view(),name='create_post'),
    url(r'posts/<int:post_id>/',views.PostDetailView.as_view(),name='post_detail'),
    url(r'profile/<str:username>/',views.UserDetailView.as_view(),name='user_detail'),
    url(r'login/',views.LoginView.as_view(), name='login'),
    url(r'logout/',views.LogoutView.as_view(),name='logout'),
    url(r'signup/',views.SignupView.as_view(),name='signup'),
    url(r'me/profile/',views.UpdateProfileView.as_view(),name='update'),
]
