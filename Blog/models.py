from django.db import models
from cloudinary.models import CloudinaryField
# Create your models here.
class blog(models.Model):
    blog_heading=models.CharField(max_length=200)
    # blog_image=models.ImageField(upload_to='Blog Img')
    blog_image = CloudinaryField('image')
    blog_desc=models.TextField(max_length=1000)
    pub_date=models.DateTimeField(auto_now_add=True)
    pub_name=models.CharField(max_length=40)

    class Meta:
        ordering=['-pub_date']

    def __str__(self):
        return self.blog_heading

class contact(models.Model):
    name=models.CharField(max_length=40)
    email=models.EmailField(max_length=40)
    comments=models.TextField(max_length=500)

    def __str__(self):
        return self.name
