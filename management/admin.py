from django.contrib import admin
from .models import Student_database,Engineering,Medical,ICS,ICom,Arts,Seience,subjects,UserAuth

# Register your models here.
admin.site.register(Student_database)
admin.site.register(Engineering)
admin.site.register(Medical)
admin.site.register(ICS)
admin.site.register(ICom)
admin.site.register(Arts)
admin.site.register(Seience)
admin.site.register(subjects)
admin.site.register(UserAuth)