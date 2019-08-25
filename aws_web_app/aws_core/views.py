from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    my_dict = {'insert_me': "Mj test!"}
    return render(request, 'aws_core/index.html', context=my_dict)