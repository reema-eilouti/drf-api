from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .models import Fact
from .serializers import FactSerializer

# Create your views here.

class FactsList(ListCreateAPIView):
    queryset = Fact.objects.all()
    serializer_class = FactSerializer

class FactsDetail(RetrieveUpdateDestroyAPIView):
    queryset = Fact.objects.all()
    serializer_class = FactSerializer