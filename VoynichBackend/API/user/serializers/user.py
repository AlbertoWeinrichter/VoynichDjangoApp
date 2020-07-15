from rest_framework import serializers

from API.user.models.user import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            "username",
            "avatar",
            "avatar_cropped"
        )
