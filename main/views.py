from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from .models import *


def index_view(request):
    context = {
        'banner': Banner.objects.last(),
        'info': Info.objects.last(),
        'contact': Contact.objects.last()

    }
    return render(request, "index.html", context)


def block_view(request):
    return render(request, "blog.html")


def portfolio_view(request):
    return render(request, "portfolio.html")


def single_view(request):
    return render(request, "single-page.html")


def my_profile_view(request):
    context = {
        'user': request.user
    }
    return render(request, 'myprofile.html', context)


def create_subject_view(request):
    if request.method == "POST":
        subject = request.POST["subject"]
        Massage.objects.create(
            subject=subject,
        )
    return redirect('index_url')


def signin_view(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        usr = authenticate(username=username, password=password)
        if usr is not None:
            login(request,usr)
            return redirect('index_url')
    return render(request, 'log-in.html')


def signup_view(request):
    if request.method =='POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        User.objects.create_user(username=username, password=password)
        return redirect('index_url')
    return render(request,'sign_up.html')


def logout_view(request):
    logout(request)
    return redirect('login_url')
