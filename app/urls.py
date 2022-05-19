# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.urls import path, re_path
from app import views

urlpatterns = [

    # The home page
    path('', views.index, name='home'),
    path("apply",views.apply, name="apply"),
    # path("getdetails",views.getdetails, name="getdetails"),
    path("requests",views.requests, name="requests"),
    path("applications",views.applications, name="applications"),
    path("filter",views.filter, name="filter"),
    path("cardsall",views.cardsall, name="cardsall"),
    path("cardsrejected",views.cardsrejected, name="cardsrejected"),
    path("cardsselected",views.cardsselected, name="cardsselected"),
    path("cardsprocessing",views.cardsprocessing, name="cardsprocessing"),
    path("dated",views.dated, name="dated"),
    path("filter_district",views.filter_district, name="filter_district"),
   

    # Matches any html file
    re_path(r'^.*\.*', views.pages, name='pages'),

]
