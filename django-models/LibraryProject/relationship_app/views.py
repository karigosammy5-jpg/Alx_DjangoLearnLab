from django.shortcuts import render
from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth.decorators import permission_required
# Check functions
def is_admin(user):
    return user.is_authenticated and user.userprofile.role == 'Admin'

def is_librarian(user):
    return user.is_authenticated and user.userprofile.role == 'Librarian'

def is_member(user):
    return user.is_authenticated and user.userprofile.role == 'Member'

# Admin View
@user_passes_test(is_admin)
def admin_view(request):
    return render(request, 'relationship_app/admin_view.html')

# Librarian View
@user_passes_test(is_librarian)
def librarian_view(request):
    return render(request, 'relationship_app/librarian_view.html')

# Member View
@user_passes_test(is_member)
def member_view(request):
    return render(request, 'relationship_app/member_view.html')
# Views with custom permissions

@permission_required('relationship_app.can_add_book')
def add_book(request):
    # logic here
    return render(request, 'relationship_app/add_book.html')

@permission_required('relationship_app.can_change_book')
def edit_book(request, pk):
    # logic here
    return render(request, 'relationship_app/edit_book.html')

@permission_required('relationship_app.can_delete_book')
def delete_book(request, pk):
    # logic here
    return render(request, 'relationship_app/delete_book.html')