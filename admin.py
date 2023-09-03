from django.contrib import admin
from .models import Post
from .models import Comments
from .models import Category
from .models import Author
from .models import Subscribe

# Register your models here.
@admin.register(Post)
class showPost(admin.ModelAdmin):
    list_display = ("title", "status", "date", "views", "author",)
    prepopulated_fields = {"slug": ("title",)}
    class Media:
	    js = ('tinyInject.js',)
    
class showComments(admin.ModelAdmin):
    list_display = ("name", "email", "website",)

    
class showCategories(admin.ModelAdmin):
    list_display = ("name",)
    prepopulated_fields = {"slug": ("name",)}
    
        
class showAuthor(admin.ModelAdmin):
    list_display = ("user", "slug",)
    prepopulated_fields = {"slug": ("user",)}


class showSubscribers(admin.ModelAdmin):
    list_display = ("email",)
    
    
admin.site.register(Author, showAuthor)
admin.site.register(Comments, showComments)
admin.site.register(Category, showCategories)
admin.site.register(Subscribe, showSubscribers)