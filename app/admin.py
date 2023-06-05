from django.contrib import admin
from .models import User

# Register your models here.

class MemberAdmin(admin.ModelAdmin):
    list_display="create_timestamp","update_timestamp","created_by"
admin.site.register(User,MemberAdmin)
