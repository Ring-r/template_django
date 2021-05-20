import django.contrib.auth.admin
from django.contrib import admin

from .forms import UserChangeForm
from .forms import UserCreationForm
from .models import User


class UserAdmin(django.contrib.auth.admin.UserAdmin):
    add_form = UserCreationForm
    form = UserChangeForm
    model = User
    list_display = ['email', 'username', ]


admin.site.register(User, UserAdmin)
