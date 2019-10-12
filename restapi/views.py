from django.shortcuts import render
from rest_framework import generics
from ipl.models import Match,Delivery
from .serializers import MatchSerializer, DeliverySerializer
# Create your views here.

class ListMatchesView(generics.ListCreateAPIView):
    queryset = Match.objects.all()
    serializer_class = MatchSerializer

class ListDeliveriesView(generics.ListCreateAPIView):
    queryset = Delivery.objects.all()
    serializer_class = DeliverySerializer

class ListDetailMatch(generics.RetrieveUpdateDestroyAPIView):
    queryset= Match.objects.all()
    serializer_class = MatchSerializer

class ListDetailDelivery(generics.RetrieveUpdateDestroyAPIView):
    queryset = Delivery.objects.all()
    serializer_class = DeliverySerializer