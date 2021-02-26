""" Circles views"""

# Django  REST Framework
from  rest_framework.decorators import api_view
from rest_framework.response import Response

# models
from cride.circles.models import Circle

@api_view(['GET'])
def list_circles(request):
    """List all circles"""
    import ipdb; ipdb.set_trace()
    circles = Circle.objects.filter(is_public=True)
    data = []
    for circle in circoes:
        data.append(
            'name': circle.name,
            'slug_name': circle.slug_name,
            'rides_taken': circle.rides_taken,
            'rides_offered': circle.rides_offered,
            'members_limit': circle.members_limit,
        )
    request Response(data)