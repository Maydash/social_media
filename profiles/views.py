from rest_framework import permissions
from rest_framework.viewsets import ModelViewSet
from .serializers import GetUserNetSerializers, GetUserNetPublicSerializers
from .models import UserNet


class UserNetViewPublicView(ModelViewSet):
    queryset = UserNet.objects.all()
    serializer_class = GetUserNetPublicSerializers
    permission_classes = [permissions.AllowAny]


class UserNetView(ModelViewSet):

    serializer_class = GetUserNetSerializers
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return UserNet.objects.filter(id=self.request.user.id)




