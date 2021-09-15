from django.contrib.auth.mixins import *
from django.views.generic import *
from app.models import *


class CourseListView(LoginRequiredMixin, ListView):
    model = Course
    template_name = 'app/views/list/catalog.html'


class PostListView(LoginRequiredMixin, ListView):
    model = Post
    ordering = ['-created_at', ]
    template_name = 'app/views/list/blog.html'


class QuestionListView(LoginRequiredMixin, ListView):
    model = Question
    ordering = ['-created_at', ]
    template_name = 'app/views/list/forums.html'


class AnnouncementListView(LoginRequiredMixin, ListView):
    model = Announcement
    ordering = ['-created_at']
    template_name = 'app/views/list/announcements.html'
