from rest_framework import serializers
from users.models import CustomUser


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('id', 'username', 'email', 'password')
        extra_kwargs = {'password': {'write_only': True, 'min_length': 8},
                        'email': {'required': True}, }

    def create(self, validated_data):
        user = CustomUser.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password']
        )

        return user

    def update(self, instanse, validated_data):
        instanse.username = validated_data.get('username', instanse.username)
        instanse.email = validated_data.get('email', instanse.email)

        if 'password' in validated_data:
            instanse.set_password(validated_data['password'])

        instanse.save()

        return instanse


class ChangePasswordSerializer(serializers.ModelSerializer):
    old_password = serializers.CharField(write_only=True)
    new_password = serializers.CharField(write_only=True, min_length=8)
