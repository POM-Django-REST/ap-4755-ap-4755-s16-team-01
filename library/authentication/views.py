from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from authentication.models import CustomUser
from .forms import RegisterForm, LoginForm

def register_view(request):

    error = None

    if request.method == 'POST':

        form = RegisterForm(request.POST)

        if form.is_valid():

            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            role = form.cleaned_data['role']

            if CustomUser.objects.filter(email=email).exists():

                error = "Користувач з таким Email вже існує."

            else:

                user = CustomUser.objects.create_user(
                    email=email,
                    password=password,
                    first_name=first_name,
                    last_name=last_name,
                    role=int(role)
                )

                login(request, user)

                return redirect('dashboard')

    else:

        form = RegisterForm()

    return render(
        request,
        'authentication/register.html',
        {
            'form': form,
            'error': error
        }
    )


def login_view(request):

    error = None

    if request.method == 'POST':

        form = LoginForm(request.POST)

        if form.is_valid():

            email_input = form.cleaned_data['email']
            password_input = form.cleaned_data['password']

            user = authenticate(
                request,
                username=email_input,
                password=password_input
            )

            if user:

                login(request, user)

                return redirect('dashboard')

            error = "Невірний Email або пароль."

    else:

        form = LoginForm()

    return render(
        request,
        'authentication/login.html',
        {
            'form': form,
            'error': error
        }
    )


def logout_view(request):
    logout(request)
    return redirect('login')


@login_required(login_url='login')
def dashboard_view(request):

    return render(request, 'authentication/dashboard.html')
