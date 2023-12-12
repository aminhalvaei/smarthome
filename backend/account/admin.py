from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserCreationForm, CustomeUserChangeForm
from .models import User

# Register your models here.


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomeUserChangeForm
    model = User
    list_display = [
        "username",
        "email",
        "birthdate",
        "is_staff",
        "is_active",
    ]
    fieldsets = UserAdmin.fieldsets + ((None, {"fields": ("birthdate",)}),)
    add_fieldsets = UserAdmin.add_fieldsets + (
        (
            None,
            {
                "fields": (
                    "email",
                    "birthdate",
                )
            },
        ),
    )


admin.site.register(User, CustomUserAdmin)
