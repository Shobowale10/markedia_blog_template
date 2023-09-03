from django.urls import path
from markedia_blog import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name="index"),
    path('index', views.index, name="index"),
    path('contact', views.contact, name="contact"),
    path('details/<slug:slug>', views.details, name="details"),
    path('comment', views.comment, name="comment"),
    path('subscribe', views.subscribe, name="subscribe"),
    path('blog', views.blog, name="blog"),
    path('author/<slug:slug>', views.author, name="author"),
    path('category/<slug:slug>', views.category, name="category"),
    path('search', views.search, name="search"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
    document_root=settings.MEDIA_ROOT)