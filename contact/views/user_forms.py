from django.shortcuts import render, redirect
from contact.forms import RegisterForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from django.contrib import auth

def register(request):

    form = RegisterForm()
   
    if request.method == 'POST':
        
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Usuário registrado')
            return redirect('contact:login')

    context = {
        'form': form
    }

    return render(
        request,
        'contact/register.html',
        context,
    )

def login_view(request):

    form = AuthenticationForm(request)

    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)

        if form.is_valid():
            user = form.get_user()
            messages.success(request, 'Logado com sucesso')

            auth.login(request, user)

            return redirect('contact:index')

    context = {
        'form': form,
    }

    return render(
        request,
        'contact/login.html',
        context,
    )

def logout_view(request):

    auth.logout(request)

    return redirect('contact:login')