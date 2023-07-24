from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from accounts.forms import LoginView


# Create your views here.
def user_login(request):
    if request.method == "POST":
        form = LoginView(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect("home")

    else:
        form = LoginView()
    context = {"form": form}

    return render(request, "accounts/login.html", context)


def user_logout(request):
    logout(request)
    return redirect("login")
