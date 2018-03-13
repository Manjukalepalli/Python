from django.shortcuts import render,HttpResponse
import random
from django.utils.crypto import get_random_string

# Create your views here.
def main(request):
    if 'attempt' in request.session:
        request.session["attempt"]+=1
    else:
        request.session["attempt"]=1
    request.session['randomString']= get_random_string(length=14)
    return render(request,'showword/index.html')