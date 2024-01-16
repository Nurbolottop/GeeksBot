from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,'index-20.1.html', locals())