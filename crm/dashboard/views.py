import json
from datetime import timedelta
from django.shortcuts import render
from django.utils import timezone
from django.db.models import Sum
from django.db.models.functions import TruncDate
from service.models import Service


def dashboard(request):
    days = 7
    today = timezone.localdate()
    start_date = today - timedelta(days=days - 1)

    qs = Service.objects.filter(served_at__date__gte=start_date)
    daily = (
        qs
        .annotate(day=TruncDate('served_at'))
        .values('day')
        .annotate(count=Sum('portion_count'))
        .order_by('day')
    )

    labels = [row['day'].strftime('%Y-%m-%d') for row in daily]
    data = [row['count'] for row in daily]

    print('labels:', labels)
    print('data:', data)

    context = {
        'labels': json.dumps(labels),
        'data': json.dumps(data),
    }
    return render(request, 'dashboard/admin_dashboard.html', context)
