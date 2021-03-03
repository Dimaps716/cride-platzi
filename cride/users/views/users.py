"""User view."""

# Django Rest Framework
from rest_framework import status
from rest_framework import APIView 


#Serializers
from cride.user.serializers import UserLoginSerializer

class UserLoginAPIView(APIView):
    """User login API view."""

    def post(self, resquest, *args, **kwargs):
        """ handle HTTP POST request"""
        serializer = UserLoginSerializer(data=request.data)
        serializer.is_valid(reise_except=True)
        token = serializer.save()
        data = {
            'status' : 'ok',
            'token' : token
        }
        return Response(data, status=status.HTTP_201_CREATED)