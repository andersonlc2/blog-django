from django.contrib import admin

from .models import BlogPost

# Register your models here.


class BlogPostAdmin(admin.ModelAdmin):
    fields = ['title', 'text']
    list_display = ('title', 'date_added', 'recently')
    list_filter = ['date_added']
    search_fields = ['title']


admin.site.register(BlogPost, BlogPostAdmin)
