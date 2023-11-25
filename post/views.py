from django.shortcuts import HttpResponse, render
from datetime import date


def hello_view(request):
    if request.method == 'GET':
        return render(request, 'index.html')

def goodbye_view(request):
    if request.method == 'GET':
        return HttpResponse('Goodbye user!')

def current_date_view(request):
    if request.method == 'GET':
        today = date.today()
        return HttpResponse("Today's date:" + str(today))


