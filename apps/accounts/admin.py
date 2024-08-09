from django.contrib import admin
from .models import Profile, User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'username', 'email', ]
    list_display_links = ['first_name', 'last_name', 'username', 'email', ]
    list_per_page = 25


class ProfileAdmin(admin.ModelAdmin):
    list_display = ['get_user',]
    list_display_links = ['get_user',]
    list_per_page = 25
    # list_filter = ['area',]

    def get_user(self, obj):
        return f"{obj.user.first_name} {obj.user.last_name}"
    get_user.short_description = 'Nome do Usuario'


admin.site.register(Profile, ProfileAdmin)
