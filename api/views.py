from django.shortcuts import render
from .models import *
from rest_framework.response import Response
from rest_framework.decorators import api_view

# Create your views here.
@api_view(['GET'])
def api_home(request, *args, **kwargs):
    pass