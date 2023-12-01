from django.shortcuts import render

# Create your views here.

# creating function based home() view (custom)
# an url for this view have to create in projDesign>appDesign>urls.py file
def home(request):
    return render(request, 'home/index.html')