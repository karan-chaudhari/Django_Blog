from django.shortcuts import render
import json

with open('config.json') as f:
    params = json.load(f)['params']

def home(request):
    context = {'params':params}
    return render(request, 'home.html', context)

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')    