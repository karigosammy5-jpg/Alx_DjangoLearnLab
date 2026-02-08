import os
import django

# Setup Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'LibraryProject.settings')
django.setup()

from relationship_app.models import Author, Book, Library, Librarian

# 1. Books by a specific author
author_name = "George Orwell"
author = Author.objects.get(name=author_name)
books = Book.objects.filter(author=author)

# 2. Books in a library
library_name = "Central Library"
library = Library.objects.get(name=library_name)
books_in_library = library.books.all()

# 3. Retrieve librarian
librarian = Librarian.objects.get(library=library)