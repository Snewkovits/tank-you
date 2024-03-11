from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Refuel
from .serializers import RefuelSerializer

from django.contrib.auth.models import AnonymousUser

# Create your views here.

@api_view(['GET'])
def getRefuels(request):
    if not isinstance(request.user, AnonymousUser):
        refuels = Refuel.objects.filter(user=request.user)
        serializer = RefuelSerializer(refuels, many=True)
        return Response(serializer.data)
    return Response({'message': 'User is undefined.'})