from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext, loader

# Create your views here.
def index(request):
    context = {'name': 'Ronald Snyder'}
    return render(request, 'mysite/index.html', context)
