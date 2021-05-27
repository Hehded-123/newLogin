from django.shortcuts import render, redirect
from django.contrib.auth.models import User

# Create your views here.

def register(request):

    if request.method == "POST":
        email = request.POST['email']
        name = request.POST['name']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if password1 !=password2:
            print('Pishiv nahoy')
        else:

            user = User.objects.create_user(email=email, username=name,  password=password1)
            user.save()

        return redirect('register')

    return render(request, 'reg_en.html')