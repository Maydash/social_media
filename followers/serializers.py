from rest_framework import serializers
from profiles.serializers import UserByFollowerSerializer
from .models import Follower


class ListFollowerSerializer(serializers.ModelSerializer):
    subscriber = UserByFollowerSerializer(many=True, read_only=True)

    class Meta:
        model = Follower
        fields = ('subscriber',)



