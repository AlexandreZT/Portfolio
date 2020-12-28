from django.shortcuts import render

from .models import appname

# Create your views here.
def bienvenu(request):
# View code here...
    appnames = appname.objects
    return render(request, 'appname/accueil.html', {'appnames': appnames})