import os
from cgi import print_directory
from django.http import HttpResponse
from django.shortcuts import render

def antlr(request):
    line = ''.join(list(request.POST.values()))
    grammarFile = open('static/antlr/fsm.g', 'w+')
    grammarFile.write(line)
    grammarFile.close()
    os.system('java -jar .\\static\\antlr-3.3-complete.jar .\\static\\antlr\\fsm.g')
    return HttpResponse(status=201)

def index(request):
    return render(request, 'main/index.html')


# Create your views here.
