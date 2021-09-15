from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    about = models.CharField(max_length=150, blank=True, default='Hey there, welcome to my profile.')
    image = models.ImageField(upload_to='images/profiles', blank=True)
    theme = models.CharField(
        max_length=10,
        default='default',
        choices=[
            ('default', 'Default'),
            ('light', 'Light'),
            ('dark', 'Dark'),
            ('auto', 'Auto'),
            ('sunrise', 'Sun Rise'),
            ('sunset', 'Sun Set'),
            ('green', 'Green Plant'),
            ('red', 'Red Rose')
        ],
    )
    courses = models.ManyToManyField('Course', through='Member')
    comments = models.ManyToManyField('Post', through='Comment', related_name='user_comments')

    def __str__(self):
        return self.username


class Announcement(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    image = models.ImageField(upload_to='images/announcements', blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return 'Announcement by ' + self.user.get_full_name()


# Course relationship
class Course(models.Model):
    title = models.CharField(max_length=60)
    about = models.CharField(max_length=256)
    description = models.TextField()
    image = models.ImageField(upload_to='images/courses')
    users = models.ManyToManyField(User, through='Member')
    rating = models.IntegerField(default=0)

    def __str__(self):
        return self.title


class Lecture(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    title = models.CharField(max_length=60)
    about = models.CharField(max_length=256, blank=True)
    file = models.FileField(upload_to='files/lectures')

    def __str__(self):
        lec = self.course.title + ' lecture ' + str(self.pk)
        return lec


class Member(models.Model):
    role = models.CharField(max_length=30, choices=[('instructor', 'Instructor'), ('student', 'Student')])
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)


# Test relationship
class Quiz(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    # The value entered to this field must be like: 3 days 04:05:06
    duration = models.DurationField()
    title = models.CharField(max_length=60)

    def __str__(self):
        return self.title


class QuizQuestion(models.Model):
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    content = models.TextField()
    type = models.CharField(
        max_length=30,
        choices=[
            ('checkbox', 'Check Box'),
            ('radio', 'Radio Button'),
            ('text', 'Text Field'),
        ]
    )

    def __str__(self):
        return self.quiz.title + ' question ' + self.type


class QuizAnswer(models.Model):
    question = models.ForeignKey(QuizQuestion, on_delete=models.CASCADE)
    content = models.TextField(blank=True)
    right = models.BooleanField('Right answer')


class Question(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField('Publication date', auto_now_add=True)
    updated_at = models.DateTimeField('Update date', auto_now=True)


class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField('Answer Content')
    created_at = models.DateTimeField('Publication date', auto_now_add=True)
    updated_at = models.DateTimeField('Update date', auto_now=True)


# Post Relation ship
class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='post_list')
    content = models.TextField('Content')
    created_at = models.DateTimeField('Publication date', auto_now_add=True)
    updated_at = models.DateTimeField('Update date', auto_now=True)
    comments = models.ManyToManyField(User, through='Comment', related_name='commented_posts')


class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='owner')
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    content = models.TextField('Content')
    created_at = models.DateTimeField('Publication date', auto_now_add=True)
    updated_at = models.DateTimeField('Update date', auto_now=True)


class Reply(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE)
    content = models.TextField('Content')
    created_at = models.DateTimeField('Publication date', auto_now_add=True)
    updated_at = models.DateTimeField('Update date', auto_now=True)
