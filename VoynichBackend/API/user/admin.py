from django.contrib import admin
from django.contrib.auth.models import Group
from rest_framework.authtoken.models import Token

from API.user.models.user import User

admin.autodiscover()


class UserAdmin(admin.ModelAdmin):
    exclude = ('groups', 'user_permissions',)


admin.site.register(User, UserAdmin)

admin.site.unregister(Group)
admin.site.unregister(Token)
