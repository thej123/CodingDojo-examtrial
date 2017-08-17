from __future__ import unicode_literals

from django.db import models

# Create your models here.

class UserManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        if len(postData['first_name']) < 2:
            errors['first_name'] = 'First name should be more than 1 charater'
        if len(postData['last_name']) < 2:
            errors['last_name'] = 'Last name should be more than 1 charater'
        if len(postData['email']) < 2:
            errors['email'] = 'Email should be more than 1 charater'
        return errors
    
        

class User(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = UserManager()