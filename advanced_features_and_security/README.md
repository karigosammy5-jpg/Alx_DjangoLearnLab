Permissions and Groups Documentation
-----------------------------------
Custom Permissions:
- can_view: Allows viewing book list.
- can_create: Allows adding new books.
- can_edit: Allows editing book details.
- can_delete: Allows removing books.

Groups and Assigned Permissions:
- Viewers: can_view
- Editors: can_view, can_create, can_edit
- Admins: All permissions (can_view, can_create, can_edit, can_delete)
