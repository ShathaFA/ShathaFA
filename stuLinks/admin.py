from django.contrib import admin
from .models import StuLinks
# Register your models here.
class StuLinksAdmin(admin.ModelAdmin):



admin.site.register(StuLinks,StuLinksAdmin)