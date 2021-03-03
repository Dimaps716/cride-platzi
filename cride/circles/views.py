""" Circles views"""

# Django  REST Framework
from  rest_framework.decorators import api_view
from rest_framework.response import Response

# models
from cride.circles.models import Circle

#serializer
from cride.circles.serializers import (
    CircleSerializer,
    CreateCircleSerializer
)



@api_view(['GET'])
def list_circles(request):
    """List all circles"""
    circles = Circle.objects.filter(is_public=True)
    serializer = CircleSerializer(circles, many=True)
    return Response(serializer.data)


@api_view(['POST'])
def create_circle(request):
    """Create circles"""
    serializer = CreateCircleSerializer(data=request.data)
    serializer.is_valid(reise_except=True)
    data = serializer.data
    circles = Circles.objects.create(**data)
    return Response(CreateCircleSerializer(circle).data)


