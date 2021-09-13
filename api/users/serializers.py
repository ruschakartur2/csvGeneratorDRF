from django.contrib.auth import get_user_model, authenticate
from django.contrib.auth.hashers import make_password
from rest_framework import serializers
from django.utils.translation import ugettext_lazy as _
from rest_framework.authtoken.models import Token

class UserRegistrationSerializer(serializers.ModelSerializer):
    """Serializer to register new user with token"""
    password = serializers.CharField(write_only=True)

    class Meta:
        model = get_user_model()
        fields = ("id", "username", "password")

    def validate(self, attrs):
        attrs['password'] = make_password(attrs['password'])
        return attrs


class UserLoginSerializer(serializers.Serializer):
    """Serializer for user authentication object"""
    username = serializers.CharField(required=True)
    password = serializers.CharField(
        required=True,
        style={'input_type': 'password'},
        trim_whitespace=False
    )

    def validate(self, attrs):
        """Validate and authenticate the user"""
        username = attrs.get('username')
        password = attrs.get('password')

        def __init__(self, *args, **kwargs):
            """Initialize serializer"""
            super(UserLoginSerializer, self).__init__(*args, **kwargs)
            self.user = None

        self.user = authenticate(
            request=self.context.get('request'),
            username=username,
            password=password
        )
        if not self.user:
            """Statement to check result of authenticate"""
            msg = _('Unable to authenticate with provided credentials')
            raise serializers.ValidationError(msg, code='authentication')
        attrs['user'] = self.user
        return attrs


class UserDetailSerializer(serializers.ModelSerializer):
    """Serializer for user detail  """

    class Meta:
        model = get_user_model()
        fields = ['id', 'username']


class TokenSerializer(serializers.ModelSerializer):
    """Serializer to authentication token"""
    auth_token = serializers.CharField(source='key')

    class Meta:
        model = Token
        fields = ('auth_token',)
        