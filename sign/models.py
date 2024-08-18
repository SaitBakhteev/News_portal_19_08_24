# То, что отмечено решеткой, после них начались проблемы. Откат назад проблему оставил
from allauth.account.forms import SignupForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User, Group
from django import forms
#
class BaseRegisterForm(UserCreationForm):
    email = forms.EmailField(label = "Email")
    first_name = forms.CharField(label = "First name")
    last_name = forms.CharField(label = "Last name")

    class Meta:
        model = User
        fields = ("username",
                  "first_name",
                  "last_name",
                  "email",
                  "password1",
                  "password2", )

class BasicSignupForm(SignupForm):
    def save(self, request):
        user=super(BasicSignupForm,self).save(request)
        basic_group=Group.objects.get(name="common")
        basic_group.user_set.add(user)
        return user




# НИЖЕ ПРЕДСТАВЛЕН ВАРИАНТ, КОТОРЫЙ ПОРЕКОМЕНДОВАЛ ПОЛЬЗОВАТЕЛЬ stds58@gmail.com В ПАЧКЕ (тоже не помогло)

# from django.contrib.auth.base_user import BaseUserManager, AbstractBaseUser
# from django.contrib.auth.hashers import make_password
# from django.contrib.auth.models import PermissionsMixin
# from django.db import models
#
#
# class UserManager(BaseUserManager):
#     def create_user(self, name, email, password=None, **kwargs):
#         if not email:
#             raise ValueError('User must have an email address')
#
#         user = self.model(
#             name=name,
#             email=self.normalize_email(email),
#             password=make_password(password),
#             **kwargs
#         )
#
#         user.save(using=self._db)
#         return user
#
#     def create_superuser(self, name, email, password=None, **kwargs):
#         user = self.create_user(
#             name=name,
#             email=self.normalize_email(email),
#             password=password,
#             **kwargs
#         )
#         user.is_superuser = True
#         user.is_staff = True
#         user.save(using=self._db)
#         return user
#
#
# class User(AbstractBaseUser, PermissionsMixin):
#     # id = models.AutoField(primary_key=True, blank=False, null=False, unique=True, verbose_name='user id')
#     name = models.CharField(max_length=255, verbose_name='name of user')
#     email = models.EmailField(unique=True, max_length=255, verbose_name='email of user')
#     date_creation = models.DateTimeField(auto_now_add=True, verbose_name='date of sign up')
#     date_password_change = models.DateTimeField(auto_now=True, verbose_name='date of password change')
#     password = models.CharField(max_length=255, verbose_name='password')
#     is_staff = models.BooleanField(default=False)
#     is_superuser = models.BooleanField(default=False)
#     random_field = models.BooleanField(default=False)
#
#     objects = UserManager()
#     USERNAME_FIELD = 'email'
#     REQUIRED_FIELDS = ['name']
#
#     def __str__(self):
#         return f'{self.email}'
#
#
# # Сох
# #
# #
# #
# #
# #
# #
