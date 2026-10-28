# from django.contrib import admin
# from .models import Task, Project, Tag


# admin.site.register(Task)
# admin.site.register(Project)
# admin.site.register(Tag)

from django.contrib import admin
from .models import SecurityLog

# Register your models here.
from .models import Project, Task, Tag, ProjectMembership

admin.site.register(Task)
admin.site.register(Project)
admin.site.register(Tag)
admin.site.register(ProjectMembership)
admin.site.register(SecurityLog)
