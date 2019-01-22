from django.shortcuts import render
import json

with open('config.json') as f:
    params = json.load(f)['params']

def home(request):
    context = {'params':params}
    return render(request, 'home.html', context)

def about(request):
    context = {'params':params}
    return render(request, 'about.html', context)

def contact(request):
    context = {'params':params}
    return render(request, 'contact.html', context)    