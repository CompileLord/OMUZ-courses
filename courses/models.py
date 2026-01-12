from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Category(models.Model):
    FRONTEND = 'frontend'
    BACKEND = 'backend'
    COURSE_TYPES = [
        (FRONTEND, 'Frontend'),
        (BACKEND, 'Backend'),
    ]
    title = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    course_type = models.CharField(max_length=10, choices=COURSE_TYPES)
    
    def __str__(self):
        return self.title

class Course(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='courses')
    mentor = models.ForeignKey(User, on_delete=models.CASCADE, related_name='mentored_courses', limit_choices_to={'role': 'mentor'})
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

class Topic(models.Model):
    title = models.CharField(max_length=100)
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='topics')
    order = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.title

class Video(models.Model):
    title = models.CharField(max_length=200)
    file = models.FileField(upload_to='videos/')
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE, related_name='videos')
    duration = models.DurationField(null=True, blank=True)

    def __str__(self):
        return self.title

class Subscription(models.Model):
    student = models.ForeignKey(User, on_delete=models.CASCADE, related_name='subscriptions')
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='subscribers')
    subscribed_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('student', 'course')

    def __str__(self):
        return f"{self.student.username} -> {self.course.title}"