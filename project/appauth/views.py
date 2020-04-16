import datetime
import time
import random
import uuid
import json
import numpy as np

from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.views import generic
from django.core import mail

from .models import *

from django.utils import timezone
from django.template import RequestContext
from django.shortcuts import render_to_response
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ValidationError, ObjectDoesNotExist
from django.core.validators import validate_email


from . import opra_crypto

from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect


    
# Sign up an account
def signup(request):
    context = RequestContext(request)
    
    registered = False
    
    # If it's a HTTP POST, we're interested in processing form data.
    if request.method == 'POST':
        userForm = UserForm(request.POST)
 
        # If the two forms are valid...
        if userForm.is_valid():
            if '@' in request.POST['username']:
                userForm = UserForm()
            else:
                # Save the user's form data to the database.
                user = userForm.save()
                
                # Hash the password with the set_password method
                user.set_password(user.password)
                user.is_active = False
                user.save()
                profile = UserProfile(user=user, time_creation=timezone.now())
                profile.save()
                # Update our variable to tell the template registration was successful.
                registered = True
                
                htmlstr =  "<p><a href='http://127.0.0.1:8000/auth/register/confirm/"+opra_crypto.encrypt(user.id)+"'>Click This Link To Activate Your Account</a></p>"
                mail.send_mail("Confirmation","Please confirm your account registration.",'argoteamservice@gmail.com',[user.email],html_message=htmlstr)
        else:
            return HttpResponse("This username already exists. Please try a different one. <a href='/auth/register'>Return to registration</a>")

    else:
        userForm = UserForm()

    return render(request, 'register.html', {'userForm': userForm, 'registered': registered})

# Confirm user from activision					  
def confirm(request, key):
    context = RequestContext(request)
    user_id = opra_crypto.decrypt(key)
    user = get_object_or_404(User, pk=user_id)
    user.is_active = True
    user.save()
    user.backend = 'django.contrib.auth.backends.ModelBackend'
    login(request,user)
    return render(request, 'activation.html', {'quick':False})


# Login 
def user_login(request):
    context = RequestContext(request)
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        
        # Check if the username/password combination is valid - a User object is returned if it is.
        user = authenticate(username=username, password=password)
        
        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
            else:
                email = user.email
                if email:
                    htmlstr = "Please <a href='http://127.0.0.1:8000/auth/register/confirm/"+opra_crypto.encrypt(user.id)+"'>CLICK HERE</a> to activate your account."
                    mail.send_mail("OPRA Confirmation From Invalid Login","Please confirm your account registration.",'argoteamservice@gmail.com',[email],html_message=htmlstr)
                return HttpResponse("Your account is not active. We have resent an activation link to your email address. Please check.")
        else:
            return HttpResponse("Invalid login details supplied.")
	
    else: 
        # Display the login form.
        return render(request,'login.html', {})



@login_required
def changePasswordView(request):
    context = RequestContext(request)
    return render(request,'changepassword.html', {})

@login_required
def user_logout(request):
    # Since we know the user is logged in, we can now just log them out.
    logout(request)
    return render(request,'index.html', {})
    
def forgetPasswordView(request):
    context = RequestContext(request)
    return render(request,'forgetpassword.html', {})
    
def resetPage(request, key):
    context = RequestContext(request)
    return render(request,'resetpassword.html',{'key':key})
    

def forgetPassword(request):
    email = request.POST['email']
    username = request.POST['username']
    if email == "" or username == "":
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    user = get_object_or_404(User, email=email, username=username)
    htmlstr = "<p><a href='http://127.0.0.1:8000/auth/resetpassword/"+opra_crypto.encrypt(user.id) + "'>Click This Link To Reset Password</a></p>"
    mail.send_mail("Find back Password","Please click the following link to reset password.",'argoteamservice@gmail.com',[email],html_message=htmlstr)
    return HttpResponse("An email has been sent to your email account. Please click on the link in that email and reset your password.")
    
def resetPassword(request, key):
    context = RequestContext(request)
    user_id = opra_crypto.decrypt(key)
    user = get_object_or_404(User, pk=user_id)
    new = request.POST['newpassword']
    con = request.POST['confirmpassword']
    if new != "" and new == con:
        user.set_password(new)
        user.save()
        return render(request,'success.html', {})
    else:
        return render(request,'resetpassword.html',{'key':key})

@login_required
def changePassword(request):
    user = request.user
    old = request.POST['oldpassword']
    new = request.POST['newpassword']
    if user.check_password(old):
        user.set_password(new)
        user.save()
        return HttpResponseRedirect(reverse('polls:index'))
    else:
        return HttpResponse("The password you entered is wrong.")
        
        


