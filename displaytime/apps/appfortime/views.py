from django.shortcuts import render,HttpResponse,redirect
from datetime import datetime

# Create your views here.
def main(request):
    time_data = {
        'date': datetime.strftime(datetime.now(), '%b %d, %Y'),
        'time': datetime.strftime(datetime.now(), '%I:%M %p')    
    }
    return render(request, 'appfortime/index.html', time_data)
    