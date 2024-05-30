from django.db import models
from django.utils.text import slugify

class BlogPost(models.Model):
    title = models.CharField(max_length=200,verbose_name ='Заголовок'  ,blank=True )
    slug = models.CharField(max_length=200, unique=True)
    content = models.TextField(verbose_name ='Содержание')
    preview = models.ImageField(upload_to='previews/',verbose_name ='Изображение', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True,verbose_name ='Дата создания')
    is_published = models.BooleanField(default=False,verbose_name ='Признак публикации')
    views_count = models.PositiveIntegerField(default=0,verbose_name ='Количество просмотров')

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title
