from django.contrib import admin
from .models import Student, Notice, Event, StudyMaterial, LostFound, Calendar

admin.site.register(Student)
admin.site.register(Notice)
admin.site.register(Event)
admin.site.register(StudyMaterial)
admin.site.register(LostFound)
admin.site.register(Calendar)