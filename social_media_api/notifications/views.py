from rest_framework import generics, permissions, status
from .models import Notification
from .serializers import NotificationSerializer
from rest_framework.response import Response

class NotificationListView(generics.ListAPIView):
    serializer_class = NotificationSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        # Returns notifications for the logged-in user, newest first
        return self.request.user.notifications.all().order_by('-timestamp')
    
class MarkAsReadView(generics.GenericAPIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, pk):
        notification = Notification.objects.get(pk=pk, recipient=request.user)
        notification.unread = False
        notification.save()
        return Response({"message": "Notification marked as read"}, status=status.HTTP_200_OK)