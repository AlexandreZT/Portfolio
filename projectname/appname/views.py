from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def welcome(request):
    return HttpResponse(f"""
    <!DOCTYPE html>
    <html>
        <head>
            <meta charset="utf-8">
            <title>WELCOME</title>
        </head>
        <body>
            <h1>WELCOME ON UNKNOWN PROJECT</h1>
        </body>
    </html>
    """)

def bienvenu(request):
    # View code here...
    return render(request, 'index.html')