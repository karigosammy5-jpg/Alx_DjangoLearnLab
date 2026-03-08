from django.shortcuts import render
from rest_framework import viewsets, permissions, generics, status
from .models import Post, Comment, Like
from .serializers import PostSerializer, CommentSerializer
from notifications.models import Notification
from django.contrib.contenttypes.models import ContentType
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

# Step 3 Task: The Feed Logic
class FeedView(generics.ListAPIView):
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        following_users = self.request.user.following.all()
        # Filter posts where the author is in the list of users the current user follows
        return Post.objects.filter(author__in=following_users).order_by('-created_at')

class LikePostView(generics.GenericAPIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, pk):
        post = get_object_or_404(Post, pk=pk)
        # 1. Use get_or_create to prevent duplicate likes
        like, created = Like.objects.get_or_create(user=request.user, post=post)
        
        if created:
            # 2. Generate Notification
            Notification.objects.create(
                recipient=post.author,
                actor=request.user,
                verb="liked your post",
                target=post,
                target_content_type=ContentType.objects.get_for_model(post),
                target_object_id=post.id
            )
            return Response({"message": "Post liked"}, status=status.HTTP_201_CREATED)
        return Response({"message": "You already liked this post"}, status=status.HTTP_400_BAD_REQUEST)

class UnlikePostView(generics.GenericAPIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, pk):
        post = get_object_or_404(Post, pk=pk)
        like = Like.objects.filter(user=request.user, post=post)
        if like.exists():
            like.delete()
            return Response({"message": "Post unliked"}, status=status.HTTP_200_OK)
        return Response({"message": "You haven't liked this post"}, status=status.HTTP_400_BAD_REQUEST)
