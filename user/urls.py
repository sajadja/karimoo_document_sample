from django.urls import path

from user.views import send_sms_otp, send_verify, verify, login_api, signup, exist_user, get_user_info

urlpatterns = [
    path('sendsms/', send_sms_otp, name='send_sms_otp'),
    path('sendverify/', send_verify, name='send_verify'),
    path('verify/', verify, name='verify'),
    path('loginuser/', login_api, name='login_api'),
    path('signupuser/', signup, name='signup'),
    path('existuser/', exist_user, name='exist_user'),
    path('getuserinfo/', get_user_info, name='get_user_info'),
]
