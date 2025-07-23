from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth import authenticate as auth_authenticate 
from django.contrib.auth import  login as auth_login 
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout as log
from datetime import date as t,timedelta
import random
from django.http import JsonResponse
from django.utils import timezone
# Create your views here.




#--------------------------------------------------------------------------index---------------------------------------------------------------------------

def index(request):
    page = 'index'
    hear = ['hear1','hear2','hero3','hero3','hero3','hero3']
    return render(request,'index.html',{'page':page,'hear':hear})



def about(request):
    page = 'about'
    return render(request,'about.html',{'page':page})


def why_hire(request):
    page = 'admin_counselling'
    return render(request,'why_hire.html',{'page':page})

def admin_counselling(request):
    page = 'admin_counselling'
    return render(request,'admin_counselling.html',{'page':page})

from django.shortcuts import render
from django.http import Http404

def pagenotfount(request, exception=None):
    return render(request, 'pagenotfount.html', status=404)





# def login(request):
#     if request.method == 'POST':
#         username = request.POST.get('username')
#         password = request.POST.get('password')
#         user = auth_authenticate(request, username=username, password=password)
#         try:
#             data = MyCustomUser.objects.get(username = username)
#         except:
#             data=None
#         if user is not None:
#             if data.user_type == 'user':
#                 auth_login(request, user)
#                 return redirect('/user_dashboard')  
#             elif data.user_type == 'admin':
#                 auth_login(request, user)
#                 return redirect('/admin_dashboard')  
#         else:          
#             return render(request, 'login.html', {'error': 'Invalid username or password'})
#     return render(request,'login.html')

# def user_signup(request):
#     if request.method == 'POST':
#         username = request.POST.get('username')
#         phone_number = request.POST.get('number')
#         age = request.POST.get('age')
#         pincode = request.POST.get('pincode')
#         password1 = request.POST.get('password')
#         password2 = request.POST.get('c_password')
    
#         if MyCustomUser.objects.filter(username=username).exists():
#             error_message = 'Username is already taken. Please choose another one.'
#             messages.error(request, error_message)
#             return render(request, 'user_signup.html', {'error_message': error_message})
        
    
#         if not username or not password1 or not password2:
#             error_message = 'Please fill in all required fields.'
#             messages.error(request, error_message)
#             return render(request, 'user_signup.html', {'error_message': error_message})

#         if password1 != password2:
#             error_message = 'Passwords do not match.'
#             messages.error(request, error_message)
#             return render(request, 'user_signup.html', {'error_message': error_message})

#         MyCustomUser.objects.create_user(username=username,user_type = 'user',age = age,pincode = pincode, password=password1, phone_number=phone_number)
#         return redirect('/login')
#     return render(request,'user_signup.html')

# def admin_signup(request):
#     if request.method == 'POST':
#         username = request.POST.get('username')
#         phone_number = request.POST.get('number')
#         age = request.POST.get('age')
#         pincode = request.POST.get('pincode')
#         password1 = request.POST.get('password')
#         password2 = request.POST.get('c_password')
#         if MyCustomUser.objects.filter(user_type = 'admin').exists():
#             error_message = 'Admin is already created.'
#             messages.error(request, error_message)
#             return render(request, 'admin_signup.html', {'error_message': error_message})

#         if MyCustomUser.objects.filter(username=username).exists():
#             error_message = 'Username is already taken. Please choose another one.'
#             messages.error(request, error_message)
#             return render(request, 'admin_signup.html', {'error_message': error_message})
        
    
#         if not username or not password1 or not password2:
#             error_message = 'Please fill in all required fields.'
#             messages.error(request, error_message)
#             return render(request, 'admin_signup.html', {'error_message': error_message})

#         if password1 != password2:
#             error_message = 'Passwords do not match.'
#             messages.error(request, error_message)
#             return render(request, 'admin_signup.html', {'error_message': error_message})

#         MyCustomUser.objects.create_user(username=username,user_type = 'admin',age = age,pincode = pincode, password=password1, phone_number=phone_number)
#         return redirect('/login')
#     return render(request,'admin_signup.html')



# def logout(request):
#     log(request)
#     return redirect('/')  

