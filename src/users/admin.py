from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth import forms as auth_forms
from users.models import User

class MyUserChangeForm(auth_forms.UserChangeForm):
    class Meta(auth_forms.UserChangeForm.Meta):
        model = User

class CustomUserAdmin(UserAdmin):
    form = MyUserChangeForm

admin.site.register(User, CustomUserAdmin)
