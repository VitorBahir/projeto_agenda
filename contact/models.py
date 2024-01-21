from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
# Create your models here.
class Category(models.Model):
    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'
    name = models.CharField(max_length=50)

    def __str__(self) -> str:
        return f'{self.name}'


class Contact(models.Model):
    first_name = models.CharField(max_length=50, verbose_name='Nome')
    last_name = models.CharField(max_length=50, verbose_name='Sobrenome')
    phone = models.CharField(max_length=50, verbose_name='Telefone')
    email = models.EmailField(max_length=254, blank=True, verbose_name='E-mail')
    description = models.TextField(blank=True, verbose_name='Descrição')
    created_date = models.DateTimeField(default=timezone.now, verbose_name='Data de criação')
    show = models.BooleanField(default=True, verbose_name='Mostrar') 
    pictures = models.ImageField(blank=True, upload_to='pictures/%Y/%m/', verbose_name='Fotos')
    category = models.ForeignKey(
        Category, 
        on_delete=models.SET_NULL,
        blank=True, null=True
        , verbose_name='Categoria')
    owner = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        blank=True, null=True,
        verbose_name='Usuário'
    )
    
    def __str__(self) -> str:
        return f'{self.first_name} {self.last_name}'