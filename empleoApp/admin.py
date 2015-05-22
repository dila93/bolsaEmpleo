from empleoApp.models import Usuario
from django.contrib import admin
from django.contrib.admin import ModelAdmin
from django.contrib.auth.models import User
# Register your models here.

class ArticleAdmin(admin.ModelAdmin):
    class Media:
        css = {
            "all": ("/my_styles.css",)
        }
        js = ("my_code.js",)



admin.site.register(Usuario,ArticleAdmin)
