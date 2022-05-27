
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseBadRequest, JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from expert.models import ExpertProfile
from user.models import UserProfile

User = get_user_model()


@csrf_exempt
def get_pic(request):
    if request.method == 'GET':
        return HttpResponse('method wrong')
    elif request.method == 'POST':
        mobile = request.POST['phone_number']
        user = UserProfile.objects.filter(mobile=mobile)
        if user:
            user.profile_image = request.POST['profile_image']
            return HttpResponse('got picture successfully')
        else:
            return HttpResponseBadRequest('user matching query not exist')


@login_required
@csrf_exempt
def update_location(request):
    if request.method == 'GET':
        return HttpResponse('method wrong')
    elif request.method == 'POST':
        mobile = request.POST['phone_number']
        user = UserProfile.objects.filter(mobile=mobile)
        expert = ExpertProfile.objects.filter(user=user)
        if expert:
            expert.country = request.POST['profile_image']
            return HttpResponse('got picture successfully')
        else:
            return HttpResponseBadRequest('user matching query not exist')


@login_required
@csrf_exempt
def get_expert_info(request):
    if request.method == 'GET':
        return HttpResponse('method wrong')
    elif request.method == 'POST':
        mobile = request.POST['mobile']
        user = UserProfile.objects.filter(mobile=mobile)
        expert = ExpertProfile.objects.filter(user=user)
        if expert:
            count_complete_services = str(expert.count_complete_services)
            total_profit = str(expert.total_profit)
            score = str(expert.score)
            balance = str(expert.expert_balance)
            free_balance = str(expert.free_balance)
            shaba = str(expert.shaba)
            count_skills = str(expert.count_skills())
            # age =
            return JsonResponse({
                'count_complete_services': count_complete_services,
                'total_profit': total_profit,
                'score': score,
                'balance': balance,
                'free_balance': free_balance,
                'shaba': shaba,
                'count_skills': count_skills
            })
        else:
            return HttpResponseBadRequest('user matching query not exist')

