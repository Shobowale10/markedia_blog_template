from django.db import models
from django.utils import timezone
from django.contrib.auth import get_user_model
User = get_user_model()
from ckeditor_uploader.fields import RichTextUploadingField



class Subscribe(models.Model):
    email = models.EmailField()
    


class Comments(models.Model):
    name = models.CharField('Name', max_length=120)
    post_id = models.IntegerField(null=True)
    email = models.EmailField()
    website = models.URLField(max_length=200)
    comment = models.TextField(blank=True)
    date_created = models.DateTimeField(blank=True,null=True)
    
    
    def publish(self):
        self.date_created=timezone.localtime(timezone.now())
        self.save()
        
        
        
class Category(models.Model):
    name = models.CharField('Name', max_length=120)
    slug = models.SlugField(default="", null=False)
    
    def __str__(self):
        return self.name
    
    
    
class Author(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    about = RichTextUploadingField()
    image = models.ImageField(upload_to='images/', null=True)
    slug = models.SlugField(default="", null=False)
    views = models.IntegerField(default=0)
    

    def __str__(self):
        return self.user.username
    
    def image_url(self):
        if self.image and hasattr(self.image, 'url'):
            return self.image.url
    


STATUS_CHOICES = (
   ('draft', 'Draft'),
   ('published', 'Published'),
)

class Post(models.Model):
    title = models.CharField('Post Title', max_length=120)
    date = models.DateTimeField()
    status = models.CharField(max_length = 10, choices = STATUS_CHOICES, default ='draft')
    category = models.ForeignKey(Category,on_delete = models.SET_NULL, blank = True, null = True,)
    author = models.ForeignKey(User,on_delete = models.SET_NULL, blank = True, null = True,)
    details = RichTextUploadingField()
    slug = models.SlugField(default="", null=False)
    image = models.ImageField(upload_to='images/', null=True)
    views = models.IntegerField(default=0)
    
    class Meta: 
        ordering = ['-date']
        
    def __str__(self):
        return self.title

    def image_url(self):
        if self.image and hasattr(self.image, 'url'):
            return self.image.url
        
    def update_views(self, *args, **kwargs):
         self.views = self.views + 1
         super(Post, self).save(*args, **kwargs)