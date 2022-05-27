from django.contrib import admin
from django.contrib.admin import register

from expert.models import ExpertProfile


@register(ExpertProfile)
class ExpertAdmin(admin.ModelAdmin):
    list_display = [
        'user', 'is_active_expert', 'ready_to_serve', 'ready_to_serve_expire_time', 'father_name', 'shaba_numer',
        'phone_number', 'military_service', 'married_status', 'insuranceID', 'score_expert', 'total_profit',
        'expert_balance', 'free_expert_balance', 'country', 'state', 'city', 'address', 'count_complete_services',
        'latitude', 'longitude'
    ]
