from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import UserLoginForm,UserCreationForm
from django.core.mail import send_mail
from django.conf import settings
from django.contrib import messages
# Create your views here.
def user_login(request):
    forms = UserLoginForm()
    if request.method == "POST":
        forms = UserLoginForm(request.POST)
        if forms.is_valid():
            username = forms.cleaned_data["username"]
            password = forms.cleaned_data["password"]

            user = authenticate(username=username, password=password)

            if user:
                login(request, user)
                return redirect("home")
            else:
                messages.error(request, "Invalid User or Password")
                return redirect("login")

    context = {
        "forms": forms
    }
    return render(request, "accounts/login.html", context)

def user_logout(request):
    logout(request)
    return redirect("login")

def register(request):
    if request.method == 'POST' :
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request,user)
            messages.success(request, f'Coucou {username}, Votre compte a été créé avec succès !')
            return render( request,'base/base.html' )
            
    else :
        form = UserCreationForm()
    return render(request,'accounts/register.html',{'form' : form})



from django.core.mail import send_mail

from django.http import HttpResponse

#-----------------------------------------------CONTACT--------------------------------------------------------------------------
#@user_passes_test(lambda u: u.is_superuser)
def mailing(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        subject=request.POST['subject']
        message = request.POST['message']

        message_body = f"Name: {name}\nEmail: {email}\nSubject: {subject}\nMessage: {message}"

        send_mail(
            'Contact Form Submission',
            message_body,
            settings.DEFAULT_FROM_EMAIL,
            ['werdijihen1919@gmail.com'],
            fail_silently=False,
        )
        return render(request, 'send mail/mailing.html', {'success': True})
    return render(request, 'send mail/mailing.html')


# def mailing(request):
#  if request.method == 'POST':
#     name  =  request.POST.get('name')
#     email  =  request.POST.get('email')
#     message =  request.POST.get('message')
#     send_mail(name ,
#      message,
#     'settings.EMAIL_HOST_USER', 
#      [email],
#      fail_silently=False)



    
#  return render(request, "send mail/mailing.html")