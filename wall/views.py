from rest_framework import  permissions, generics

from base.classes import CreateUpdateDestroyDS, CreateRetrieveUpdateDestroyDS
from base.permissions import IsAuthorEntry, IsMemberGroup, IsAuthorCommentEntry,IsAuthorComment
from .serializers import CreateCommentSerializer, ListCommentSerializer, PostSerializer, ListPostSerializer
from .models import Post, Comment


class PostListView(generics.ListAPIView):
    """List Post on User wall"""
    serializer_class = ListPostSerializer

    def get_queryset(self):
        return Post.objects.filter(user_id=self.kwargs.get('pk')).select_related('user').prefetch_related('comments')


class PostView(CreateRetrieveUpdateDestroyDS):
    """CRUD Post"""
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Post.objects.all().select_related('user').prefetch_related('comments')
    serializer_class = PostSerializer
    permission_classes_by_action = {'get': [permissions.AllowAny],
                                    'update': [IsAuthorComment],
                                    'destroy': [IsAuthorComment],
                                    }

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class CommentView(CreateUpdateDestroyDS):
    """CRUD Comment to Post"""
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Comment.objects.all()
    serializer_class = CreateCommentSerializer
    permission_classes_by_action = {'update': [IsAuthorComment],
                                    'destroy': [IsAuthorComment],
                                    }

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def perform_destroy(self, instance):
        instance.deleted = True
        instance.save()

