from django.contrib import admin
from .models import Book, BookNumber


# Register your models here.
# admin.site.register(Book)

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    fields = ['title', 'description', 'price', 'published', 'is_published', 'cover', 'pages']
    list_display = ['title', 'description']
    list_filter = ['published']
    search_fields = ['title']


admin.site.register(BookNumber)
