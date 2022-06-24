from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.base_user import BaseUserManager
from django.utils.crypto import get_random_string


class MyUserManager(BaseUserManager):
    use_in_migrations = True

    def create_user(self, login, password, **extra_fields):
        if not login: raise ValueError('email is required')
        email = self.normalize_email(extra_fields.get('email'))
        user = self.model(email=email, login=login, **extra_fields)
        user.set_password(password)
        # user.create_activation_code()
        user.save(using=self._db)
        return user

    def create_superuser(self, login, password, **extra_fields):
        if not login: raise ValueError('email is required')
        email = self.normalize_email(extra_fields.get('email'))
        user = self.model(email=email, login=login, **extra_fields)
        user.set_password(password)
        user.is_superuser = True
        user.is_staff = True
        # user.is_active = True
        user.save(using=self._db)
        return user


class User(AbstractUser):
    # username = None
    email = models.EmailField(unique=True, blank=True)
    login = models.CharField(max_length=35, unique=True)
    slug = models.SlugField(max_length=35, unique=True)

    first_name = models.CharField(max_length=150, blank=True)
    last_name = models.CharField(max_length=250, blank=True)
    image = models.ImageField(default='../media/default/default_author.png', upload_to='users', null=True)
    is_active = models.BooleanField(default=True)

    # activation_code = models.CharField(max_length=20, blank=True)

    USERNAME_FIELD = 'login'
    REQUIRED_FIELDS = tuple()

    def save(self, *args, **kwarks):
        self.slug = self.login.lower().replace(" ", '-')
        return super().save(*args, **kwarks)

    def __str__(self):
        return self.login

    objects = MyUserManager()

    # def create_activation_code(self):
    #     code = get_random_string(18)
    #     self.activation_code = code
    #     self.save()

