from django.shortcuts import render
import json
from .models import *
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import *
# Create your views here.
@api_view(['POST'])
def api_home(request, *args, **kwargs):
    data= request.data
    serializer = SkillSerializer(data)
    if serializer.is_valid():
        print(seralizer.data)
        data = seralizer.data
    return Response(data)