from django.shortcuts import render,redirect

from django.contrib.auth.hashers import make_password

from django.contrib import messages


from mainApp.tests import verifyInput


from mainApp.models import User,Post,Comment,Follower,Following


from django.contrib.auth import authenticate,login

from django.contrib import auth





# Create your views here.


def index(request):

    if request.method == 'POST':

        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request,username=username,password=password)

        if user is not None and user.is_active:

            auth.login(request,user)  

            return redirect('main')

        else:
            messages.info(request,'Invalid username or password')

            return redirect('index')
    
    else:
        
        return render(request,'index.html')


def registerUser(request):

    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']

        hash_password = make_password(password)  # this make password is a django function base password

        error = verifyInput(username,password)

        if len(error) != 0:

            error = error[0]

            print(error)

            return render(request,'registration.html',{'error':error})
        
        else :

            r = User(username = username,email=email,password = password)
            r.save()

            messages.success(request,'Account created successfully')

            return redirect('register')
    else:
        return  render(request,'registration.html')
    



def main(request):

    print(request.user)

    return render(request,'main.html')



def logout(request):
    
    return render(request,'logout.html')

            


