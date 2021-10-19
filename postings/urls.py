from django.contrib.auth.decorators import login_required
from . import views
from django.conf.urls import url


urlpatterns = [
    url(r'',views.PostFeedView.as_view(),name='feed'),
    url(r'posts/new/',views.CreatePostView.as_view(),name='create_post'),
    url(r'posts/<int:post_id>/',views.PostDetailView.as_view(),name='detail'),
]
