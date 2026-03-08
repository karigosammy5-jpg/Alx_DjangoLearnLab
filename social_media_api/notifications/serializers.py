from rest_framework import serializers
from .models import Notification

class NotificationSerializer(serializers.ModelSerializer):
    # These fields help make the notification readable (e.g., "Sammy" instead of "User ID 1")
    actor = serializers.ReadOnlyField(source='actor.username')
    recipient = serializers.ReadOnlyField(source='recipient.username')

    class Meta:
        model = Notification
        fields = [
            'id', 
            'actor', 
            'recipient', 
            'verb', 
            'timestamp', 
            'unread',
            'target_content_type',
            'target_object_id'
        ]