
# LibraryProject - Advanced Features and Security

This project is a Django-based library management system focused on implementing advanced security features, custom permissions, and secure web communication.

## Project Structure
- **LibraryProject/**: The main project directory.
- **advanced_features_and_security/**: A specialized app focusing on:
    - **HTTPS & Secure Headers**: Enforcing SSL redirects and HSTS.
    - **RBAC (Role-Based Access Control)**: Implementing custom permissions (can_view, can_edit, etc.) and user groups (Viewers, Editors, Admins).

## How to Run
1. Install requirements.
2. Run `python manage.py migrate`.
3. Start the server with `python manage.py runserver`.

