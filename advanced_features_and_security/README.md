# Role-Based Access Control (RBAC) in Django

This project implements a custom permission and grouping system to manage user access to application features.

## 1. Custom Permissions
Custom permissions were defined in the `models.py` within the `Meta` class of the chosen model. These permissions allow for granular control over user actions:
- `can_view`: Allows users to view model instances.
- `can_create`: Allows users to create new model instances.
- `can_edit`: Allows users to modify existing model instances.
- `can_delete`: Allows users to remove model instances.

## 2. User Groups and Roles
Users are categorized into three primary groups, each assigned specific permissions via the Django Admin interface:
- **Viewers**: Assigned the `can_view` permission.
- **Editors**: Assigned `can_view`, `can_create`, and `can_edit` permissions.
- **Admins**: Assigned all permissions, including `can_delete`.

## 3. View Protection
Access control is enforced at the view level using Django’s built-in decorators.
- The `@permission_required` decorator is used to ensure only users with the correct permission can access specific views.
- Example: `@permission_required('advanced_features_and_security.can_edit', raise_exception=True)` ensures that only authorized users can reach the edit page.

## 4. Setup Instructions
1. Run migrations to register the custom permissions: `python manage.py makemigrations` and `python manage.py migrate`.
2. Access the Django Admin panel.
3. Create the Groups (Viewers, Editors, Admins).
4. Assign the custom permissions to the respective groups.
5. Assign users to these groups to test the access levels.