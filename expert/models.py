# from django.core.validators import MaxLengthValidator, DecimalValidator
from django.db import models
from django.utils.translation import ugettext_lazy as _
from user.models import UserProfile
from django. views import View


class ExpertProfile(models.Model):
    user = models.OneToOneField(UserProfile, on_delete=models.CASCADE)
    is_active_expert = models.BooleanField(_('is active expert'), default=False)
    ready_to_serve = models.BooleanField(_('ready to serve'), default=False)
    ready_to_serve_expire_time = models.DateTimeField(_('ready to serve expire time'), auto_now=True)
    father_name = models.CharField(_('father name'), max_length=26, null=True)
    shaba_numer = models.CharField(_('shaba number'), max_length=24)
    phone_number = models.CharField(_('phone number'), max_length=11)
    WOMEN = 1
    DONE = 2
    EXEMPT = 3
    SUBJECT = 4
    MILITARY_SERVICE_CHOICES = [
        (WOMEN, 'WOMEN'),
        (DONE, 'DONE'),
        (EXEMPT, 'EXEMPT'),
        (SUBJECT, 'SUBJECT')
    ]
    military_service = models.IntegerField(
        _('military service'), choices=MILITARY_SERVICE_CHOICES, null=True, blank=True
    )
    SINGLE = 1
    MARRIED = 2
    MARRIED_CHOICES = [
        (SINGLE, 'SINGLE'),
        (MARRIED, 'MARRIED')
    ]
    married_status = models.IntegerField(_('married status'), choices=MARRIED_CHOICES)
    insuranceID = models.CharField(_('insuranceID'), max_length=32)
    score_expert = models.IntegerField(_('score expert'), default=0)
    total_profit = models.IntegerField(_('total profit'), default=0)
    expert_balance = models.IntegerField(_('expert balance'), default=0)
    free_expert_balance = models.IntegerField(_('free expert balance'), default=0)
    country = models.CharField(_('country'), max_length=32, default='iran')
    state = models.CharField(_('state'), max_length=12)
    city = models.CharField(_('city'), max_length=12)
    address = models.TextField(_('address'))
    count_complete_services = models.PositiveIntegerField(_('count complete services'), default=0)
    # skill = models.ManyToManyField(Services, related_name='skill', through='Skillship')
    latitude = models.DecimalField(
        _('latitude'), max_digits=19, decimal_places=16, default=0
    )
    longitude = models.DecimalField(
        _('longitude'), max_digits=19, decimal_places=16, default=0
    )

    def count_skills(self):
        # expert = ExpertProfile.objects.filter
        return self.objects.skill.count()

    def skill_list(self):
        return self.objects.skill.all()

    def __str__(self):
        return self.user.user.get_full_name()

    def withdraw(self, amount):
        if self.expert_balance < amount:
            return False
        else:
            self.expert_balance = self.expert_balance - amount
            return True
