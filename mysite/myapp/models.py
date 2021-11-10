from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
from phonenumber_field.modelfields import PhoneNumberField


class FacultyDetails(models.Model):
    facultyId = models.ForeignKey(User,on_delete=models.CASCADE)
    facultyName = models.CharField(max_length=10,null=False)
    facultyPhone = PhoneNumberField(null=False, blank=False, unique=False, default='+91')
    facultyGender = models.CharField(max_length=20,null=True)
    facultyDOB = models.DateTimeField(default=datetime.now,null=True)
    # user_pass = models.CharField(max_length=10, blank=True)
    # user_unique = models.CharField(max_length=100,null=True)
    facultyDesc = models.TextField(blank=False,null=True)
    facultyCollege = models.CharField(max_length=100,null=False)
    collegeState = models.CharField(max_length=50,null=False)
    experience = models.CharField(max_length=2,null=True)
    facultyPic = models.ImageField(upload_to='facultyPic/', null=True, blank=True)
    user_date = models.DateTimeField(default=datetime.now,null=True)

    def __str__(self):
        return str(self.facultyId) if self.facultyId else ''


class StudentDetails(models.Model):
    studentId = models.ForeignKey(User,on_delete=models.CASCADE)
    studentName = models.CharField(max_length=10,null=False)
    studentPhone = PhoneNumberField(null=False, blank=False, unique=False, default='+91')
    studentGender = models.CharField(max_length=20,null=False)
    studentDOB = models.DateTimeField(default=datetime.now,null=True)
    # user_pass = models.CharField(max_length=10, blank=True)
    # user_unique = models.CharField(max_length=100,null=True)
    studentDesc = models.TextField(blank=False,null=True)
    studentCollege = models.CharField(max_length=100,null=False)
    collegeState = models.CharField(max_length=50,null=False)
    yearOfStudy = models.CharField(max_length=2,null=True)
    studentPic = models.ImageField(upload_to='StudentPic/', null=True, blank=True)
    user_date = models.DateTimeField(default=datetime.now,null=True)

    def __str__(self):
        return str(self.studentId) if self.studentId else ''
