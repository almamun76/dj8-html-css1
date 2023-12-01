from django.urls import path

# import projDesign>appDesign>views.py file here
from . import views

urlpatterns = [
    # url for home() view created in projDesign>appDesign>views.py file
    path('', views.home),
]
# this appDesign>urls.py file have to include in projDesign>urls.py file