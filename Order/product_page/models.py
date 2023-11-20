from django.db import models

# Create your models here.
class Perfum(models.Model):
    name = models.CharField(max_length=300, verbose_name="Ім'я")
    price = models.IntegerField(verbose_name='Ціна')
    image = models.ImageField(verbose_name="Зображення", blank=True, null=True)
    description = models.CharField(max_length = 1000, verbose_name="Опис", blank=True, null=True)
    
    
    class Meta:
        verbose_name = 'Парфум'
        verbose_name_plural = 'Парфуми'
        
    def __str__(self):
        return self.name
 
    