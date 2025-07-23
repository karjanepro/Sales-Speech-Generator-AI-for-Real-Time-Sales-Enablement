from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .utils import generate_sales_speech

CATEGORIES = ['Cold Outreach', 'Product Demo', 'Follow-Up', 'Upsell', 'Client Retention']

def user_register(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        User.objects.create_user(username=username, password=password)
        return redirect('login')
    return render(request, 'core/register.html')

def user_login(request):
    if request.method == 'POST':
        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
        if user:
            login(request, user)
            return redirect('select_category')
    return render(request, 'core/login.html')

def user_logout(request):
    logout(request)
    return redirect('login')

@login_required
def select_category(request):
    return render(request, 'core/select_category.html', {'categories': CATEGORIES})

@login_required
def generate_prompt(request, category):
    if request.method == 'POST':
        product = request.POST['product']
        client_profile = request.POST['client_profile']
        script = generate_sales_speech(category, product, client_profile)
        return render(request, 'core/generated_script.html', {'script': script})
    return render(request, 'core/prompt_input.html', {'category': category})
