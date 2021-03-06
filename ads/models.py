from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.contrib import auth
# Create your models here.
class BaseUserManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, username, email, password, **extra_fields):
        """
        Create and save a user with the given username, email, and password.
        """
        if not username:
            raise ValueError('The given username must be set')
        email = self.normalize_email(email)
        username = self.model.normalize_username(username)
        user = self.model(username=username, email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, username, email=None, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(username, email, password, **extra_fields)

    def create_superuser(self, username, email=None, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(username, email, password, **extra_fields)

    def with_perm(self, perm, is_active=True, include_superusers=True, backend=None, obj=None):
        if backend is None:
            backends = auth._get_backends(return_tuples=True)
            if len(backends) == 1:
                backend, _ = backends[0]
            else:
                raise ValueError(
                    'You have multiple authentication backends configured and '
                    'therefore must provide the `backend` argument.'
                )
        elif not isinstance(backend, str):
            raise TypeError(
                'backend must be a dotted import path string (got %r).'
                % backend
            )
        else:
            backend = auth.load_backend(backend)
        if hasattr(backend, 'with_perm'):
            return backend.with_perm(
                perm,
                is_active=is_active,
                include_superusers=include_superusers,
                obj=obj,
            )
        return self.none()


class Userinfo(AbstractUser):
    mobno=models.CharField(max_length=12,null=True)
    dob=models.DateField(null=True)
    place = models.CharField(max_length=100,blank=True)
    prof_pic=models.ImageField(upload_to="images",blank=True)
    objects = BaseUserManager()
class Property(models.Model):
    uname=models.CharField(max_length=20)
    title=models.CharField(max_length=200)
    address=models.CharField(max_length=200)
    city=models.CharField(max_length=100)
    state=models.CharField(max_length=100)
    mobno=models.IntegerField()
    whtspno=models.IntegerField(blank=True)
    description=models.TextField(blank=True)
    price=models.IntegerField()
    bedrooms=models.IntegerField(default=0)
    bathrooms = models.IntegerField(default=0)
    sqft=models.IntegerField(blank=True)
    list_date=models.DateTimeField(auto_now=True)
    photo_main=models.ImageField(upload_to='images',blank=True)
    photo1 = models.ImageField(upload_to='images',blank=True)
    photo2 = models.ImageField(upload_to='images', blank=True)
    choices = [
            ("published","published"),
            ("blocked","blocked"),

        ]
    status=models.CharField(choices=choices,default="published",max_length=20)

    def __str__(self):
        return self.title


# class notification(models.Model):
#     date=models.DateField(auto_now=True)
#     time=models.TimeField(auto_now=True)
#     title=models.CharField(max_length=50)
#     description=models.CharField(max_length=200)

class Propertys(models.Model):
    uname=models.CharField(max_length=20)
    title=models.CharField(max_length=200)
    address=models.CharField(max_length=200)
    city=models.CharField(max_length=100)
    state=models.CharField(max_length=100)
    mobno=models.CharField(max_length=12)
    whtspno=models.CharField(max_length=12)
    description=models.TextField(blank=True)
    price=models.IntegerField()
    bedrooms=models.IntegerField(default=0)
    bathrooms = models.IntegerField(default=0)
    sqft=models.IntegerField(blank=True)
    list_date=models.DateTimeField(auto_now=True)
    photo_main=models.ImageField(upload_to='images',blank=True)
    photo1 = models.ImageField(upload_to='images',blank=True)
    photo2 = models.ImageField(upload_to='images', blank=True)
    choices = [
            ("published","published"),
            ("blocked","blocked"),

        ]
    status=models.CharField(choices=choices,default="published",max_length=20)

    def __str__(self):
        return self.title

