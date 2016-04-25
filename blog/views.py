
# Create your views here.
from django.shortcuts import render, RequestContext, get_object_or_404, get_list_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Post, Category
from django.http import HttpResponse
def all_posts(request):
    post_list = Post.objects.all()
    paginator = Paginator(post_list, 6)
    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        posts = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        posts = paginator.page(paginator.num_pages)
    data = {'posts': posts}
    
    
    return render(request, 'blog/all.html', data)

def add_post(request):
    titl = request.GET.get('title')
    auth = request.GET.get('author')
    cont = request.GET.get('content')
    categTitle = request.GET.get('category')
    
    thePost = Post(title=titl)   #You can add properties when constructing the object
    thePost.content = cont                  #Or after you've constructed it
    thePost.save()
    queryResult = Category.objects.filter(title=categTitle)     #A list of all Category objects whose titles are "categTitle"
    theCateg = queryResult[0]                   #Hopefully there's only one category with this name
    thePost.categories.add(theCateg)         #This is how you add items in a ManyToMany relationship 
    thePost.save()
    return HttpResponse("did it!")

def single_post(request, slug):
    post = get_object_or_404(Post, slug=slug)
    data = {'post': post}
    return render(request, 'blog/single.html', data)


def category_archive(request, slug):
    category = get_object_or_404(Category, slug=slug)
    categories = Category.objects.all()
    posts = Post.objects.filter(categories=category)
    data = {'cateogries': categories, 'posts': posts}
    return render(request, 'blog/category.html', data)
