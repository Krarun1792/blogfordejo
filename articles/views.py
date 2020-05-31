from django.shortcuts import render
from .models import Article,Author
from django.http import HttpResponse

def blog_list(request):
    blogs = Article.objects.all().order_by('date')
    author      = Author.objects.all()
    context = {
        'barticles':blogs,
        'bauthor': author
    }
    return render(request,'articles/blog.html',context)

def blog_detail(request, slug):
    article = Article.objects.get(slug=slug)
    author      = Author.objects.all()

    context = {
        'article': article,
        'author': author
    }
    return render(request,'articles/single.html',context)
