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
        
        
        
        
class Menu(models.Model):
    name = models.CharField(max_length=250,verbose_name="название блюда")
    description = models.TextField(verbose_name='описание')
    price = models.CharField(max_length=250, verbose_name="цена")
    image = models.ImageField(upload_to = "base/", verbose_name = "Изображение")
    
    class Meta:
        verbose_name = 'меню'
        verbose_name_plural = 'меню'
        

class Contact(models.Model):
    title = models.CharField(max_length=255,verbose_name='Название')
    description = models.TextField(verbose_name='описание')
    phone = models.CharField(max_length=255,verbose_name='номер')
    adres = models.CharField(max_length=255,verbose_name='адрес')