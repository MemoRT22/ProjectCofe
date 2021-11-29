from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,"core/home.html")

def about(request):
    return render(request,"core/about.html")

def visit_us(request):
    return render(request,"core/visitus.html")