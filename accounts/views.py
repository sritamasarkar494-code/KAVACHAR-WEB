from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect

from .forms import WorkerSignupForm


def signup_view(request):

    if request.method == "POST":

        form = WorkerSignupForm(request.POST)

        if form.is_valid():

            user = form.save()

            # Automatically log in the newly created worker
            login(request, user)

            # Temporary destination until the worker home/training
            # section is implemented.
            return redirect("dashboard")

    else:

        form = WorkerSignupForm()

    return render(
        request,
        "accounts/signup.html",
        {
            "form": form,
        },
    )


def login_view(request):

    if request.method == "POST":

        username = request.POST.get(
            "username",
            ""
        ).strip()

        password = request.POST.get(
            "password",
            ""
        )

        user = authenticate(
            request,
            username=username,
            password=password,
        )

        if user is not None:

            login(request, user)

            # Temporary destination until the worker home/training
            # section is implemented.
            return redirect("dashboard")

        return render(
            request,
            "accounts/login.html",
            {
                "error": "Invalid username or password.",
            },
        )

    return render(
        request,
        "accounts/login.html",
    )


def logout_view(request):

    logout(request)

    return redirect("worker-login")