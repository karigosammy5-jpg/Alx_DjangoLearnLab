# Security Implementation
- DEBUG set to False
- Configured SECURE_BROWSER_XSS_FILTER, X_FRAME_OPTIONS, and SECURE_CONTENT_TYPE_NOSNIFF
- Set CSRF_COOKIE_SECURE and SESSION_COOKIE_SECURE to True
- Implemented CSP using django-csp
- Used Django ORM to prevent SQL Injection
- Added CSRF tokens to templates
