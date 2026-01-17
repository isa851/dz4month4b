from django.db import models

# Create your models here.
class Base(models.Model):
    title = models.CharField(max_length=255,verbose_name='Название')
    description = models.TextField(verbose_name='описание')
    phone = models.CharField(max_length=255,verbose_name='номер')
    adres = models.CharField(max_length=255,verbose_name='адрес')
    logo = models.ImageField(upload_to = "base/", verbose_name = "Логотив")
    
    class Meta:
        verbose_name = 'Базовый'
        verbose_name_plural = 'Базовые'
        