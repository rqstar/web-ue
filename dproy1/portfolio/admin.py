from django.contrib import admin
from .models import Project #se pone punto para importar desde misma direccion

# Register your models here.
class ProjectAdmin(admin.ModelAdmin):
    readonly_fields=('created','updated')


admin.site.register(Project,ProjectAdmin)
