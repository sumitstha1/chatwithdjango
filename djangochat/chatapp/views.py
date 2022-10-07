from re import template
from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import SignUpForm


# Create your views here.
def home_page(request):
    template = 'chatapp/index.html'
    return render(request, template)

def signup(request):
    template = 'user/signup.html'
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('frontpage')
    else:
        form = SignUpForm()

    return render(request, template, {'form': form})
