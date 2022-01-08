from django.contrib import admin
from .models import Cities
# Register your models here.

@admin.register(Cities)
class cityAdmin(admin.ModelAdmin):
    list_to_display = ['Id','name','month','utilities'] 
