from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def home(request):
    return render(request, 'posts/index.html', {})
    #return HttpResponse("<h1>Hello, Blog App</h1>")

def post_detail(request):
    return HttpResponse("<h1>Hello, Blog App post_detail</h1>")

def post_update(request):
    return HttpResponse("<h1>Hello, Blog App post_update</h1>")

def post_delete(request):
    return HttpResponse("<h1>Hello, Blog App post_delete</h1>")
