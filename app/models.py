from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from autoslug import AutoSlugField
from ckeditor.fields import RichTextField

# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    time = models.DateTimeField(auto_now_add=True)
    tags = models.CharField(max_length=100)
    content = RichTextField()
    slug = AutoSlugField(populate_from='title', editable=True, always_update=True)
    image = models.ImageField(upload_to='images/', null=True, blank=True)
    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog', kwargs={'slug': self.slug})
