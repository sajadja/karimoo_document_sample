from django.urls import path

from expert.views import get_pic, update_location, get_expert_info

urlpatterns = [
    path('getpic/', get_pic, name='get_pic'),
    path('updatelocation/', update_location, name='update_location'),
    path('getexpertinfo/', get_expert_info, name='get_expert_info'),
]
