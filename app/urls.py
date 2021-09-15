from django.contrib.auth import views as auth_views
from django.urls import path
from app.views.views import *

app_name = 'app'

app = [
    path('', IndexView.as_view(), name='index'),
    path('catalog/', CourseListView.as_view(), name='catalog'),
    path('catalog/course/<int:id>/details', CourseDetailView.as_view(), name='course_detail'),
    path('catalog/course/<int:id>/details/enroll', MemberCreationView.as_view(), name='enroll'),

    path('blog/', PostListView.as_view(), name='blog'),
    path('blog/post/add', PostCreationView.as_view(), name='create_post'),
    path('blog/post/<int:id>/details', PostDetailView.as_view(), name='post_detail'),
    path('blog/post/<int:id>/edit', PostEditView.as_view(), name='edit_post'),
    path('blog/post/<int:id>/delete', PostDeleteView.as_view(), name='delete_post'),
    path('blog/post/<int:id>/details/comment', CommentCreationView.as_view(), name='create_comment'),
    path('blog/post/comment/<int:id>/edit', CommentEditView.as_view(), name='edit_comment'),
    path('blog/post/comment/<int:id>/details', CommentDetailView.as_view(), name='comment_detail'),
    path('blog/post/delete/<int:id>/comment', CommentDeleteView.as_view(), name='delete_comment'),
    path('blog/post/comment/<int:id>/reply', ReplyCreationView.as_view(), name='create_reply'),
    path('blog/post/comment/<int:id>/reply/edit', ReplyEditView.as_view(), name='edit_reply'),
    path('blog/post/comment/<int:id>/reply/delete', ReplyDeleteView.as_view(), name='delete_reply'),

    path('forums/', QuestionListView.as_view(), name='forums'),
    path('forums/question/add', QuestionCreationView.as_view(), name='create_question'),
    path('forums/question/<int:id>/details', QuestionDetailView.as_view(), name='generic_question_detail'),
    path('forums/question/<int:id>/edit', QuestionEditView.as_view(), name='edit_generic_question'),
    path('forums/question/<int:id>/delete', QuestionDeleteView.as_view(), name='delete_generic_question'),
    path('forums/question/<int:id>/details/answer', QuestionAnswerCreationView.as_view(), name='create_answer'),
    path('forums/question/edit/<int:id>/answer', QuestionAnswerEditView.as_view(), name='edit_answer'),
    path('forums/question/delete/<int:id>/answer', QuestionAnswerDeleteView.as_view(), name='delete_answer'),

    path('announcements/', AnnouncementListView.as_view(), name='announcements'),

    path('accounts/signup', UserCreationView.as_view(), name='signup'),
    path('accounts/<int:id>/details', UserDetailView.as_view(), name='user_detail'),
    path('accounts/user/<int:id>/edit', UserEditView.as_view(), name='edit_user'),

    path('images/<str:typ>/<int:pk>', FileView.as_view(), name='return_file'),
]

dashboard = [
    path(
        'dashboard/',
        DashboardIndexView.as_view(),
        name='dashboard'
    ),
    # Accounts
    path(
        'dashboard/list/account',
        DashboardUserList.as_view(),
        name='dashboard_user_list'
    ),
    path('dashboard/account/<int:id>/details',
         DashboardAccountDetailView.as_view(),
         name='dashboard_account'
         ),
    path(
        'dashboard/account/<int:id>/edit',
        DashboardAccountEditView.as_view(),
        name='dashboard_account_edit'
    ),
    # Courses
    path(
        'dashboard/add/course',
        DashboardCourseCreationView.as_view(),
        name='create_course'
    ),
    path(
        'dashboard/list/course',
        DashboardCourseList.as_view(),
        name='dashboard_course_list'
    ),
    path(
        'dashboard/edit/<int:id>/course',
        DashboardCourseEditView.as_view(),
        name='edit_course'
    ),
    path(
        'dashboard/delete/<int:id>/course',
        DashboardCourseDeletionView.as_view(),
        name='delete_course'
    ),
    # Lectures
    path(
        'dashboard/edit/<int:id>/course/add/lecture',
        DashboardLectureCreationView.as_view(),
        name='create_lecture'
    ),
    path(
        'dashboard/edit/course/edit/<int:id>/lecture',
        DashboardLectureEditView.as_view(),
        name='edit_lecture'
    ),
    path(
        'dashboard/edit/course/delete/<int:id>/lecture',
        DashboardLectureDeletionView.as_view(),
        name='delete_lecture'
    ),
    # Quizzes
    path(
        'dashboard/edit/<int:id>/course/add/quiz',
        DashboardQuizCreationView.as_view(),
        name='create_quiz'
    ),
    path(
        'dashboard/edit/course/edit/<int:id>/quiz',
        DashboardQuizEditView.as_view(),
        name='edit_quiz'
    ),
    path(
        'dashboard/edit/course/delete/<int:id>/quiz',
        DashboardQuizDeletionView.as_view(),
        name='delete_quiz'
    ),
    # Quiz Questions
    path(
        'dashboard/edit/course/edit/<int:id>/quiz/add/question',
        DashboardQuizQuestionCreationView.as_view(),
        name='create_quiz_question'
    ),
    path(
        'dashboard/edit/course/edit/quiz/edit/<int:id>/question',
        DashboardQuizQuestionEditView.as_view(),
        name='edit_quiz_question'
    ),
    path(
        'dashboard/edit/course/edit/quiz/delete/<int:id>/question',
        DashboardQuizQuestionDeletionView.as_view(),
        name='delete_quiz_question'
    ),
    # Quiz Answers
    path(
        'dashboard/edit/course/edit/quiz/edit/<int:id>/question/add/answer',
        DashboardQuizAnswerCreationView.as_view(),
        name='create_quiz_answer'
    ),
    path(
        'dashboard/edit/course/edit/quiz/edit/question/edit/<int:id>/answer',
        DashboardQuizAnswerEditView.as_view(),
        name='edit_quiz_answer'
    ),
    path(
        'dashboard/edit/course/edit/quiz/edit/question/delete/<int:id>/answer',
        DashboardQuizAnswerDeletionView.as_view(),
        name='delete_quiz_answer'
    ),
    # Announcements
    path(
        'dashboard/add/announcement',
        DashboardAnnouncementCreationView.as_view(),
        name='create_announcement'
    ),
    path(
        'dashboard/list/announcement',
        DashboardAnnouncementList.as_view(),
        name='dashboard_announcement_list'
    ),
    path(
        'dashboard/edit/<int:id>/announcement',
        DashboardAnnouncementEditView.as_view(),
        name='edit_announcement'
    ),
    path(
        'dashboard/delete/<int:id>/announcement',
        DashboardAnnouncementDeleteView.as_view(),
        name='delete_announcement'
    ),
]

override = [
    path('accounts/password/change/', auth_views.PasswordChangeView.as_view(), name='change_password'),
    path('accounts/password/change/done/', auth_views.PasswordChangeDoneView.as_view(), name='change_done'),
    path('accounts/password/reset/', auth_views.PasswordResetView.as_view(), name='reset_password'),
    path('accounts/password/reset/done/', auth_views.PasswordResetDoneView.as_view(), name='reset_done'),
    path(
        'accounts/password/reset/confirm/<uidb64>/<token>/',
        auth_views.PasswordResetConfirmView.as_view(),
        name='reset_confirm'
    ),
    path('accounts/password/reset/complete/', auth_views.PasswordResetCompleteView.as_view(), name='reset_complete'),
]

urlpatterns = app + dashboard + override
