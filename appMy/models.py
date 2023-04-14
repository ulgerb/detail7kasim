from django.db import models

# Create your models here.

class Brand(models.Model):
   title = models.CharField(("Marka"), max_length=50)
   
   def __str__(self):
      return self.title
   
class Card(models.Model):
   brand = models.ForeignKey(Brand, verbose_name=("Marka"), on_delete=models.CASCADE, null=True)
   title = models.CharField(("Başlık"), max_length=50)
   text = models.TextField(("İçerik"))
   date_now = models.DateTimeField(("Tarih - Saat"), auto_now_add=True)
   image = models.ImageField(("Resim"), upload_to='cards', max_length=200)
   author = models.CharField(("Satıcı"), max_length=50)
   
   def __str__(self):
      return self.title
