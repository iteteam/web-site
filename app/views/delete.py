import re
from django.contrib.auth.mixins import *
from django.shortcuts import get_object_or_404, redirect
from django.views.generic import *
from django.urls import reverse_lazy

from app.models import *


class DeletionView(LoginRequiredMixin, DeleteView):
    pk_url_kwarg = 'id'

    def get_queryset(self):
        qs = super(DeletionView, self).get_queryset()
        return qs.filter(user=self.request.user)


class PostDeleteView(DeletionView):
    model = Post
    template_name = 'app/views/delete/post.html'
    success_url = reverse_lazy('app:blog')


class CommentDeleteView(DeletionView):
    model = Comment
    template_name = 'app/views/delete/comment.html'
    success_url = reverse_lazy('app:blog')


class ReplyDeleteView(DeletionView):
    model = Reply
    template_name = 'app/views/delete/reply.html'
    success_url = reverse_lazy('app:blog')


class QuestionDeleteView(DeletionView):
    model = Question
    template_name = 'app/views/delete/question.html'
    success_url = reverse_lazy('app:forums')


class QuestionAnswerDeleteView(DeletionView):
    model = Answer
    context_object_name = 'answer'
    template_name = 'app/views/delete/question_answer.html'
    success_url = reverse_lazy('app:forums')
