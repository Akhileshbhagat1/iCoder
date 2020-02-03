from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Contact
from django.contrib.auth.models import User
from django.contrib import messages
from blog.models import Post
from django.contrib.auth import authenticate, login, logout


def home(request):
    return render(request, 'home/home.html')


def contact(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        content = request.POST['content']
        if len(name) < 2 or len(email) < 3 or len(phone) < 10 or len(content) < 4:
            messages.error(request, 'please fill the form correctly ')
        else:
            contact = Contact(name=name, email=email, phone=phone, content=content)
            contact.save()
            messages.success(request, 'your message has been successfully sent')
    return render(request, 'home/contact.html')


def about(request):
    # messages.error(request, 'this is about ')
    return render(request, 'home/about.html')


def search(request):
    query = request.GET['query']
    if len(query) > 80:
        allPosts = Post.objects.none()
    else:
        allPostsTitle = Post.objects.filter(title__icontains=query)
        allPostsContent = Post.objects.filter(content__icontains=query)
        allPostsAuthor = Post.objects.filter(author__icontains=query)
        allPosts = allPostsTitle.union(allPostsContent, allPostsAuthor)

    if allPosts.count() == 0:
        messages.warning(request, 'Please fil the specific keyword ')
    params = {'allPosts': allPosts, 'query': query}
    return render(request, 'home/search.html', params)


def handleSignup(request):
    if request.method == 'POST':
        # get the post parameter
        username = request.POST['username']
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        email = request.POST['email']
        password1 = request.POST['password']
        password2 = request.POST['confirmpassword']

        # check for errorneous inputs
        if len(username) > 10:
            messages.error(request, 'user name must be under 10 characters ')
            return redirect('home')

        # username should be alphanumeric
        if not username.isalnum():
            messages.error(request, 'User name should only contain letters and numbers ')
            return redirect('home')

        # Password should match
        if password1 != password2:
            messages.error(request, 'confirm password is not similar with password')
            return redirect('home')

        # Create user
        myuser = User.objects.create_user(username, email, password1)
        myuser.firstname = firstname
        myuser.lastname = lastname
        myuser.save()
        messages.success(request, 'you are successfully signed up...')
        return redirect('home')

    else:
        return HttpResponse(' 404 - Not Found ')


def handlelogin(request):
    if request.method == 'POST':
        # get the post parameter
        loginusername = request.POST['login_username']
        loginpassword = request.POST['login_password']

        user = authenticate(username=loginusername, password=loginpassword)

        if user is not None:
            login(request, user)
            messages.success(request, 'you are successfully logged in..')
            return redirect('home')
        else:
            messages.error(request, 'Invalid  credential, Please try again..')
            return redirect('home')

    return HttpResponse('404 - Not Found ')


def handlelogout(request):
    if request.method == 'POST':
        logout(request)
        messages.success(request, 'you are successfully logged out..')
        return redirect('home')

#
# def handleprofile(request):
#     if request.method == 'POST':
#         username = request.POST['login_username']
#         return render(request, 'home/profile.html', {'username': username})
#         # username = request.POST['login_username']
#         # username = request.POST['login_username']
#         # username = request.POST['login_username']
#
#
#     return redirect('home/profile')








