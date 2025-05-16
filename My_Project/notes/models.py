from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin

class UserManager(BaseUserManager):
    def create_user(self, email, user_name, password=None):
        if not email:
            raise ValueError('Users must have an email address')
        if not user_name:
            raise ValueError('Users must have a user name')

        email = self.normalize_email(email)
        user = self.model(email=email, user_name=user_name)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, user_name, password):
        user = self.create_user(email=email, user_name=user_name, password=password)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser, PermissionsMixin):
    user_name = models.CharField(max_length=150, unique=True)
    email = models.CharField(max_length=100, unique=True)
    password = models.CharField(max_length=100)  
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)      
    is_superuser = models.BooleanField(default=False) 
    created_at = models.DateField(default='2025-05-16')   
    last_update = models.DateField(auto_now=True)      
    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['user_name']

    def __str__(self):
        return self.email


class Note(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    note_title = models.CharField(max_length=255)
    note_content = models.TextField()
    created_at = models.DateField(default='2025-05-16')  
    last_update = models.DateField(auto_now=True)      

    def __str__(self):
        return f"{self.note_title} ({self.user.user_name})"
