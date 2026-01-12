from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    ADMIN = 'admin'
    MENTOR = 'mentor'
    STUDENT = 'student'
    
    ROLE_CHOICES = [
        (ADMIN, 'Admin'),
        (MENTOR, 'Mentor'),
        (STUDENT, 'Student'),
    ]

    phone = models.CharField(max_length=15, null=True, blank=True)
    bio = models.TextField(blank=True)
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default=STUDENT)

    @property
    def is_mentor(self):
        return self.role == self.MENTOR

    @property
    def is_student(self):
        return self.role == self.STUDENT

    @property
    def is_admin(self):
        return self.role == self.ADMIN
