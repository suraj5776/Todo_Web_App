from django.contrib import admin
from .models import TodoTable

# Register your models here.
class show_table(admin.ModelAdmin):
    list_display = ("id", "text", "created")


admin.site.register(TodoTable, show_table)
