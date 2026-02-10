# Permissions and Groups Setup

## Permissions
The Book model has the following custom permissions:
- can_view: Allows users to view book details.
- can_create: Allows users to add new books.
- can_edit: Allows users to modify existing books.
- can_delete: Allows users to remove books.

## Groups
1. **Viewers**: Assigned the can_view permission.
2. **Editors**: Assigned can_view, can_create, and can_edit.
3. **Admins**: Assigned all permissions.
