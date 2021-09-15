from django.contrib.auth.mixins import *
from django.urls import reverse_lazy
from django.views.generic import *

from app.forms.create import *
from app.models import Course, Announcement
from app.views.create import CreationView
from app.views.delete import DeletionView
from app.views.edit import EditionView, UserEditView

required_permissions = (
    'app.add_course', 'app.change_course', 'app.view_course', 'app.delete_course',
    'app.add_lecture', 'app.change_lecture', 'app.view_lecture', 'app.delete_lecture',
    'app.add_test', 'app.change_test', 'app.view_test', 'app.delete_test',
    'app.add_testquestion', 'app.change_testquestion', 'app.view_testquestion', 'app.delete_testquestion',
    'app.add_answer', 'app.change_answer', 'app.view_answer', 'app.delete_answer',
    'app.add_announcement', 'app.change_announcement', 'app.view_announcement', 'app.delete_announcement',
)


class DashboardIndexView(LoginRequiredMixin, PermissionRequiredMixin, TemplateView):
    template_name = 'app/dashboard/base/index.html'
    permission_required = required_permissions


# Accounts
class DashboardAccountDetailView(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    pk_url_kwarg = 'id'
    model = User
    template_name = 'app/dashboard/views/detail/user.html'
    permission_required = required_permissions


class DashboardAccountEditView(UserEditView, PermissionRequiredMixin):
    template_name = 'app/dashboard/views/edit/user.html'
    success_url = reverse_lazy('app:dashboard')
    permission_required = required_permissions


class DashboardUserList(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    model = User
    template_name = 'app/dashboard/views/list/user.html'
    permission_required = required_permissions


# Courses
class DashboardCourseCreationView(PermissionRequiredMixin, CreationView):
    model = Course
    form_class = CourseCreationForm
    template_name = 'app/dashboard/views/create/course.html'
    success_url = reverse_lazy('app:dashboard_course_list')
    permission_required = required_permissions


class DashboardCourseList(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    model = Course
    template_name = 'app/dashboard/views/list/course.html'
    permission_required = required_permissions


class DashboardCourseEditView(PermissionRequiredMixin, LoginRequiredMixin, UpdateView):
    pk_url_kwarg = 'id'
    model = Course
    form_class = CourseCreationForm
    success_url = reverse_lazy('app:dashboard_course_list')
    template_name = 'app/dashboard/views/edit/course.html'
    permission_required = required_permissions


class DashboardCourseDeletionView(PermissionRequiredMixin, LoginRequiredMixin, DeleteView):
    pk_url_kwarg = 'id'
    model = Course
    template_name = 'app/dashboard/views/delete/course.html'
    success_url = reverse_lazy('app:dashboard_course_list')
    permission_required = required_permissions


# Lectures
class DashboardLectureCreationView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = Lecture
    fields = ('title', 'about', 'file')
    permission_required = required_permissions
    success_url = reverse_lazy('app:dashboard_course_list')

    def form_valid(self, form):
        lecture = form.save(commit=False)
        lecture.course = Course.objects.all().get(id=self.kwargs['id'])
        self.success_url = reverse_lazy('app:edit_course', args=[self.kwargs['id']])
        lecture.save()
        return super(DashboardLectureCreationView, self).form_valid(form)


class DashboardLectureEditView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    pk_url_kwarg = 'id'
    model = Lecture
    fields = ('title', 'about', 'file')
    template_name = 'app/dashboard/views/edit/lecture.html'
    permission_required = required_permissions


class DashboardLectureDeletionView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    pk_url_kwarg = 'id'
    model = Lecture
    template_name = 'app/dashboard/views/delete/lecture.html'
    success_url = reverse_lazy('app:dashboard_course_list')
    permission_required = required_permissions


# Quizzes
class DashboardQuizCreationView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = Quiz
    fields = ('title', 'duration')
    permission_required = required_permissions
    success_url = reverse_lazy('app:dashboard_course_list')

    def form_valid(self, form):
        quiz = form.save(commit=False)
        quiz.course = Course.objects.all().get(id=self.kwargs['id'])
        quiz.save()
        self.success_url = reverse_lazy('app:edit_course', args=[self.kwargs['id']])
        return super(DashboardQuizCreationView, self).form_valid(form)


class DashboardQuizEditView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    pk_url_kwarg = 'id'
    model = Quiz
    fields = ('title', 'duration')
    template_name = 'app/dashboard/views/edit/quiz.html'
    permission_required = required_permissions
    success_url = reverse_lazy('app:dashboard_course_list')


class DashboardQuizDeletionView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    pk_url_kwarg = 'id'
    model = Quiz
    template_name = 'app/dashboard/views/delete/quiz.html'
    success_url = reverse_lazy('app:dashboard_course_list')
    permission_required = required_permissions


# Quiz Questions
class DashboardQuizQuestionCreationView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = QuizQuestion
    fields = ('type', 'content')
    template_name = 'app/dashboard/views/create/quiz_question.html'
    success_url = reverse_lazy('app:dashboard_course_list')
    permission_required = required_permissions

    def form_valid(self, form):
        question = form.save(commit=False)
        question.quiz = Quiz.objects.all().get(id=self.kwargs['id'])
        self.success_url = reverse_lazy('app:edit_quiz', args=[self.kwargs['id']])
        question.save()
        return super(DashboardQuizQuestionCreationView, self).form_valid(form)


class DashboardQuizQuestionEditView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    pk_url_kwarg = 'id'
    fields = ('type', 'content')
    model = QuizQuestion
    template_name = 'app/dashboard/views/edit/quiz_question.html'
    success_url = reverse_lazy('app:dashboard_course_list')
    permission_required = required_permissions


class DashboardQuizQuestionDeletionView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    pk_url_kwarg = 'id'
    model = QuizQuestion
    template_name = 'app/dashboard/views/delete/quiz_question.html'
    success_url = reverse_lazy('app:dashboard_course_list')
    permission_required = required_permissions


# Quiz Answers
class DashboardQuizAnswerCreationView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = QuizAnswer
    fields = ('right', 'content')
    template_name = 'app/dashboard/views/create/quiz_answer.html'
    success_url = reverse_lazy('app:dashboard_course_list')
    permission_required = required_permissions

    def form_valid(self, form):
        answer = form.save(commit=False)
        answer.question = QuizQuestion.objects.all().get(id=self.kwargs['id'])
        answer.save()
        self.success_url = reverse_lazy('app:edit_quiz_question', args=[self.kwargs['id']])
        return super(DashboardQuizAnswerCreationView, self).form_valid(form)


class DashboardQuizAnswerEditView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    pk_url_kwarg = 'id'
    model = QuizAnswer
    fields = ('right', 'content')
    template_name = 'app/dashboard/views/edit/quiz_answer.html'
    success_url = reverse_lazy('app:dashboard_course_list')
    permission_required = required_permissions


class DashboardQuizAnswerDeletionView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    pk_url_kwarg = 'id'
    model = QuizAnswer
    template_name = 'app/dashboard/views/delete/quiz_answer.html'
    success_url = reverse_lazy('app:dashboard_course_list')
    permission_required = required_permissions


# Announcements
class DashboardAnnouncementCreationView(PermissionRequiredMixin, CreationView):
    model = Announcement
    fields = ('content', 'image')
    template_name = 'app/dashboard/views/create/announcement.html'
    success_url = reverse_lazy('app:dashboard_announcement_list')
    permission_required = required_permissions


class DashboardAnnouncementList(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    model = Announcement
    template_name = 'app/dashboard/views/list/announcement.html'
    permission_required = required_permissions


class DashboardAnnouncementEditView(PermissionRequiredMixin, EditionView):
    model = Announcement
    fields = ('content',)
    success_url = reverse_lazy('app:announcements')
    template_name = 'app/dashboard/views/edit/announcement.html'
    permission_required = required_permissions


class DashboardAnnouncementDeleteView(PermissionRequiredMixin, DeletionView):
    model = Announcement
    template_name = 'app/dashboard/views/delete/announcement.html'
    success_url = reverse_lazy('app:dashboard_announcement_list')
    permission_required = required_permissions
