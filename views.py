from django.shortcuts import render
from .models import Post
from .models import Comments
from .models import Category
from .models import Author
from .models import Subscribe
from django.http import JsonResponse
from django.utils import timezone
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.db.models import Count



# DEFINING CONTEXTS DETAILS
posts = Post.objects.filter(status="published")
recentPosts = Post.objects.filter(status="published").order_by("-id")[:3]
sidebarPosts = Post.objects.filter(status="published").order_by("-id")[:5]
morePosts = Post.objects.filter(status="published").order_by("-id")[:2]
popularPosts = Post.objects.order_by("-views")[:3]
categoryList = Category.objects.annotate(nblog=Count('post')).values()



# VIEW FOR INDEX PAGE
def index(request, template='index.html'):
    paginator = Paginator(posts, 3)
    page = request.GET.get('page')

    try:
        post_list = paginator.page(page)
    except PageNotAnInteger:
        post_list = paginator.page(1)
    except EmptyPage:
        post_list = paginator.page(paginator.num_pages)

    context = {
        'posts' : posts,
        'sidebarPosts' : sidebarPosts,
        'morePosts' : morePosts,
        'popularPosts' : popularPosts,
        'categoryList' : categoryList,
        'post_list': post_list,
        'recentPosts' : recentPosts,
        'page' : page
    }
    
    return render(request, template, context)



# VIEW FOR CATEGORY PAGE
def category(request, slug, template='category.html',):
    category = Category.objects.get(slug = slug)
    category_posts = Post.objects.filter(category__in=[category])
    paginator = Paginator(category_posts, 3)
    page = request.GET.get('page')
    catName = slug
    catCount = len(category_posts)


    try:
        post_list = paginator.page(page)
    except PageNotAnInteger:
        post_list = paginator.page(1)
    except EmptyPage:
        post_list = paginator.page(paginator.num_pages)
        
    categoryList = Category.objects.annotate(nblog=Count('post')).values()
        
    context = {
        'sidebarPosts' : sidebarPosts,
        'morePosts' : morePosts,
        'popularPosts' : popularPosts,
        'recentPosts' : recentPosts,
        'page' : page,
        'categoryList' : categoryList,
        'catCount' : catCount,
        'post_list': post_list,
        'categoryName' : catName,
        'category_posts' : category_posts
    }
    
    return render(request, template, context)



# VIEW FOR POST DETAILS PAGE
def details(request, slug): 
    thisPost = Post.objects.filter(slug=slug).first()
    thisPost.update_views()
    id = thisPost.id
   
      
    author = thisPost.author
    category = thisPost.category
  
    postCategory = Category.objects.filter(name = category).first()
    authorDetail = Author.objects.filter(user = author).first()
    allComments = Comments.objects.filter(post_id = id).order_by("-date_created").values()
    commentCount = len(Comments.objects.filter(post_id = id))
    
    context = {
        'details' : thisPost,
        'postCategory' : postCategory,
        'allComments' : allComments,
        'count' : commentCount,
        'authorDetail' : authorDetail,
        'sidebarPosts' : sidebarPosts,
        'morePosts' : morePosts,
        'recentPosts' : recentPosts,
        'popularPosts' : popularPosts,
        'categoryList' : categoryList
    }
    return render(request,'details.html', context)
       


# VIEW FOR CONTACT PAGE
def contact(request, template='contact.html'):
        
    context = {
        'sidebarPosts' : sidebarPosts,
        'morePosts' : morePosts,
        'popularPosts' : popularPosts,
        'categoryList' : categoryList,
        'recentPosts' : recentPosts,
    }
    return render(request, template, context, )



# VIEW FOR AUTHOR PAGE
def author(request, slug, template='author.html'):
    authorDetail = Author.objects.filter(slug=slug).first()
    
    context = {
        'authorDetail' : authorDetail,
        'sidebarPosts' : sidebarPosts,
        'morePosts' : morePosts,
        'popularPosts' : popularPosts,
        'categoryList' : categoryList,
        'recentPosts' : recentPosts,
    }
    
    return render(request, template, context)    
    



# VIEW FOR BLOG PAGE
def blog(request, template='blog.html'):
    paginator = Paginator(posts, 3)
    page = request.GET.get('page')

    try:
        post_list = paginator.page(page)
    except PageNotAnInteger:
        post_list = paginator.page(1)
    except EmptyPage:
        post_list = paginator.page(paginator.num_pages)
        
    context = {
        'posts' : posts,
        'sidebarPosts' : sidebarPosts,
        'morePosts' : morePosts,
        'popularPosts' : popularPosts,
        'recentPosts' : recentPosts,
        'page' : page,
        'post_list' : post_list,
        'categoryList' : categoryList,
    }
    return render(request, template, context)
    
    

# VIEW FOR SEARCH PAGE
def search(request, template='search.html'):
    search_item = request.GET['search']
    searchPosts = Post.objects.filter(title__icontains = search_item)
    search_post_Count = len(searchPosts)
    
    paginator = Paginator(searchPosts, 3)
    page = request.GET.get('page')

    try:
        post_list = paginator.page(page)
    except PageNotAnInteger:
        post_list = paginator.page(1)
    except EmptyPage:
        post_list = paginator.page(paginator.num_pages)
        
    context = {
        'post_list': post_list,
        'search_item' : search_item,
        'sidebarPosts' : sidebarPosts,
        'morePosts' : morePosts,
        'postCount' : search_post_Count,
        'categoryList' : categoryList,
        'popularPosts' : popularPosts,
        'recentPosts' : recentPosts,
    }
    return render(request, template, context)



# VIEW FOR COMMENT PAGE
def comment(request):
    if request.POST.get('action') == 'comment':
        name = request.POST.get('name')
        post_id = request.POST.get('post_id')
        email = request.POST.get('email')
        website = request.POST.get('website') 
        comment = request.POST.get('comment') 
 
        commentDet = Comments.objects.create(
            name=name,
            post_id=post_id,
            email=email,
            website=website,
            comment=comment,
            date_created = timezone.localtime(timezone.now()),
        )
        
        allComments = {'name':commentDet.name,'email':commentDet.email,'website':commentDet.website,'comment':commentDet.comment, 'date_created': commentDet.date_created}

        context = {
            'allComments': allComments
        }
 
    return JsonResponse(context)


    
            
# VIEW FOR EMAIL SUBSCRIPTION
def subscribe(request):
    if request.POST.get('action') == 'subscribe':
        email = request.POST.get('email') 
        alreadySubcribed = Subscribe.objects.filter(email=email)
        
        if len(alreadySubcribed) > 0:
            subscribed = 1
        else:
            subscribed = 0

            Subscribe.objects.create(
                email=email,
            )
        
        context = {
            'subscribed' : subscribed
        }
        
    return JsonResponse(context)
