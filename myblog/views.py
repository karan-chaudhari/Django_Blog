from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.core.paginator import Paginator
from django.utils import timezone
from .models import Contact, Comment, Post
import json

with open('config.json') as f:
    params = json.load(f)['params']

def home(request):
    posts_list = Post.objects.all()[::-1]
    paginator = Paginator(posts_list, 3)
    page = request.GET.get('page')
    posts = paginator.get_page(page)
    context = {'params':params, 'posts':posts}
    return render(request, 'home.html', context)

def about(request):
    context = {'params':params}
    return render(request, 'about.html', context)

def contact(request):
    if request.method == 'POST':
        name = request.POST["name"]
        email = request.POST["email"]
        phone = request.POST["phone"]
        msg = request.POST["msg"]
        cont = Contact(name=name, email=email, phone=phone, msg=msg)
        cont.save()
        messages.success(request,"Your details has been submitted. We will give you response very soon. Thank you so much.")
        return redirect('/contact')
    context = {'params':params}
    return render(request, 'contact.html', context)    

def post(request, slug):
    post = get_object_or_404(Post, slug=slug)
    if request.method == 'POST':
        name = request.POST["name"]
        cmnt = request.POST["cmnt"]
        post_cmnt = Comment(post_id=post, name=name, cmnt=cmnt)
        post_cmnt.save()   
    context = {'post':get_object_or_404(Post, slug=slug),
                'comments':Comment.objects.filter(post_id=post),
                'params':params}
    return render(request, 'post.html', context)    
     