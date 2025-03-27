from django.shortcuts import render
from .serializers import *
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import *
from django.db import DatabaseError

@api_view(['GET'])
def data(request):
    
    queryset = Data.objects.all()
    serializer = DataSerializer(queryset, many=True)
    return Response(serializer.data)
   
        


     



