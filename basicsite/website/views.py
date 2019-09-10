from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.template import loader

# Create your views here.
def index(request):
    return HttpResponse('hi')

def about(request):
    context = {
        'name': 'ivo'
    }
    return render(request, 'website/about.html', context)

def api(request):
    responseData = {
        'id': 4,
        'name': 'Test Response',
        'roles' : ['Admin','User']
    }
    return JsonResponse(responseData)