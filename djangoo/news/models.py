from django.db import models


# Create your models here.
class Articles(models.Model):
    title = models.CharField('Название', max_length=50, default='Name title')
    anons = models.CharField('Анонс', max_length=250, default='Name title')
    full_text = models.TextField('Статья', )
    date = models.DateTimeField('Дата публикации')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'

# python manage.py makemigrations
# python manage.py migrate
