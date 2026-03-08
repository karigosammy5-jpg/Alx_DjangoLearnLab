from django.urls import path, include
from .views import NotificationListView, MarkAsReadView
urlpatterns = [
    path('', NotificationListView.as_view(), name='notification-list'),
]