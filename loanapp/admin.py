from django.contrib import admin

# Register your models here.

from . models import Application

'''
class ApplicationAdmin(admin.ModelAdmin):
    readonly_fields = ('highlighted',)
'''

admin.site.register(Application)