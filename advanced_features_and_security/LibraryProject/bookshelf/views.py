from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import permission_required
from .models import Book
from .forms import ExampleForm
# --- SECURITY: SECURE DATA ACCESS (Step 3) ---

@permission_required('bookshelf.can_view', raise_exception=True)
def book_list(request):
    """
    Securely lists all books using Django's ORM. 
    ORM automatically prevents SQL injection by parameterizing queries.
    """
    books = Book.objects.all()
    return render(request, 'bookshelf/book_list.html', {'books': books})

# Example of a secure search view using the ORM
@permission_required('bookshelf.can_view', raise_exception=True)
def search_books(request):
    query = request.GET.get('q')
    if query:
        # SECURE: Use icontains (ORM) instead of raw SQL strings
        books = Book.objects.filter(title__icontains=query)
    else:
        books = Book.objects.all()
    return render(request, 'bookshelf/book_list.html', {'books': books})

# --- PERMISSIONS: ENFORCING ACCESS CONTROL ---

@permission_required('bookshelf.can_create', raise_exception=True)
def add_book(request):
    # Ensure forms use {% csrf_token %} in the template
    return render(request, 'bookshelf/add_book.html')

@permission_required('bookshelf.can_edit', raise_exception=True)
def edit_book(request, pk):
    book = get_object_or_404(Book, pk=pk)
    return render(request, 'bookshelf/edit_book.html', {'book': book})

@permission_required('bookshelf.can_delete', raise_exception=True)
def delete_book(request, pk):
    book = get_object_or_404(Book, pk=pk)
    return render(request, 'bookshelf/delete_book.html', {'book': book})