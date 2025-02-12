from django.db import models
from django.contrib.auth.models import AbstractUser 
from django.utils.text import slugify
from django.utils import timezone
# Create your models here.

class CustomUser(AbstractUser):
    bio = models.TextField(blank=True, null=True)
    job_title = models.CharField(max_length=225, blank=True, null=True)
    profile_picture = models.ImageField(upload_to="profile_img", blank=True, null=True)
    facebook = models.URLField(blank=True, null=True)
    youtube = models.URLField(blank=True, null=True)
    instagram  = models.URLField(blank=True, null=True)
    twitter = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.username
    
class Blog(models.Model):
    CATEGORY = [
        ("Frontend", "Frontend"),
                ("Backend", "Backend"),
                ("Fullstack", "Fullstack"),
                ("Web3", "Web3"),
                ("Design", "Design")
                
    ]
    title = models.CharField(max_length=225)
   
    slug = models.SlugField(max_length=225, unique=True, blank=True, null=True)
    category = models.CharField(max_length=225, choices=CATEGORY, null=True, blank=True)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    published_date = models.DateTimeField(blank=True, null=True)
    is_draft = models.BooleanField(default=True)
    author = models.ForeignKey(CustomUser, on_delete=models.SET_NULL, null=True, blank=True, related_name="blogs")
    featured_image = models.ImageField(upload_to="blog_img", blank=True, null=True)

    class Meta:
        ordering = ["-published_date"]

    def __str__(self):
        return self.title
    
    def save(self, *args, **kwargs):
        base_slug = slugify(self.title)
        slug = base_slug
        n = 1
        while Blog.objects.filter(slug=slug).exists():
            slug = base_slug + "-" + str(n)
            n += 1  
        self.slug = slug
        if not self.is_draft and self.published_date is None:
            self.published_date = self.published_date = timezone.now()
        super().save(*args, **kwargs)
        

    
        



        
