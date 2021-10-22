from django.contrib.auth import logout
from django.contrib.auth import views
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import get_object_or_404, redirect, render
from django.views.generic import DetailView, FormView, UpdateView, ListView, DetailView, CreateView
from django.contrib.auth.models import User
from .forms import SignupForm,PostForm
from .models import Post,Profile
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator


# Create your views here.

class SignupView(FormView):
    """Signup View."""
    template_name = 'users/register.html'
    form_class = SignupForm
    success_url = reverse_lazy('postings:login')

    def form_valid(self, form):
        """If the form is valid save the user"""
        form.save()
        return super().form_valid(form)


class LoginView(views.LoginView):
    """Login view"""
    template_name = 'users/login.html'
    redirect_authenticated_user = True

class LogoutView(LoginRequiredMixin, views.LogoutView):
    """Logout View."""

class UpdateProfileView(LoginRequiredMixin, UpdateView):
    """Update a user's profile view"""
    template_name = 'users/update_profile.html'
    model = Profile
    fields = ['website', 'biography', 'phone_number', 'picture']
    # Return success url
    def get_object(self):
        """Return user's profile"""
        return self.request.user.profile
    def get_success_url(self):
        """Return to user's profile."""
        username = self.object.user.username
        return reverse('postings:user_detail', kwargs={'username_slug': username})


class UserDetailView(LoginRequiredMixin, DetailView):
    """User detail view."""
    template_name = 'users/update.html'
    slug_field = 'username'
    slug_url_kwarg = 'username_slug'
    queryset = User.objects.all()
    context_object_name = 'user'

    def get_context_data(self, **kwargs):
        """Add user's posts to context"""
        context = super().get_context_data(**kwargs)
        user = self.get_object()
        context['posts'] = Post.objects.filter(profile__user=user).order_by('-created')
        return context

class CreatePostView(LoginRequiredMixin, CreateView):
    
    """Create New Post View"""
    template_name = 'posts/new_post.html'
    form_class = PostForm
    success_url = reverse_lazy('postings:feed')
    context_object_name = 'form'

    def get_context_data(self, **kwargs):
        """Add User and profile to context."""
        context = super().get_context_data(**kwargs)
        context['profile'] = self.request.user.profile
        return context


class PostFeedView(LoginRequiredMixin, ListView):
    """Return all published posts."""
    template_name = 'postings/all_posts.html'
    model = Post
    ordering = ('-created',)
    paginate_by = 4
    context_object_name = 'posts'



class PostDetailView(LoginRequiredMixin, DetailView):
    """Detail view posts"""
    template_name = 'postings/post_details.html'
    slug_field = 'id'
    slug_url_kwarg = 'post_id'
    queryset = Post.objects.all()
    context_object_name = 'post'
