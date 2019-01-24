from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.core.paginator import Paginator
from django.utils import timezone
from django.db.models import Q
from .models import Contact, Comment, Categorie, Post
import json

with open('config.json') as f:
    params = json.load(f)['params']

categories = Categorie.objects.order_by('categ')

def home(request):
    posts_list = Post.objects.all()[::-1]
    paginator = Paginator(posts_list, 3)
    page = request.GET.get('page')
    posts = paginator.get_page(page)
    context = {'params':params, 'posts':posts, 'cates':categories}
    return render(request, 'home.html', context)

def about(request):
    context = {'params':params, 'cates':categories}
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
    context = {'params':params, 'cates':categories}
    return render(request, 'contact.html', context)    

def post(request, slug):
    post = get_object_or_404(Post, slug=slug)
    if request.method == 'POST':
        name = request.POST["name"]
        cmnt = request.POST["cmnt"]
        post_cmnt = Comment(post_id=post, name=name, cmnt=cmnt)
        post_cmnt.save()   
        messages.success(request, "Your comment published successfully.")
    context = {'post':get_object_or_404(Post, slug=slug),
                'comments':Comment.objects.filter(post_id=post),
                'params':params, 'cates':categories}
    return render(request, 'post.html', context)    

def category(request, categ):
    cate = get_object_or_404(Categorie, categ=categ)
    posts = Post.objects.filter(post_cate=cate)
    context = {'posts':posts, 'cates':categories, 'params':params}
    return render(request, 'home.html', context)

def search(request):
    if 'query' in request.GET:
        search_term = request.GET["query"]
        posts = Post.objects.filter(Q(title__icontains=search_term)|Q(content__icontains=search_term))
        if not posts:
            messages.info(request, "No results found")
        context = {'posts':posts, 'params':params, 'search_term':search_term, 'cates':categories}
        return render(request, 'home.html', context)