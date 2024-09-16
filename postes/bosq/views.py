from django.shortcuts import render

# Create your views here.
def homepage(request):
    return render(request, 'homepage/index.html')

def about(request):
    return render(request, 'homepage/about.html')
def dashboard(request):
    return render(request, 'homepage/dashboard.html')