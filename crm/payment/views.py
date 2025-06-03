# payment/views.py

from django.shortcuts import render, redirect, get_object_or_404
from .models import Payment
from .forms import PaymentForm

def payment_list(request):
    payments = Payment.objects.all().order_by('-created_at')
    return render(request, 'payment/payment_list.html', {'payments': payments})

def payment_detail(request, pk):
    payment = get_object_or_404(Payment, pk=pk)
    return render(request, 'payment/payment_detail.html', {'payment': payment})

def payment_create(request):
    if request.method == "POST":
        form = PaymentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('payment_list')
    else:
        form = PaymentForm()
    return render(request, 'payment/payment_form.html', {'form': form, 'type': 'create'})

def payment_update(request, pk):
    payment = get_object_or_404(Payment, pk=pk)
    if request.method == "POST":
        form = PaymentForm(request.POST, instance=payment)
        if form.is_valid():
            form.save()
            return redirect('payment_list')
    else:
        form = PaymentForm(instance=payment)
    return render(request, 'payment/payment_form.html', {'form': form, 'type': 'edit'})

def payment_delete(request, pk):
    payment = get_object_or_404(Payment, pk=pk)
    if request.method == "POST":
        payment.delete()
        return redirect('payment_list')
    return render(request, 'payment/payment_confirm_delete.html', {'payment': payment})

# Tez pul qo‘shish uchun alohida view:
def add_money(request, pk):
    payment = get_object_or_404(Payment, pk=pk)
    if request.method == "POST":
        amount = int(request.POST.get('amount', 0))
        payment.total_money += amount
        payment.save()
        return redirect('payment_detail', pk=payment.pk)
    return render(request, "payment/add_money.html", {"payment": payment})
