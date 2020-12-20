from django.shortcuts import render
from django.http import HttpResponse
from .models import appname
# Create your views here.
def welcome(request):
    return HttpResponse(f"""
    <!DOCTYPE html>
    <html>
        <head>
            <meta charset="utf-8">
            <title>WELCOME</title>
        </head>
        <body style='background-color:grey;'>
            <h1 style='color:blue;'>WELCOME ON UNKNOWN PROJECT</h1>
        </body>
    </html>
    """)

def bienvenu(request):
    appnames = appname.objects
    # View code here...
    # return render(request, 'index.html')
    return render(request, 'index.html', {'appnames': appnames})