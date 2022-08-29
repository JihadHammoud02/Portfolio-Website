from django.contrib import admin

# Register your models here.
from django.contrib import admin

from .models import Personal,Skills, previous_jobs, projects, jihad,Education,experiences

admin.site.register(Personal)
admin.site.register(Skills)
admin.site.register(projects)
admin.site.register(jihad)
admin.site.register(Education)
admin.site.register(previous_jobs)
admin.site.register(experiences)