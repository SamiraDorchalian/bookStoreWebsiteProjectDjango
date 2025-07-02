from django.db import models
from django.urls import reverse
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _

class Book(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    title = models.CharField(max_length=200, verbose_name=_('Title'))
    author = models.CharField(max_length=200, verbose_name=_('Author'))
    description = models.TextField(verbose_name=_('Description'))
    price = models.DecimalField(max_digits=6, decimal_places=3, verbose_name=_('Price'))
    cover = models.ImageField(upload_to='covers/', blank=True, verbose_name=_('Cover'))

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("book_detail", args=[self.id])
    

class Comment(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='comments')
    text = models.TextField(verbose_name=_('Text'))
    is_active = models.BooleanField(default=True)
    recommend = models.BooleanField(default=True, verbose_name=_('Recomment'))

    datetime_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.text
