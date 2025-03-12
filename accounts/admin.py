from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .forms import CustomUserChangeForm, CustomUserCreationForm
from .models import CustomUser

# Register your models here.

@admin.register(CustomUser)
class CustomUseradmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser

    fieldsets = UserAdmin.fieldsets = (
        (None, {'fields': ('username', 'password', ), }),
        ('Personal Info', {'fields': ('first_name', 'last_name', 'email', ), }),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions', ), }),
        ('Important Dates', {'fields': ('last_login', 'date_joined', ), }),
    )

    add_fieldsets =  UserAdmin.add_fieldsets = (
        (None, {"classes": ("wide", ), 'fields': ('username', 'password1', 'password2', )}),
    )
    list_display = ('username', 'email', 'is_staff')
