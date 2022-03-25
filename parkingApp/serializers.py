from inspect import formatannotationrelativeto
from pyexpat import model
from statistics import mode
from django.forms import fields
from rest_framework import serializers

from parkingApp.models import bookings,premises,lots,car,businessusers,favourites

class bookingSerializers(serializers.ModelSerializer):
    class Meta:
        model = bookings
        fields = (
            'bookingId',
            'user',
            'platenumber',
            'email',
            'contact',
            'date',
            'start',
            'stop',
            'lots',
            'bill'
        )

class premisesSerializers(serializers.ModelSerializer):
    class Meta:
        model = premises
        fields = (
            'name',
            'space'
        )

class lotsSerializers(serializers.ModelSerializer):
   class Meta:
        model = lots
        fields = (
            'lotId',
            'area',
            'location',
            'premises',
            'rating',
            'price',
            'status'
        )

class carSerializers(serializers.ModelSerializer):
   class Meta:
        model = car
        field = (
            'platenumber',
            'owner',
            'carstate',
            'cartype'
        )

class businessUserSerializers(serializers.ModelSerializer):
    class Meta:
        model = businessusers
        fields = (
            'businessId',
            'user',
            'premises',
            'fullname',
            'email',
            'dividents'
        )

class favouritesSerializers(serializers.ModelSerializer):
    class Meta:
        model = favourites
        field = (
            'lotId'
        )