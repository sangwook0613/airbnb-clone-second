from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User


@admin.register(User) # admin.site.register(User, CustomUserAdmin) 이 코드와 같은 역할을 수행하는 decorater
class CustomUserAdmin(UserAdmin):
    
    """ Custom User Admin """

    fieldsets = UserAdmin.fieldsets + (
        (
            'Custom Profile',
            {
                'fields': (
                    'avatar',
                    'gender',
                    'bio',
                    'birthdate',
                    'language',
                    'currency',
                    'superhost',
                )
            },
        ),
    )
