from django.shortcuts import render, redirect, get_object_or_404
from .models import Service
from .forms import ServiceForm
from django.contrib import messages
from django.utils import timezone
from datetime import timedelta

def service_list(request):
    services = Service.objects.select_related('meal', 'served_by').order_by('-served_at')
    return render(request, 'service/service_list.html', {'services': services})

def serve_meal(request):
    if request.method == 'POST':
        form = ServiceForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Taom muvaffaqiyatli yetkazildi!")
            return redirect('service_list')
    else:
        form = ServiceForm()
    return render(request, 'service/serve_meal.html', {'form': form})

def recent_services(request):
    date_from = timezone.now() - timedelta(days=10)
    recent = Service.objects.filter(served_at__gte=date_from).order_by('-served_at')
    return render(request, 'service/recent_services.html', {'recent': recent})
