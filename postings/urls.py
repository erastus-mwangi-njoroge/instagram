from django.contrib.auth.decorators import login_required

from postings.models import Post
from . import views
from django.conf.urls import url
from . import views

app_name = 'postings'

urlpatterns = [
    url(r'',views.PostFeedView.as_view(queryset = Post.objects.all()),name='feed'),
    url(r'posts/new/',views.CreatePostView.as_view(),name='create_post'),
    url(r'posts/<int:post_id>/',views.PostDetailView.as_view(),name='detail'),
]
