from django.shortcuts import render, redirect
from .models import Emp_reg
import random
from django.core.mail import send_mail
from django.conf import settings
# Create your views here.
def index(request):
	return render(request,'index.html')


def signup(request):
	if request.method == "POST":
		name = request.POST['name']
		email = request.POST['email']
		mobileno = request.POST['mobileno']
		password = request.POST['password']
		cpassword = request.POST['cpassword']
		if password == cpassword:
			
			Emp_reg.objects.create( 
			 	name = name,email=email,mobileno=mobileno,password=password
			 )
		return render(request,'login.html',{'msg':msg})
	return render(request,'signup.html')

def login(request):
	if request.method == "POST":
		try:
			user=Emp_reg.objects.get(email=request.POST['email'])
			if user.password == request.POST['password']:
				request.session['email'] = user.email
				request.session['user'] = user.name
				
				return render(request,'index.html')
			else:
				msg = "the username and password you have entered is incorrect"
				return render(request,'login.html',{'msg':msg})	
		except:
			msg = "the email you have entered is incorrect"
			return render(request,'login.html',{'msg':msg})

def reset_password(request):
	if request.method == 'POST':
		try:
			user=Emp_reg.objects.get(email=request.session.get('email'))
			if user.password==request.POST['opassword']:
				if request.POST['npassword'] == request.POST['cpassword']:
					user.password = request.POST['npassword']
					user.save()
					return redirect('logout')
				else:
					msg = "Your password doesn't Match"
					return render(request,'reset_password.html',{'msg':msg})
			else:
					msg = "Reenter your old password "
					return render(request,'reset_password.html',{'msg':msg})		
		except Exception as e:
			print("Might be some issue",e)
			msg = "Reenter your old password "
			return render(request,'reset_password.html',{'msg':msg})
	return render(request,'reset_password.html')

def contact(request):
	return render(request,'contact.html')

def logout(request):
	try:
		del request.session['email']
		del request.session['user']
		msg = "Thank You!"
		return render(request,'login.html',{'msg':msg})
	except Exception as e:
		print("Might be some issue",e)
		return render(request,'login.html')

def forgot_password(request):
	otp=random.randint(1000,9999)
	
	if request.method == 'POST':
		email=request.POST['otpemail']
		request.session['Email_OTP'] = email
		
		try:
			subject = 'welcome to GFG world'
			message = f'Hi, thank you for registering in AB dev. here is your OTP : {otp} on your email {email}'
			email_from = settings.EMAIL_HOST_USER
			recipient_list = [email]
			send_mail( subject, message, email_from, recipient_list)
			msg = "Mail sent Successfully !!"
			return render(request,'otp_verification.html',{'msg':msg})
		except Exception as e:
			print("Might be some issue",e)
			
	return render(request,'forgot_password.html')


def otp_verification(request):
	if str(request.session['OTP'])==request.POST['otp']:
		msg = "OTP Successfully verified "
		return render(request,'new_password.html',{'msg':msg})
	else:
		return render(request,'otp_verification.html')
		
def new_password(request):
	if request.method == "POST":
		n_pwd=request.POST['password']
		c_pwd=request.POST['cpassword']
		email=request.session['Email_OTP']
		
		try:
			email_user=Emp_reg.objects.get(email=email)
			
		except Exception as e:
			print("Might be some issue",e)
		if n_pwd == c_pwd:
			email_user.password = n_pwd
			email_user.save()
			return redirect('logout')
		else:
			msg="Password is Not matched ||"
			return render(request,'new_password.html',{'msg':msg})
	else:
		return render(request,'new_password.html')
