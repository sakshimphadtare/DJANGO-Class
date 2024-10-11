from django.urls import path
from . import views    # "." means root path
from . import api
from Myapp import api  #api.py file imported
from Myapp.api import *   #all classes imported

