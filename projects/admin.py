from django.contrib import admin

# Register your models here.
from .models import Project,Review,Tag #we are importing the database we have created in this instance project 


admin.site.register(Project)
admin.site.register(Review)
admin.site.register(Tag)