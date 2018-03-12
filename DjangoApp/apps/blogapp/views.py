from django.shortcuts import render,HttpResponse,redirect

# Create your views here.
def index(requst):
    response = "placeholder to later display all the list of blogs"
    return HttpResponse(response)

def new(request):
    response = "placeholder to display a new form to create a new blog"
    return HttpResponse(response)

def create(request):
    return redirect('/')    

def main(request):
    response = "this is main page"
    return HttpResponse(response)

def showblog(request,number):
    response = "this is a place holder to display blog number: "+str(number)
    return HttpResponse(response)

def edit(request,number):
    response = "this is a place holder to edit blog number: "+str(number)
    return HttpResponse(response)

def delete(request,number):
    response = "this is a place holder to delete blog number: "+str(number)
    return HttpResponse(response)    