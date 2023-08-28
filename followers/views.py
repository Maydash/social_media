from .serializers import ListFollowerSerializer
from profiles.models import UserNet
from .models import Follower
from rest_framework import generics, permissions, views, response


class ListFollowerView(generics.ListAPIView):
    """Show List followers"""
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = ListFollowerSerializer

    def get_queryset(self):
        return Follower.objects.filter(user=self.request.user)


class FollowerView(views.APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, pk):
        try:
            user = UserNet.objects.get(id=pk)
        except Follower.DoesNotExist:
            return response.Response(status=404)
        Follower.objects.create(subscriber=request.user, user=user)
        return response.Response(status=201)

    def delete(self, request, pk):
        try:
            sub = Follower.objects.get(subscriber=request.user, user_id=pk)
        except Follower.DoesNotExist:
            return response.Response(status=404)
        sub.delete()
        return response.Response(status=204)






