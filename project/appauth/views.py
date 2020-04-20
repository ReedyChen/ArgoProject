from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.views import generic
from django.core import mail

from .models import *
from .forms import *
from forms.models import *

from django.utils import timezone
from django.template import RequestContext
from django.shortcuts import render_to_response
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ValidationError, ObjectDoesNotExist
from django.core.validators import validate_email


from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView


MASTER_KEY="this-is-argo-key-tea-b-a-a"

# Python encrpytion, waiting for more implementations
def encrypt_val(txt):
    return str(txt)

# Python decryption, waiting for more implementations
def decrypt_val(txt):
    return str(txt)

# Create a new user account using userForm
def signup(request):    
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.refresh_from_db()

            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password')
            user.set_password(user.password)

            user.save()
            user = authenticate(username=username, password=raw_password)
            login(request, user)

            user.is_active = False
            user.save()

            # send the verification email
            htmlstr =  "<p><a href='http://127.0.0.1:8000/auth/register/confirm/"+encrypt_val(user.id)+"'>Click This Link To Activate Your Account</a></p>"
            mail.send_mail("Confirmation","Please confirm your account registration.",'argoteamservice@gmail.com',[user.email],html_message=htmlstr)
            return render(request, 'register.html', {'registered': True, 'form': form})
    else:
        form = UserForm()
    return render(request, 'register.html', {'registered': False, 'form': form})
    
    
# Confirm user from activision					  
def confirm(request, key):
    context = RequestContext(request)
    user_id = decrypt_val(key)
    user = get_object_or_404(User, pk=user_id)
    user.is_active = True
    user.save()
    user.backend = 'django.contrib.auth.backends.ModelBackend'
    login(request, user)
    return render(request, 'activation.html', {})

# Login 
def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                # Redirect to the success page.
                return render(request, 'index.html', {'user': user})
            else:
                return render(request, 'login.html', {'message': "This account has not been activated, please first activate first"})
        # incorrect message has been entered
        else:
            return render(request, 'login.html', {'message': "Login Failed, please check the information entered"})
     
    return render(request, 'login.html', {})


# Change password
@login_required
def changePasswordView(request):
    context = RequestContext(request)
    return render(request,'changepassword.html', {})

# Logout
@login_required
def user_logout(request):
    logout(request)
    return render(request,'index.html', {})
    
def forgetPasswordView(request):
    context = RequestContext(request)
    return render(request,'forgetpassword.html', {})
    
def resetPage(request, key):
    context = RequestContext(request)
    return render(request,'resetpassword.html',{'key':key})
    
# the function to let the people find the forgotten password
def forgetPassword(request):
    email = request.POST['email']
    username = request.POST['username']
    # try to find the user by entered email and username
    try:
        user = User.objects.get(email=email, username=username)
        htmlstr = "<p><a href='http://127.0.0.1:8000/auth/resetpassword/"+encrypt_val(user.id) + "'>Click This Link To Reset Password</a></p>"
        mail.send_mail("Find back Password","Please click the following link to reset password.",'argoteamservice@gmail.com',[email],html_message=htmlstr)
        return render(request,'forgetpassword.html', {'message': "An verification email has been sent to your mail box, please wait shortly to receive them"})    
    except: # Return the warning if the user can not been found
        return render(request,'forgetpassword.html', {'message': "The user info has not been found"})

# the function to let the people reset the password, the password confirmation is done in js
def resetPassword(request, key):
    context = RequestContext(request)
    user_id = decrypt_val(key)
    user = get_object_or_404(User, pk=user_id)
    password1 = request.POST['newpassword']
    return render(request,'success.html', {})
    


'''
def createform(request):
    if request.method == 'POST':
        form = CreationForm(request.POST)
    else:
        form = CreationForm()

    return render(request, 'createform.html', {'form': form})
'''


def createform(request):
    if request.method == 'POST':
        form = FormCreationSet(request.POST)
    else:
        form = FormCreationSet()
    return render(request, 'createform.html', {'form': form})

# Form creation views
class createformview(CreateView):
    template_name = 'createform.html'
    model = Form
    form_class = FormCreationForm # the parent object's form

    # On successful form submission
    def get_success_url(self):
        return reverse('-created')

    # Validate forms
    def form_valid(self, form):
        ctx = self.get_context_data()
        inlines = ctx['inlines']
        if inlines.is_valid() and form.is_valid():
            self.object = form.save() # saves Father and Children
            if inlines.is_valid():
                # also save the field objects of the form
                inlines.instance = self.object
                inlines.save()

            return redirect('/') # redirect to the index page after successfully created
        else:
            return self.render_to_response(self.get_context_data(form=form))

    def form_invalid(self, form):
        return self.render_to_response(self.get_context_data(form=form))

    # We populate the context with the forms. Here I'm sending
    # the inline forms in `inlines`
    def get_context_data(self, **kwargs):
        ctx = super(createformview, self).get_context_data(**kwargs)
        if self.request.POST:
            ctx['form'] = FormCreationForm(self.request.POST)
            ctx['inlines'] = FormCreationSet(self.request.POST)

        else:
            ctx['form'] = FormCreationForm()
            ctx['inlines'] = FormCreationSet()
        # Tags that are used to create the header of the form
        ctx['inlines_tags'] = ('label', 'field_type', 'required', 'choices', 'placeholder_text','help_text')

        return ctx