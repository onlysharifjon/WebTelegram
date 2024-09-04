from django.contrib import admin

# Register your models here.
from .models import Foydalanuvchilar,ChatModel


class FoydalanuvchiAdmin(admin.ModelAdmin):
    list_display = ['name', 'surname', 'email']
    search_fields = ["email"]


admin.site.register(Foydalanuvchilar, FoydalanuvchiAdmin)
admin.site.register(ChatModel,list_display = ['kim_yozdi','kimga_yozdi',"vaqt"])