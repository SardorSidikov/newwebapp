from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import RegUser
from django.contrib.auth.decorators import login_required

@login_required
def reg(request):
    if request.method == "POST":
        form = RegUser(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f"Пользователь {username} успешно зарегистрирован")
            return redirect ('reg')
    else:
        form = RegUser()
    return render (request, 'webapp/reg.html', {'form': form})

@login_required
def home(request):
    return render (request, 'webapp/index.html')