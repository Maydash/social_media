from rest_framework import serializers
from base.serializers import RecursiveSerializer, FilterCommentListSerializer
from .models import Post, Comment


class CreateCommentSerializer(serializers.ModelSerializer):
    """Add comment to post"""
    class Meta:
        model = Comment
        fields = ('post', 'text', 'parent')


class ListCommentSerializer(serializers.ModelSerializer):
    """List of comments"""
    text = serializers.SerializerMethodField()
    children = RecursiveSerializer(many=True)
    user = serializers.ReadOnlyField(source='user.username')

    def get_text(self, obj):
        if obj.deleted:
            return None
        return obj.text

    class Meta:
        list_serializer_class = FilterCommentListSerializer
        model = Comment
        fields = ('id', 'user', 'post', 'text', 'created_date', 'update_date', 'deleted', 'children')


class PostSerializer(serializers.ModelSerializer):
    """Show and change Post"""
    user = serializers.ReadOnlyField(source='user.username')
    comments = ListCommentSerializer(many=True, read_only=True)
    view_count = serializers.CharField(read_only=True)

    class Meta:
        model = Post
        fields = ('id', 'create_date', 'user', 'text', 'comments', 'view_count')


class ListPostSerializer(serializers.ModelSerializer):
    """List of Posts"""
    user = serializers.ReadOnlyField(source='user.username')

    class Meta:
        model = Post
        fields = ('id', 'create_date', 'user', 'text', 'comments_count')




