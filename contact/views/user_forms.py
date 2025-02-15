from django.shortcuts import render, redirect
from contact.forms import RegisterForm, RegisterUpdateForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
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

@login_required(login_url='contact:login')
def logout_view(request):

    auth.logout(request)

    return redirect('contact:login')


@login_required(login_url='contact:login')
def user_update(request):
    
    form = RegisterUpdateForm(instance=request.user)
    
    context = {
        'form': form,
    }

    if request.method != 'POST':

        return render(
            request,
            'contact/user_update.html',
            context,
        )
    
    form = RegisterUpdateForm(data=request.POST, instance=request.user)
    context = {
        'form': form,
    }
    
    if not form.is_valid():
        return render(
            request,
            'contact/user_update.html',
            context,
        )
    

    form.save()
    messages.success(request, 'User updated')
    return redirect('contact:user_update')