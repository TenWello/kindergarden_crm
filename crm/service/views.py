from django.shortcuts import render, redirect, get_object_or_404
from .models import Service
from .forms import ServiceForm
from django.contrib import messages
from django.utils import timezone
from datetime import timedelta
from meal.models import Meal

def service_list(request):
    services = Service.objects.select_related('meal','served_by').order_by('-served_at')
    meals    = Meal.objects.all()     # <<< buni qo‘shganingizga ishonch hosil qiling
    return render(request, 'service/service_list.html', {
        'services': services,
        'meals': meals,              # <<< meals konteksti
    })
def serve_meal(request):
    if request.method == 'POST':
        form = ServiceForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Taom muvaffaqiyatli yetkazildi!")
            return redirect('service:service_list')
        else:
            # validatsiya xatolari ham shu yerda ko‘rinadi
            messages.error(request, "Xatolik: " + "; ".join(
                [e for errs in form.errors.values() for e in errs]
            ))
    else:
        form = ServiceForm(initial={
            'meal': request.GET.get('meal')
        })
    return render(request, 'service/serve_meal.html', {'form': form})


def recent_services(request):
    date_from = timezone.now() - timedelta(days=10)
    recent = Service.objects.filter(served_at__gte=date_from).order_by('-served_at')
    return render(request, 'service/recent_services.html', {'recent': recent})
