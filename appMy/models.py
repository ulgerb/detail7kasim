from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Profile(models.Model):
   user = models.ForeignKey(User, verbose_name=("Kullanıcı Adı"), on_delete=models.CASCADE)
   address = models.CharField(("Adres"), max_length=50, blank=True, default="-")
   tel = models.CharField(("Telefon numarası"), max_length=10, blank=True, default="-")
   job = models.CharField(("Meslek"), max_length=50, blank=True, default="-")
   image = models.ImageField(("Profil Resmi"), upload_to='profile', max_length=255, blank=True, null=True)
   password = models.CharField(("Şifre"), max_length=50)

   def __str__(self):
      return self.user.username
class Brand(models.Model):
   title = models.CharField(("Marka"), max_length=50)
   
   def __str__(self):
      return self.title
   
class Card(models.Model):
   user = models.ForeignKey(User, verbose_name=("Kullanıcı - Satıtcı"), on_delete=models.SET_NULL, null=True)
   brand = models.ForeignKey(Brand, verbose_name=("Marka"), on_delete=models.SET_NULL, null=True)
   title = models.CharField(("Başlık"), max_length=50)
   text = models.TextField(("İçerik"))
   date_now = models.DateTimeField(("Tarih - Saat"), auto_now_add=True)
   image = models.ImageField(("Resim"), upload_to='cards', max_length=200, default="cards/vivo.jfif")
   active = models.BooleanField(("Göster"), default=False)
   price = models.FloatField(("Fiyat"), default=0)
   
   
   def __str__(self):
      return self.title

   

class Comment(models.Model):
   card = models.ForeignKey(Card, verbose_name=("Ürün"), on_delete=models.CASCADE, null=True)
   fname = models.CharField(("İsim"), max_length=50)
   text = models.TextField(("Yorum"))
   date_now = models.DateTimeField(("Tarih - Saat"), auto_now_add=True)
   
   def __str__(self):
      return self.fname
