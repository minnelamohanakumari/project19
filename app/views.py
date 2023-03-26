from django.shortcuts import render
# Create your views here.
def sample(request):
    return render(request,'sample.html')
def virat(request):
    return render(request,'virat.html')