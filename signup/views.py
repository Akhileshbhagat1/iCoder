# signup's view
from django.contrib.auth.models import User
from django.shortcuts import render, redirect


def signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']

        user = User.objects.create_user(username=username, email=email, password=password)
        user.save()
        print('user created successfully')
        return redirect('/')

    else:
        return render(request, 'signup/signup.html')


