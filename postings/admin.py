
  
from django.contrib import admin

# Register your models here.
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib import admin
from django.contrib.auth.models import User
from .models import Post, Profile
#admin.site.register(User, UserAdmin)



@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    """Profile Admin"""
    list_display = ('pk', 'user', 'phone_number', 'website', 'picture')
    list_display_links = ('pk', 'user')
    list_editable = ('phone_number', 'website', 'picture')
    search_fields = (
        'user__email',
        'user__username',
        'user__first_name',
        'user__last_name',
        'phone_number'
    )
    list_filter = (
        'user__is_active',
        'user__is_staff',
        'created',
        'modified',
    )
    fieldsets = (
        (
            'Profile',
            {
                'fields': (('user', 'picture'),)
            }
        ),

        (
            'Extra info',
            {
                'fields': (
                    ('phone_number', 'website'),
                    ('biography'),
                )
            }
        ),
        (
            'Metadata',
            {
                'fields': (('created', 'modified'),)
            }
        ),
    )
    readonly_fields = ('created', 'modified')

class ProfileInline(admin.StackedInline):
        """Profile in-line admin for users."""
        model = Profile
        can_delete = False
        verbose_name_plural = 'profiles'

#admin.site.register(User)

class UserAdmin(BaseUserAdmin):
    """Add profile admin to base user admin."""
    inlines = (ProfileInline, )
    list_display = (
        'username',
        'first_name',
        'last_name',
        'is_active',
        'is_staff',
    )






@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    """Post Admin"""
    list_display = ('__str__', 'title', 'photo', 'created', 'modified')
    readonly_fields = ('created', 'modified')
    list_editable = ('title', 'photo')
    search_fields = (
        'profile__user__email',
        'profile__user__username',
        'profile__user__first_name',
        'profile__user__last_name',
        'title'
    )
    # list_filter = (
    #     'profile__user__is_active',
    #     'profile__user__is_staff',
    #     'created',
    #     'modified',
    # )