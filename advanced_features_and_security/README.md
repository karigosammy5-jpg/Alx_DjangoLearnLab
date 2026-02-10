# Advanced Features and Security

## Custom Permissions
Implemented in models.py for the Book model:
- can_view
- can_create
- can_edit
- can_delete

## Groups
- **Viewers**: can_view
- **Editors**: can_view, can_create, can_edit
- **Admins**: All permissions
