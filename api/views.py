from rest_framework import generics
import json
from .models import *
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import AdminSerializer

# Create your views here.
@api_view(['POST'])
def api_home(request, *args, **kwargs):
    serializer = AdminSerializer(data=request.data)
    if serializer.is_valid():
        data = serializer.data
    return Response(serializer.data)

class AdminDetailAPIView(generics.RetrieveAPIView)    