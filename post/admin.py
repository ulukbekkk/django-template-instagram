from django.contrib import admin
from .models import *

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'created_at',)
    list_filter = ('created_at',)
    prepopulated_fields = {'slug': ('title', )}

admin.site.register(Post)
