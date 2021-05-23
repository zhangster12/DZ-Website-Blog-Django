from django.db import models
from datetime import datetime
from django.template.defaultfilters import slugify

# Create your models here.
class BlogPost(models.Model):
    title = models.CharField(max_length = 100)
    slug = models.SlugField()
    thumbnail = models.ImageField(upload_to = 'photos/%Y/%m/%d/', blank=True)
    date_created = models.DateTimeField(default = datetime.now)
    content = models.TextField()
    featured = models.BooleanField(default = False)

    def save(self, *args, **kwargs):
        # Creates unique slug for each post.
        original_slug = slugify(self.title)
        queryset = BlogPost.objects.all().filter(slug__iexact = original_slug).count()

        count = 1
        slug = original_slug
        while(queryset):
            slug = original_slug + '-' + str(count)
            count += 1
            queryset = BlogPost.objects.all().filter(slug__iexact = slug).count()

        self.slug = slug

        if self.featured:
            try:
                temp = BlogPost.objects.get(featured = True)
                if self != temp:
                    temp.featured = False
                    temp.save()
            except BlogPost.DoesNotExist:
                pass

        super(BlogPost, self).save(*args, **kwargs)
    
    def __str__(self):
        return self.title