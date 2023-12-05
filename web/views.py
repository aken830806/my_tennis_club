from django.contrib.auth import authenticate
from django.http import HttpResponse
from django.shortcuts import redirect
from django.template import loader
from django.contrib import auth

from web.forms import LoginForm


def login(request):
    template = loader.get_template('login.html')
    message = ''
    if request.method == "POST":
        post_form = LoginForm(request.POST)
        if post_form.is_valid():
            username = post_form.cleaned_data['username']
            password = post_form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                auth.login(request, user)
                return redirect('main')
            message = 'Login failed.'
    else:
        post_form = LoginForm()
    context = {
        'post_form': post_form,
        'message': message,
    }
    return HttpResponse(template.render(context, request))


def logout(request):
    """登出"""
    auth.logout(request)
    return redirect('main')
