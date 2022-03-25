from django.shortcuts import render
from rest_framework import generics
from  django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse



# Create your views here.
from parkingApp.models import bookings, premises, lots,car,businessusers,favourites
from parkingApp.serializers import bookingSerializers, premisesSerializers,lotsSerializers,carSerializers,businessUserSerializers, favouritesSerializers

class detailbookings (generics.RetrieveUpdateDestroyAPIView):
    queryset = bookings.objects.all()
    serializer_class = bookingSerializers

class listbookings (generics.ListCreateAPIView):
    queryset = bookings.objects.all()
    serializer_class = bookingSerializers

class detailpremises (generics.RetrieveUpdateDestroyAPIView):
    queryset = premises.objects.all()
    serializer_class = premisesSerializers

class listpremises (generics.ListCreateAPIView):
    queryset = premises.objects.all()
    serializer_class = premisesSerializers

class detaillots (generics.RetrieveUpdateDestroyAPIView):
    queryset = lots.objects.all()
    serializer_class = lotsSerializers

class listlots (generics.ListCreateAPIView):
    queryset = lots.objects.all()
    serializer_class = lotsSerializers

class detailcars (generics.RetrieveUpdateDestroyAPIView):
    queryset = car.objects.all()
    serializer_class = carSerializers

class listcars (generics.ListCreateAPIView):
    queryset = car.objects.all()
    serializer_class = carSerializers

class detailusers (generics.RetrieveUpdateDestroyAPIView):
    queryset = businessusers.objects.all()
    serializer_class = businessUserSerializers

class listusers (generics.ListCreateAPIView):
    queryset = businessusers.objects.all()
    serializer_class = businessUserSerializers

class detailfavourites (generics.RetrieveUpdateDestroyAPIView):
    queryset = favourites.objects.all()
    serializer_class = favouritesSerializers

class listfavourites (generics.ListCreateAPIView):
    queryset = favourites.objects.all()
    serializer_class = favouritesSerializers