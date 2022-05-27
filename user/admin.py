from django.contrib import admin
from django.contrib.admin import register

from user.models import UserProfile


@register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = [
        'user', 'sub_number', 'mobile', 'nationality_code', 'nationality', 'gender',
        'birth_date', 'profile_image', 'profile_thumbnail', 'score', 'friend_counts', 'count_receive_services',
        'otp_password', 'otp_time_created', 'otp_expire_time', 'is_active_customer', 'is_expert', 'wallet_balance'
    ]
