from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from .models import User

ROLE_URLS = {
    1: 'admin_dashboard',         # Admin
    2: 'serve_meal',              # Oshpaz
    3: 'inventory_dashboard',     # Menejer
}
def login_view(request):
    error = None
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user:
            auth_login(request, user)
            url_name = ROLE_URLS.get(user.role, 'forbidden')
            return redirect(url_name)
        else:
            error = 'Invalid Login or Password'
    elif request.user.is_authenticated:
        url_name = ROLE_URLS.get(request.user.role, 'forbidden')
        return redirect(url_name)

    print('Authenticate result:', user)
    return render(request, 'login.html', {'error': error})

@login_required
def admin_dashboard(request):
    if request.user.role != 1:
        return redirect('forbidden')
    return render(request, 'dashboard/admin_dashboard.html')

@login_required
def serve_meal(request):
    # faqat oshpaz kiradi
    return render(request, 'dashboard/serve_meal.html')

@login_required
def inventory_dashboard(request):
    # faqat menejer kiradi
    return render(request, 'dashboard/inventory_dashboard.html')

def forbidden(request):
    return render(request, 'forbidden.html')
