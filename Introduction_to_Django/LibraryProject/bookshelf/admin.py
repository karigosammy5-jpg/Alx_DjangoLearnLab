from django.contrib import admin
from .models import Book

# 1. Define the Custom Admin Class
class BookAdmin(admin.ModelAdmin):
    # Display these fields in the list view
    list_display = ('title', 'author', 'publication_year')
    
    # Add a search bar for title and author
    search_fields = ('title', 'author')
    
    # Add a filter sidebar for publication year
    list_filter = ('publication_year',)

# 2. Register the model with the custom class
admin.site.register(Book, BookAdmin)
