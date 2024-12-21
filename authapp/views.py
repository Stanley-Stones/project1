from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Create your views here.



def register(request):

  if request.user.is_authenticated:
    return redirect('homepage')

  code1 = '00000'

  if request.method == "POST":
    username = request.POST.get('username')
    email = request.POST.get('email')
    password = request.POST.get('pass1')
    password2 = request.POST.get('pass2')
    code2 = request.POST.get('code')

    if password == password2:

      if code1 == code2:

        if User.objects.filter(email=email).exists():
          messages.info(request, 'Email Already Taken')
          return redirect('register')

        else:
          user = User.objects.create_user(username=username, email=email,password=password)
          user.save()

          user = auth.authenticate(username=username, password=password)

          if user is not None:
            auth.login(request, user)
            return redirect('account')

          else:
            messages.info(request, 'No Account Found!')
            return redirect('login')
        
    
      
      else:
        messages.info(request, 'Code Does Not Match!')
        return redirect('register')

    else:
      messages.info(request, 'Password Does Not Match!')
      return redirect('register')


  return render(request, 'register.html')


def login(request):
  if request.user.is_authenticated:
    return redirect('homepage')

  if request.method == "POST":
    username = request.POST.get('username')
    password = request.POST.get('password')

    user = auth.authenticate(username=username, password=password)

    if user is not None:
      auth.login(request, user)
      return redirect('homepage')

    else:
      messages.info(request, 'No Account Found!')
      return redirect('login')
  return render(request, 'login.html')


@login_required(login_url="login")
def logout(request):
  auth.logout(request)
  return redirect('homepage')