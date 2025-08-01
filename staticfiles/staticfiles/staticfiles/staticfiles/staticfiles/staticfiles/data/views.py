from django.shortcuts import render, redirect, get_object_or_404
from data.models import *
from django.contrib.auth import authenticate, login, logout
from django.http import Http404
from django.urls import reverse
# Create your views here.
#!
#@
#?
#*
#&
#^
#~
#//

#^ ---- PAGES -------------------


#& ------------ HOME CODE -------
def indexViews(request):
    context = {}
    return render(request, "pages/index.html", context)

#& ------------ ABOUT CODE -------
def aboutViews(request):
    context = {}
    return render(request, "pages/about.html", context)

#& ------------ CONTACT CODE -------
def contactViews(request):
    context = {}
    return render(request, "pages/contact.html", context)