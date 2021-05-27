from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages

# Create your views here.

def register(request):

    if request.method == "POST":
        email = request.POST['email']
        name = request.POST['name']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if password1 !=password2:
            messages.info(request, 'Keke')


        elif User.objects.filter(username=name).exists():
            messages.info(request, 'Bruh')


        elif User.objects.filter(email=email).exists():
            messages.info(request, 'Pishiv nahoy')



        else:

            user = User.objects.create_user(email=email, username=name,  password=password1)
            user.save()

        return redirect('register')

    return render(request, 'reg_en.html')