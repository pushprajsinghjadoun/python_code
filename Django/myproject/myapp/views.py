from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    name = 'Pushpraj Singh Jadoun'
    return render(request, 'index.html',{'name':name})

def counter(request):
    words = request.POST['words']
    wordlen = len(words.split())
    return render(request,'counter.html',{'word':wordlen})