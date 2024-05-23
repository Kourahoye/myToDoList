from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from .forms import sign_upForm
from .models import Utilisateurs

# Create your views here.
def sign_up(request):
    if request.method == 'POST':
        form = sign_upForm(request.POST)
        if form.is_valid():
            up_form = form.save(commit=False)
            up_form.password = make_password(form.cleaned_data['password'])
            up_form.status = 1
            up_form.save()
            user = Utilisateurs.objects.get_by_natural_key(username=request.POST['username'])
            login(request, user)
            return redirect("liste")
    else:
        form = sign_upForm()
    return render(request, "accounts/sign_up.html", context={"sign_up_forms": form})

def login_user(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password= request.POST.get("password")
        user = authenticate(username=username,password=password)
        if user:
            login(request, user)
            return redirect("liste")
    return render(request, "accounts/login.html")


def logout_user(request):
    logout(request)
    return redirect("login_user")