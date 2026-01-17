from django.db import models

# Create your models here.


class Settings(models.Model):
    title = models.CharField(max_length=255, verbose_name='Название')
    description = models.TextField(verbose_name='описание')
    phone = models.CharField(max_length=255, verbose_name='номер')
    adres = models.CharField(max_length=255, verbose_name='адрес')
    
    class Meta:
        verbose_name = 'данный'
        verbose_name_plural = 'данные'