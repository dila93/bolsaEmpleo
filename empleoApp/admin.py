from empleoApp.models import Usuario
from django.contrib import admin

# Register your models here.

class editarInfo(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['usuario']}),
        (None,               {'fields': ['tipo_user']}),
        (None,               {'fields': ['nombres']}),
        (None,               {'fields': ['apellidos']}),
    ]

    list_display = ('usuario', 'tipo_user','nombres','apellidos')

admin.site.register(Usuario, editarInfo)