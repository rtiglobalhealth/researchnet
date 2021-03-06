from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User

from core.models import Participant

# Define an inline admin descriptor for Participant model
# which acts a bit like a singleton
class ParticipantInline(admin.StackedInline):
    model = Participant
    can_delete = False
    verbose_name_plural = 'participant'

# Define a new User admin
class UserAdmin(BaseUserAdmin):
    inlines = (ParticipantInline, )

# Re-register UserAdmin
admin.site.unregister(User)
admin.site.register(User, UserAdmin)