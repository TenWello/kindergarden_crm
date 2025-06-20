
import datetime
from django.utils import timezone
from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Sum
from service.models import Service
from payment.models import Payment
from .models import Report
from django.contrib import messages
from django.contrib.admin.views.decorators import staff_member_required

def report_list(request):
    reports = Report.objects.order_by('-reported_month')

    today = timezone.localdate()

    return render(request, 'report/report_list.html', {
        'reports': reports,
        'current_year':  today.year,
        'current_month': today.month,
    })
def generate_report(request, year, month):
    reported_month = datetime.date(year, month, 1)

    payments = Payment.objects.filter(
        created_at__year=year,
        created_at__month=month
    )
    total_expense = payments.aggregate(total=Sum('total_money'))['total'] or 0

    services = Service.objects.filter(
        served_at__year=year,
        served_at__month=month
    )
    product_went_out = sum(s.portion_count for s in services)

    total_product = Service.objects.aggregate(total=Sum('portion_count'))['total'] or 0
    left_product  = total_product - product_went_out

    money_left    = (payments.aggregate(total=Sum('total_money'))['total'] or 0) - total_expense
    total_benefit = money_left

    report = Report.objects.create(
        reported_month   = reported_month,
        total_expense    = total_expense,
        money_left       = money_left,
        total_product    = total_product,
        left_product     = left_product,
        product_went_out = product_went_out,
        total_benefit    = total_benefit,
    )
    report.payment.set(payments)
    report.save()

    return redirect('report:report_detail', report.pk)

def report_detail(request, pk):
    report   = get_object_or_404(Report, pk=pk)
    return render(request, 'report/report_detail.html', {'report': report})

@staff_member_required
def report_delete(request, pk):
    report = get_object_or_404(Report, pk=pk)
    if request.method == 'POST':
        report.delete()
        messages.success(request, "Hisobot o‘chirildi.")
        return redirect('report:report_list')
    return render(request, 'report/report_confirm_delete.html', {'report': report})
