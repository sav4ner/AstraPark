from os import name
from parkingApp.views import detailbookings,listbookings,detailcars,listcars,detailfavourites,listfavourites,detaillots,listlots,detailpremises,listpremises,detailusers,listusers
from django.urls import  path
from django.conf.urls import *
from django.contrib import admin


urlpatterns =[

    path("api/v1/bookings", listbookings.as_view(), name='bookimgs'),
    path("api/v1/bookings/<int:pk>/", detailbookings.as_view(), name='dbookimgs'),

    path("api/v1/cars", listcars.as_view(), name='cars'),
    path("api/v1/cars/<int:pk>/", detailcars.as_view(), name='dcars'),

    path("api/v1/favourites", listfavourites.as_view(), name='favourites'),
    path("api/v1/favourites/<int:pk>/", detailfavourites.as_view(), name='dfavourites'),

    path("api/v1/lots", listlots.as_view(), name='lots'),
    path("api/v1/lots/<int:pk>/", detaillots.as_view(), name='dlots'),

    path("api/v1/businessusers", listusers.as_view(), name='users'),
    path("api/v1/businessusers/<int:pk>/", detailusers.as_view(), name='dusers'),

    path("api/v1/premises", listpremises.as_view(), name='premises'),
    path("api/v1/premises/<int:pk>/", detailpremises.as_view(), name='dpremises'),
]