from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Refuel
from .serializers import RefuelSerializer

# Create your views here.

def getRefuels(request):
    if request.User is not None:
        refuels = Refuel.objects.filter(user=request.User)
        serializer = RefuelSerializer(refuels, many=True)
        return Response(serializer)
    return Response({'message': 'User is undefined.'})