from django.contrib import admin
from .models import Contact,Comment, Categorie, Post

admin.site.register(Categorie)
admin.site.register(Contact)
admin.site.register(Comment)
admin.site.register(Post)
