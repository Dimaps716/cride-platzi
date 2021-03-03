"""User serializers.""" 

# Django Rest Framework
from rest_framework import serializers

class UserLoginSerializer(serializers.Serializer):
    """User login serializer.
    Handle the login request data"""

    email = serializers.EmailField()
    password = serializer.CharField(min_length=8, max_length=68)

    def validate(self,data):
        """check credentials."""
        user = authenticate(username=data['email'], password=data['password'])
        if not user:
            raise serializers.ValidationError('Invalid credentials')
        return data