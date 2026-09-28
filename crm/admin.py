from django.contrib import admin
from .models import Customer

@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ("name", "email", "phone", "company", "status", "created_at")
    list_filter = ("status", "city", "created_at")
    search_fields = ("name", "email", "phone", "company", "city")
    ordering = ("-created_at",)
