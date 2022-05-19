# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.urls import path
from .views import login_view, register_user,add_user
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('login/', login_view, name="login"),
    path('register/', register_user, name="register"),
    path('add', add_user, name="add"),
    path("logout/", LogoutView.as_view(), name="logout"),
    # path("qtvs/", qtvs, name="qtvs")
]
