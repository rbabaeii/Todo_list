from django.conf import settings
from django.http import HttpRequest, HttpResponse
from django.shortcuts import redirect, render
from django.views import View
from django.contrib.auth.models import User
from django.contrib.auth import login , authenticate , logout
from random import choice
from uuid import uuid4
# Create your views here.
from django.core.mail import send_mail
from todolist.models import Data
class users(View):
    def get(self , request):
        return render(request , "users/index.html")

    def post(self , request):
        if "signup" in request.POST:
            if ("name" and "pass" and 'email' in request.POST):
                name = request.POST['name']
                password = request.POST['pass']
                email = request.POST['email']
                u = User.objects.create_user(
                    username = name,
                    password = password , 
                    email = email
                )
                u.save()
                return redirect('/')
            else:
                return HttpResponse("full the fields")
        elif 'signin' in request.POST:
            if( 'username' in request.POST and
                "pass" in request.POST 
            ):
                username = request.POST['username']
                password = request.POST['pass']
                

                u = authenticate(
                    request ,
                    username = username,
                    password = password,
                )
                if u:
                    login(request , u)
                    return redirect("/")
                else:
                    return HttpResponse("your name or password is wrong ")
            else:
                return HttpResponse("full the fields")

class logoutt(View):
    def get(self , request):
        logout(request)
        return redirect("/users/u")
class Forgotpassword(View):
    def get(self , request):
        return render(request , 'users/password.html')
    def post(slf , request):
            email = request.POST['email']
            username = request.POST['username']
            def generate_password():
                lst = []
                a = 'abcdefghijklmnopqrstuvwxyz1234567890@#$'
                for i in a:
                    lst.append(i)
                passwordlist = []
                for i in range(8):
                    passwordlist.append(choice(lst))
                password = ''
                for i in passwordlist:
                    password+= i
                return(password)
            new_password = generate_password()
            try:
                user = User.objects.get(username = username)
            except:
                return HttpResponse("username is not exist !! ")
            else:
                user.set_password(new_password)            
                user.save()
                print('well done')
                subject = 'Change password'
                massege = f"Hi {user.username} your new password is : [{new_password}] please after login in account change youre password"
                usermail = [email , ]
                print(user.password)
                emal_from = settings.EMAIL_HOST_USER 
                print('---')
                send_mail(subject , massege , emal_from , usermail , fail_silently = False,)
                print('====')
                return HttpResponse('new password sent')
            