from django.contrib.auth.mixins import *
from django.views.generic import *
from app.models import *


class CourseDetailView(LoginRequiredMixin, DetailView):
    model = Course
    pk_url_kwarg = 'id'
    template_name = 'app/views/detail/course.html'


class UserDetailView(LoginRequiredMixin, DetailView):
    model = User
    pk_url_kwarg = 'id'
    template_name = 'app/views/detail/user.html'


class PostDetailView(LoginRequiredMixin, DetailView):
    model = Post
    pk_url_kwarg = 'id'
    template_name = 'app/views/detail/post.html'


class CommentDetailView(LoginRequiredMixin, DetailView):
    model = Comment
    pk_url_kwarg = 'id'
    template_name = 'app/views/detail/comment.html'


class QuestionDetailView(LoginRequiredMixin, DetailView):
    model = Question
    pk_url_kwarg = 'id'
    context_object_name = 'question'
    template_name = 'app/views/detail/question.html'
