from django.contrib import admin
from AppTwo.models import (Topic, WebUsers)

class WebUsersAdmin(admin.ModelAdmin):
    """
    It's used to split the lists in more than on collumn
    and show all the items in it
    """
    list_display = ('name', 'lname', 'email')

class TopicsAdmin(admin.ModelAdmin):
    list_display = ('top_name',)

admin.site.register(Topic, TopicsAdmin)
admin.site.register(WebUsers, WebUsersAdmin) #This will register the collumn of the objects
#The second parameter it's if you want to split the items in collumns
