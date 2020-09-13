from django.shortcuts import render, redirect
from django.db import IntegrityError
from django.contrib.auth import authenticate, login, logout, get_user_model
from django.contrib.auth.models import auth,User
from django.contrib.auth.decorators import login_required


# Create your views here.
def home(request):
    return render(request,'home/index.html')

@login_required(login_url='/login/')
def donate(request):
    return render(request,'home/donate.html')
#def current(request):
    #return render(request,'home/current.html')

#APPLYING FORCE LOGIN
@login_required(login_url='/login/')
def apply(request):
    return render(request,'home/apply.html')

def user_logout(request):
      if request.method == 'POST':
         logout(request)
         return redirect('/')

def user_login(request):

    if request.method == 'POST':
        USERNAME = request.POST['username']
        PASSWORD = request.POST['password']
        x = authenticate(request,username=USERNAME, password=PASSWORD)

        if x is not None:

          login(request,x)
          return redirect('home')

        else:
            return render(request,'home/joinus.html',{'hi': 'invalid username or password'})
    else:
        return render(request,'home/joinus.html')
def user_signup(request):

        if request.method == 'GET':
          return render(request, 'home/signup.html')
        else:

            username = request.POST['username']
            email = request.POST['email']
            password = request.POST['password']
            #last_name = request.POST['re_type_password']
            # if password == last_name:
            try:
                    user = User.objects.create_user(username=username, email=email, password=password)
                    user.save()

                    return redirect('user_login')
            except IntegrityError:
                    return render(request,'home/signup.html',
                                  {'error': 'username has used previously please try with another one'})


    # else:
    #             return render(request, 'signup.html', {'name': 'You entered wrong password , please try again'})
