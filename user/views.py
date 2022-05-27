from json import JSONEncoder
from datetime import datetime
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseBadRequest, JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from user.models import UserProfile

User = get_user_model()


@csrf_exempt
def send_sms_otp(request):
    if request.method == 'GET':
        return HttpResponse('method wrong')
    elif request.method == 'POST':
        phone_number = request.POST['phone_number']
        user = UserProfile.objects.filter(mobile=phone_number)
        if user:
            # send sms with kavenegar api and save to database
            return JsonResponse({'status': True}, encoder=JSONEncoder)
        else:
            return HttpResponseBadRequest('userProfile matching query not exist')


@csrf_exempt
def send_verify(request):
    if request.method == 'GET':
        return HttpResponse('method wrong')
    elif request.method == 'POST':
        phone_number = request.POST['phone_number']
        # send sms verify
        return JsonResponse({'status': True}, encoder=JSONEncoder)


@csrf_exempt
def verify(request):
    check_otp = False
    if request.method == 'GET':
        return HttpResponse('method wrong')
    elif request.method == 'POST':
        otp_code = request.POST['otp_code']
        # edit check otp
        if check_otp:
            return JsonResponse({'status': True}, encoder=JSONEncoder)
        else:
            return JsonResponse({'status': False}, encoder=JSONEncoder)


@csrf_exempt
def login_api(request):
    if request.method == 'GET':
        return HttpResponse('method wrong')
    elif request.method == 'POST':
        otp = request.POST['otp_code']
        phone_number = request.POST['phone_number']
        user = UserProfile.objects.filter(mobile=phone_number)
        if user:
            if datetime.now() > user.otp_expire_time:
                return HttpResponse('OTP code is expired')
            elif otp == user.otp_password:
                return JsonResponse({
                    'loggedin': True,
                    'mobile': user.mobile,
                })
            else:
                return HttpResponse('OTP code is wrong')

        else:
            return HttpResponseBadRequest('user matching query not exist')


@csrf_exempt
def signup(request):
    if request.method == 'GET':
        return HttpResponse('method wrong')
    elif request.method == 'POST':
        username = request.POST['username']
        user = User.objects.filter(username=username)
        if user:
            mobile = request.POST['phone_number']
            sub_number = request.POST['sub_number']
            nationality_code = request.POST['nationality_code']
            nationality = request.POST['nationality']
            gender = request.POST['gender']
            birth_date = request.POST['birth_date']
            profile_image = request.POST['profile_image']
            profile_thumbnail = request.POST['profile_thumbnail']
            is_active_customer = request.POST['is_active_customer']
            try:
                user_profile = UserProfile.objects.create(
                    mobile=mobile, sub_number=sub_number, nationality_code=nationality_code, nationality=nationality,
                    gender=gender, birth_date=birth_date, profile_image=profile_image,
                    profile_thumbnail=profile_thumbnail, is_active_customer=is_active_customer
                )
            except Exception as e:
                return HttpResponse(e)
        else:
            return HttpResponseBadRequest('user matching query not exist')


@csrf_exempt
def exist_user(request):
    if request.method == 'GET':
        return HttpResponse('method wrong')
    elif request.method == 'POST':
        mobile = request.POST['phone_number']
        user = UserProfile.objects.filter(mobile=mobile)
        if user:
            return JsonResponse({'exist': True})
        else:
            return JsonResponse({'exist': False})


@login_required
@csrf_exempt
def get_user_info(request):
    if request.method == 'GET':
        return HttpResponse('method wrong')
    elif request.method == 'POST':
        mobile = request.POST['mobile']
        user = UserProfile.objects.filter(mobile=mobile)
        if user:
            firstname = user.user.firstname
            lastname = user.user.lastname
            gender = user.gender
            profile_image = user.profile_image
            count_receive_services = user.count_receive_services
            friend_counts = user.friend_counts
            # have_massage = user.have_massage
            is_expert = user.is_expert
            return JsonResponse({
                'first_name': firstname,
                'last_name': lastname,
                'gender': gender,
                'profile_image': profile_image,
                'count_receive_services': count_receive_services,
                'friend_counts': friend_counts,
                'is_expert': is_expert
            })
        else:
            return HttpResponseBadRequest('user matching query not exist')
