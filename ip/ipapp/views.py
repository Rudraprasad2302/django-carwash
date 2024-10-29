from django.shortcuts import render,redirect
from .models import *
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as auth_login , logout as auth_logout
# Create your views here.

def home(request):
    home = Home.objects.all()
    context = {'home':home}
    return render(request,'ipapp/index.html',context)

def about(request):
    home = Home.objects.all()
    context = {'home':home}
    return render(request,'ipapp/about.html',context)

def carwash(request):
    home = Home.objects.all()
    context = {'home':home}
    return render(request,'ipapp/carwash.html',context)

def bikewash(request):
    home = Home.objects.all()
    context = {'home':home}
    return render(request,'ipapp/bikewash.html',context)

def reviews(request):
    home = Home.objects.all()
    context = {'home':home}
    return render(request,'ipapp/reviews.html',context)

def contact(request):
    home = Home.objects.all()
    context = {'home':home}
    if request.method == "POST":
        yourname = request.POST['name']
        yourmail = request.POST['mail']
        yournumber = request.POST['number']
        selectgender = request.POST['gender']

        if len(yourname) > 4:
            contact = Contact(your_name=yourname,your_mail=yourmail,your_number=yournumber,select_gender=selectgender)
            contact.save()
            messages.success(request,'Successfully form submit')
            return redirect('contact')
        else:
            messages.error(request,'your name should be more than 4 chars')
            return redirect('contact')
    return render(request,'ipapp/contact.html',context)


def login(request):
	if request.user.is_authenticated:
		return  redirect('/')

	if request.method == 'POST':
		number = request.POST['number']
		password = request.POST['password']

		print(password)

		user = authenticate(request,username=number,password=password)
		print(user)
		if user is not None:
			auth_login(request,user)
			messages.success(request,"Successfully Login")
			return redirect('/')
		else:
			messages.error(request,"Something Went Wrong")
			return redirect('/login')
	return render(request,'auth/login.html')

def signup(request):
    if request.user.is_authenticated:
         return  redirect('/')
    if request.method == 'POST':
        fname = request.POST['fname']
        lname = request.POST['lname']
        number = request.POST['number']
        email = request.POST['email']
        password = request.POST['password']
        cpassword = request.POST['cpassword']

        number_check = User.objects.filter(username=number).exists()
        email_check = User.objects.filter(email=email).exists()
        
        if number_check == True:
            messages.error(request,"Your Number  Already Exists")
            return redirect('/signup')
        
        if email_check == True:
            messages.error(request,"Your Email Already Exists")
            return redirect('/signup')
        
        
        if len(number) != 10:
            messages.error(request,'Number Should Be 10 Digit')
            return redirect('/signup')
        
        elif password != cpassword:
            messages.error(request,"Password And Confirm Did'nt Match")
            return redirect('/signup')
        
        else:
            user = User.objects.create_user(username=number,email=email,password=cpassword)
            user.first_name = fname 
            user.last_name = lname 
            user.save()
            messages.success(request,"Your Account Successfully Created")
            return redirect('/login')


    return render (request,'auth/signup.html')

def logout(request):
	auth_logout(request)
	messages.success(request,"Logout Succesfully")
	return redirect('/')