from django.contrib import admin

from blog.models import Patient


# Register your models here.
@admin.register(Patient)

class testModelAdmin(admin.ModelAdmin):
    pass
