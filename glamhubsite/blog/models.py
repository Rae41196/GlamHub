from django.db import models

from django.utils.text import slugify
from django.conf import settings
from django.db.models.signals import post_delete
from django.dispatch import receiver

# from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField

from account.models import Account


# method to define the upload location for images associated with blog posts
def upload_location(instance, filename, **kwargs):
    file_path = 'blog/{author_id}/{title}-{filename}'.format(
            author_id=str(instance.author.id),
            title=str(instance.title),
            filename=filename
        )
    return file_path


class BlogPost(models.Model):
    title = models.CharField(max_length=255, null=False, blank=False)
    body = RichTextUploadingField(max_length=50000, null=False, blank=False)
    image = models.ImageField(upload_to=upload_location, null=True, blank=True)
    date_published = models.DateTimeField(auto_now_add=True, verbose_name="date published")  # noqa
    date_updated = models.DateTimeField(auto_now=True, verbose_name="date updated")  # noqa
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)  # noqa
    slug = models.SlugField(max_length=255, blank=True, null=True, unique=True)

    # to return title when referenced
    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = slugify(self.author.username + "-" + self.title)
        super().save(*args, **kwargs)


# to delete images associated with a blog post that is deleted
@receiver(post_delete, sender=BlogPost)
def submission_delete(sender, instance, **kwargs):
    instance.image.delete(False)


class Comment(models.Model):
    post = models.ForeignKey('blog.BlogPost', on_delete=models.CASCADE, related_name='comments') # noqa
    participant = models.ForeignKey(
        Account, on_delete=models.CASCADE,
        blank=True, null=True)
    body = models.TextField(help_text='Your comment')
    created_on = models.DateTimeField(auto_now_add=True)
    approved_comment = models.BooleanField(default=False)

    class Meta:
        ordering = ['-created_on', 'participant']

    def approve(self):
        self.approved_comment = True
        self.save()

    def __str__(self):
        return 'Comment {} by {}'.format(self.body, self.participant_name)
