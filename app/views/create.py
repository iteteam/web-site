from django.contrib.auth.mixins import *
from django.urls import reverse_lazy
from django.views.generic import *
from app.forms.forms import *


class CreationView(LoginRequiredMixin, CreateView):
    pk_url_kwarg = 'id'

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.user = self.request.user
        obj.save()
        return super(CreationView, self).form_valid(form)


class UserCreationView(CreateView):
    model = User
    form_class = SignUpForm
    template_name = 'app/views/create/user.html'
    success_url = reverse_lazy('app:index')


class PostCreationView(CreationView):
    model = Post
    fields = ('content',)
    template_name = 'app/views/create/post.html'
    success_url = reverse_lazy('app:blog')


class CommentCreationView(LoginRequiredMixin, CreateView):
    model = Comment
    fields = ('content',)
    success_url = reverse_lazy('app:blog')

    def form_valid(self, form):
        comment = form.save(commit=False)
        comment.user = self.request.user
        comment.post = Post.objects.all().get(pk=self.kwargs['id'])
        comment.save()
        self.success_url = reverse_lazy('app:post_detail', args=[self.kwargs['id']])
        return super(CommentCreationView, self).form_valid(form)


class QuestionCreationView(CreationView):
    model = Question
    fields = ('content',)
    template_name = 'app/views/create/question.html'
    success_url = reverse_lazy('app:forums')


class QuestionAnswerCreationView(LoginRequiredMixin, CreateView):
    model = Answer
    fields = ('content',)
    success_url = reverse_lazy('app:forums')

    def form_valid(self, form):
        answer = form.save(commit=False)
        answer.user = self.request.user
        answer.question = Question.objects.all().get(pk=self.kwargs['id'])
        answer.save()
        self.success_url = reverse_lazy('app:generic_question_detail', args=[self.kwargs['id']])
        return super(QuestionAnswerCreationView, self).form_valid(form)


class ReplyCreationView(LoginRequiredMixin, CreateView):
    model = Reply
    fields = ('content',)
    success_url = reverse_lazy('app:blog')

    def form_valid(self, form):
        reply = form.save(commit=False)
        reply.user = self.request.user
        reply.comment = Comment.objects.all().get(pk=self.kwargs['id'])
        reply.save()
        self.success_url = reverse_lazy('app:comment_detail', args=[self.kwargs['id']])
        return super(ReplyCreationView, self).form_valid(form)


class MemberCreationView(LoginRequiredMixin, CreateView):
    model = Member
    fields = ()
    success_url = reverse_lazy('app:catalog')

    def form_valid(self, form):
        member = form.save(commit=False)
        member.user = self.request.user
        member.course = Course.objects.all().get(pk=self.kwargs['id'])
        member.save()
        self.success_url = reverse_lazy('app:course_detail', args=[self.kwargs['id']])
        return super(MemberCreationView, self).form_valid(form)
