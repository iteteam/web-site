from django.contrib.auth.mixins import *
from django.http import Http404
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import *

from app.forms.forms import *


class EditionView(LoginRequiredMixin, UpdateView):
    pk_url_kwarg = 'id'

    def get_queryset(self):
        """ Limit a User to only modifying their own data. """
        qs = super(EditionView, self).get_queryset()
        return qs.filter(user=self.request.user)


class UserEditView(LoginRequiredMixin, UpdateView):
    pk_url_kwarg = 'id'
    model = User
    form_class = UserEditForm
    template_name = 'app/views/edit/user.html'
    success_url = reverse_lazy('app:index')

    def get_queryset(self):
        """ Limit a User to only modifying their own data. """
        qs = super(UserEditView, self).get_queryset()
        return qs.filter(id=self.request.user.id)


class PostEditView(EditionView):
    model = Post
    fields = ('content',)
    success_url = reverse_lazy('app:blog')
    template_name = 'app/views/edit/post.html'


class CommentEditView(EditionView):
    model = Comment
    fields = ('content', )
    success_url = reverse_lazy('app:blog')
    template_name = 'app/views/edit/comment.html'


class ReplyEditView(EditionView):
    model = Reply
    fields = ('content', )
    success_url = reverse_lazy('app:blog')
    template_name = 'app/views/edit/reply.html'


class QuestionEditView(EditionView):
    model = Question
    context_object_name = 'question'
    fields = ('content',)
    success_url = reverse_lazy('app:forums')
    template_name = 'app/views/edit/question.html'


class QuestionAnswerEditView(EditionView):
    model = Answer
    context_object_name = 'answer'
    fields = ('content', )
    success_url = reverse_lazy('app:forums')
    template_name = 'app/views/edit/question_answer.html'
