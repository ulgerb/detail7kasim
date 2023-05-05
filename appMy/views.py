from django.shortcuts import render, redirect
from .models import *
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages

# Create your views here.


def index(request):
   cards = Card.objects.all()
   cardsC = Card.objects.all().order_by("?")[:5]
   brands = Brand.objects.all()
      
   context={
      "cards":cards,
      "cardsC": cardsC,
      "brands":brands,
   }
   return render(request, 'index.html',context)


def detailPage(request, id):
   card = Card.objects.get(id=id)
   comments = Comment.objects.filter(card=card)
   
   if request.method =="POST":
      name = request.POST.get("fname")
      text = request.POST.get("text")
      
      comment = Comment(fname = name, text=text, card=card )
      comment.save()
   
   context = { 
      "card":card,
      "comments": comments,
   }
   return render(request, 'detail.html', context)


def categoryPage(request, cate="all", group=4):
   brands = Brand.objects.all()

   if cate == "all":
      cards = Card.objects.all().order_by("-id")
   else:
      cards = Card.objects.filter(brand__title=cate)

   
   context = {
       "cards": cards,
       "brands": brands, 
       "category_actice": cate,
       "group":group,
   }
   return render(request, 'category.html', context)


def cardAdd(request):
   brands = Brand.objects.all() 
   context = {
       "brands": brands,
   }
   if request.method == "POST":
      title = request.POST.get("title")
      brand = request.POST.get("brand")
      text = request.POST.get("text")

      if not (title.strip(" ") == "" or text.strip(" ") == ""):
         print("GİRDİ")
         brandget = Brand.objects.filter(title=brand)

         if brandget.exists():

            brandget = brandget.get()
            
            card = Card(user=request.user,title=title, brand=brandget, text=text)
            card.save()
            return redirect("/card-add/")
         else:
            context.update({"hata": "Marka Kayıtlı Değil!!"})
            
      else:
         print("GİRMEDİ")
         context.update({"hata": "Başlık veya içerik boş bırakılmamalı!!"})
      
   return render(request, 'card-add.html', context)

def cardDelete(request, id):
   card = Card.objects.get(id=id)
   card.delete()
   
   return redirect("index")
   
def loginUser(request):
   
   if request.method == "POST":
      username = request.POST.get("username") # berkay
      password = request.POST.get("password")
      
      user = authenticate(username=username, password=password)
      useractive = User.objects.filter(username=username)
      if useractive.exists():
         if useractive.get().is_active == True:
            if user is not None:
               login(request, user)
               return redirect("index")
            else:
               messages.warning(request, 'Kullanıcı adı veya şifre yanlış!!')
               return redirect("loginUser")
         else:
            messages.warning(request, 'Emaili active et!!')
            return redirect("loginUser")

   context = {}
   return render(request, 'user/login.html',context)

def registerUser(request):
   context = {}
   
   if request.method == "POST":
      fname = request.POST.get("fname")
      lname = request.POST.get("lname")
      email = request.POST.get("email")
      username = request.POST.get("username")
      password1 = request.POST.get("password1")
      password2 = request.POST.get("password2")
      
      # PASWORD START
      upp = False
      numm = False
      for i in password1:
         print(i)
         if i == i.upper():
            upp = True
         if i.isdecimal():
            numm = True
            
      if not upp:
         messages.warning(request, "Şifrede bir büyük harf olmalı!!")
      if not numm:
         messages.warning(request, "Şifrede bir numara olmalı!!")
      if not len(password1)>=6:
         messages.warning(request, "Şifrede en az 6 karakter olmalı!!")
      # PASWORD END

      
      if fname.strip(" ") != "" and email.strip(" ") != "" and username.strip(" ") != "" and password1.strip(" ") != "":
         if password1 == password2 and upp and numm and len(password1)>=6:
            if not User.objects.filter(username=username).exists():
               if not User.objects.filter(email=email).exists():
                  user = User.objects.create_user(first_name = fname, last_name = lname, email=email, username=username, password=password2)
                  user.is_active = False
                  user.save()

                  profile = Profile(user=user, password=password1) 
                  profile.save()
                  
                  return redirect("loginUser")
               else:
                  messages.warning(request, "Bu email başkası tarafından zaten kullanılıyor!!")
            else:
               messages.warning(request, "Bu username başkası tarafından zaten kullanılıyor!!")
         else:
            messages.warning(request, "Şifreler aynı değil!!")
      else:
         messages.warning(request, 'Boş bırakılan yerler var!!')
      
      context.update({
          "fname": fname, 
          "lname": lname,
          "email": email,
          "username": username,
      })
         
   
   return render(request, 'user/register.html',context)

def logoutUser(request):
   if request.user.is_authenticated:
      logout(request)
   return redirect("index")


def profileUser(request):
   profile = Profile.objects.get(user = request.user)
   user = User.objects.get(username=request.user)
   
   
   if request.method == "POST":
      submit = request.POST.get("submit")

      if submit == "passwordChange":
         password = request.POST.get("password")
         password1 = request.POST.get("password1")
         password2 = request.POST.get("password2")

         if user.check_password(password): # eski şifre
            # PASWORD START
            upp = False
            numm = False
            for i in password1:
               print(i)
               if i == i.upper():
                  upp = True
               if i.isdecimal():
                  numm = True

            if not upp:
               messages.warning(request, "Şifrede bir büyük harf olmalı!!")
            if not numm:
               messages.warning(request, "Şifrede bir numara olmalı!!")
            if not len(password1) >= 6:
               messages.warning(request, "Şifrede en az 6 karakter olmalı!!")
            # PASWORD END
            if password1 == password2 and upp and numm and len(password1)>=6: # yeni şifreler
               user.set_password(password1)
               print(password1)
               user.save()
               # login(request, user)
               return redirect("loginUser")
            else:
               messages.warning(request, "Şifreler aynı değil!!")
         else:
            messages.warning(request, "Şifre Yanlış!!")
               
         
         
      elif submit == "profilChange":
         fullname = request.POST.get("fullname") # berkay ülger
         username = request.POST.get("username")
         job = request.POST.get("job")
         email = request.POST.get("email")
         address = request.POST.get("address")
         tel = request.POST.get("tel")
         image = request.FILES.get("image")

         profile.job = job
         profile.address = address
         profile.tel = tel
         profile.image = image
         profile.save()
         
         # NAME START
         listname = fullname.split(" ")
         fname = ""
         lname = ""
         if len(listname) != 1:
            lname = listname.pop()
         for i in listname:
            if i != "":
               fname += i + " "
               
         user.first_name = fname
         user.last_name = lname
         # NAME END
         
         if not User.objects.filter(username = username).exists():
            user.username = username
            
         if not User.objects.filter(email = email).exists():
            user.email = email
         user.save()
      
      return redirect("profileUser")
   
   context = {
       "profile": profile,
   }


   return render(request, "user/profile.html",context)