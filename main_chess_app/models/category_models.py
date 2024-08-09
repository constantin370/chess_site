from django.db import models

from django.urls import reverse


class Category(models.Model):
    """Модель списка категорий."""
    name = models.CharField(verbose_name='Название категории', max_length=256, db_index=True)
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="URL")
    is_published = models.BooleanField(verbose_name='Опубликовать', default=True)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('news:news_single_category', kwargs={'cat_slug': self.slug})

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ['id']