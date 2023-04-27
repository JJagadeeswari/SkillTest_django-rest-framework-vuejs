from django.contrib import admin
from users.models import MyUser, Role, UserProfile, Logs

from rest_framework_simplejwt.token_blacklist.admin import OutstandingTokenAdmin
from rest_framework_simplejwt.token_blacklist.models import OutstandingToken, BlacklistedToken


# Register your models here.

#admin.site.register(MyUser)
@admin.register(MyUser)
class Model1Admin(admin.ModelAdmin):
    list_display = ('email',)


@admin.register(Role)
class Model1Admin(admin.ModelAdmin):
    list_display = ('id', 'role')


@admin.register(UserProfile)
class Model1Admin(admin.ModelAdmin):
    list_display = ('id', 'user_id', 'role_id')

@admin.register(Logs)
class Model1Admin(admin.ModelAdmin):
    list_display = ('id', 'user_id')


# Unregister TokenBlacklist models from admin site
admin.site.unregister(OutstandingToken)
admin.site.unregister(BlacklistedToken)

# Unregister TokenBlacklist admin from admin site
#admin.site.unregister(OutstandingTokenAdmin)

