from django.contrib import admin
from .models import *

# Register your models here.

@admin.register(Card)
class CardAdmin(admin.ModelAdmin):

   list_display = ('title', 'user','brand', 'date_now','id')
   search_fields = ('',)
   

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):

   list_display = ('user', 'tel',  'id') 
   search_fields = ('',)


admin.site.register(Brand)
admin.site.register(Comment)
 