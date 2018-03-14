from django.shortcuts import render,HttpResponse,redirect

# Create your views here.
def main(request):
    if 'counter' not in request.session:
        request.session['counter'] = 0 #initialize the counter
    return render(request,"myform/index.html")

def process(request):
    if request.method == 'POST':  #user has completed form, process data
        request.session['counter'] += 1  #count number of times user submits
        request.session['name'] = request.POST['name']
        request.session['location'] = request.POST['location']
        request.session['language'] = request.POST['language']
        request.session['comment'] = request.POST['comment']
        return redirect('/result')
    else:
        return redirect('/')
    
def result(request):
    return render(request,"myform/result.html")