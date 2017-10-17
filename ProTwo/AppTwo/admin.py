from django.contrib import admin
from AppTwo.models import (Topic, WebUsers)

class WebUsersAdmin(admin.ModelAdmin):
    list_display = ('name', 'lname', 'email')

class TopicsAdmin(admin.ModelAdmin):
    list_display = ('top_name',)

admin.site.register(Topic, TopicsAdmin)
admin.site.register(WebUsers, WebUsersAdmin)
