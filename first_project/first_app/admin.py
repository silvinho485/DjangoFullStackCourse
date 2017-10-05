from django.contrib import admin
from first_app.models import (AccesRecord,
                                Topic,
                                Webpage)

admin.site.register(AccesRecord)
admin.site.register(Topic)
admin.site.register(Webpage)
# Register your models here.
