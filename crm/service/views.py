from django.shortcuts import render, redirect, get_object_or_404
from .models import Service
from .forms import ServiceForm
from django.contrib import messages
from django.utils import timezone
from datetime import timedelta
from meal.models import Meal
from django.contrib.admin.views.decorators import staff_member_required

def service_list(request):
    services = Service.objects.select_related('meal','served_by').order_by('-served_at')
    meals    = Meal.objects.all()
    return render(request, 'service/service_list.html', {
        'services': services,
        'meals': meals,
    })
def serve_meal(request):
    meal_id = request.GET.get('meal')
    initial = {}
    if meal_id:
        meal = get_object_or_404(Meal, pk=meal_id)
        initial = {
            'meal': meal,
            'portion_count': meal.available_portions
        }

    if request.method == 'POST':
        form = ServiceForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Taom muvaffaqiyatli yetkazildi!")
            return redirect('service:service_list')
        else:
            messages.error(request, "Xatolik: " + "; ".join(
                e for errs in form.errors.values() for e in errs
            ))
    else:
        form = ServiceForm(initial=initial)

    return render(request, 'service/serve_meal.html', {
        'form': form,
        'meal': Meal.objects.filter(pk=meal_id).first()
    })


def recent_services(request):
    # so‘nggi 10 kun ichidagi Service yozuvlari
    since = timezone.now() - timedelta(days=10)
    recent = Service.objects.select_related('meal','served_by')\
                            .filter(served_at__gte=since)\
                            .order_by('-served_at')
    return render(request, 'service/recent_services.html', {
        'recent': recent
    })
def service_detail(request, pk):
    service = get_object_or_404(Service.objects.select_related('meal','served_by'), pk=pk)
    return render(request, 'service/service_detail.html', {
        'service': service
    })

@staff_member_required
def service_delete(request, pk):
    service = get_object_or_404(Service, pk=pk)
    if request.method == 'POST':
        service.delete()
        messages.success(request, "Service yozuvi o‘chirildi.")
        return redirect('service:service_list')
    return render(request, 'service/service_confirm_delete.html', {
        'service': service
    })