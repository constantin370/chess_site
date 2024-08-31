from django.core.validators import FileExtensionValidator
from django.db import models


class Video(models.Model):
    """Модель списка видеофайлов."""
    title         = models.CharField(max_length=100, blank=True, null=True)
    description   = models.TextField(blank=True, null=True)
    video         = models.FileField(upload_to='video/', blank=True, null=True,
                                     validators=[FileExtensionValidator(allowed_extensions=['mp4'])])
    create_at     = models.DateTimeField(auto_now_add=True)
    is_published  = models.BooleanField(verbose_name='Опубликовать', default=True)

    def __str__(self) -> str:
        return self.title
    
    class Meta:
        """Для понятного отображения названий."""
        verbose_name = 'Видеофайлы'
        verbose_name_plural = 'Видеофаил'