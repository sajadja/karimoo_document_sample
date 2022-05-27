from datetime import datetime, timedelta
from django.contrib.auth import get_user_model
# from django.core.validators import MaxLengthValidator
from django.utils.translation import ugettext_lazy as _
from django_resized import ResizedImageField
from django.db import models

User = get_user_model()


class UserProfile(models.Model):
    user = models.OneToOneField(User, related_name='user_profile', unique=True, on_delete=models.CASCADE)
    sub_number = models.CharField(_('sub number'), max_length=5, default='+98')
    mobile = models.CharField(_('mobile'), max_length=11, unique=True)
    nationality_code = models.CharField(_('nationality code'), max_length=12, unique=True)
    IRAN = 1
    AFGHANISTAN = 2
    OTHER = 3
    NATIONALITY_CHOICE = [
        (IRAN, 'IRAN'),
        (AFGHANISTAN, 'AFGHANISTAN'),
        (OTHER, 'OTHER')
    ]
    nationality = models.IntegerField(_('nationality'), choices=NATIONALITY_CHOICE, default=IRAN)
    MALE = 1
    FEMALE = 2
    GENDER_CHOICE = [
        (MALE, 'MALE'),
        (FEMALE, 'FEMALE')
    ]
    gender = models.IntegerField(_('gender'), choices=GENDER_CHOICE, null=True, blank=True)
    birth_date = models.DateField(_('birth date'), null=True, blank=True)
    profile_image = models.ImageField(_('profile image'), upload_to='user/profile_image', null=True, blank=True)
    profile_thumbnail = ResizedImageField(
        upload_to='user/profile_thumbnail',
        size=[515, 478], crop=['middle', 'center'], quality=10, null=True, blank=True
    )
    score = models.IntegerField(_('score'), default=0)
    friend_counts = models.PositiveIntegerField(_('friend counts'), default=0)
    count_receive_services = models.PositiveIntegerField(_('count receive services'), default=0)
    # badge = models.ManyToManyField(through='GiftShip', related_name='gift', blank=True)
    # active_gifts = models.ManyToManyField(through='GiftShip', related_name='gift', blank=True)
    otp_password = models.CharField(_('otp password'), max_length=6, blank=True, null=True)
    otp_time_created = models.DateTimeField(_('otp created time'), auto_now_add=True)
    otp_expire_time = models.DateTimeField(_('otp expire time'), default=datetime.now() + timedelta(minutes=2))
    is_active_customer = models.BooleanField(_('is active customer'), default=True)
    is_expert = models.BooleanField(_('is expert'), default=False)
    wallet_balance = models.IntegerField(_('wallet balance'), default=0)

    def get_otp_time(self):
        return self.otp_time_created

    def __str__(self):
        return self.user.get_full_name()

    def balance_display(self):
        return self.wallet_balance

    def deposit(self, amount):
        self.wallet_balance = self.balance_display() + amount

    def spend(self, amount):
        if amount > self.balance_display():
            return 'not enough money: {}'.format(self.balance_display())
        else:
            self.wallet_balance = self.balance_display() - amount
            return 'success! left: {}'.format(self.balance_display())

    def get_info(self):
        info = {
            'first_name': self.user.first_name,
            'last_name': self.user.last_name,
            'gender': self.gender,
            'profile_image': self.profile_image.url(),
            'count_receive_services': self.count_receive_services,
            'friends_counts': self.friend_counts,
            # 'have_massages': true(if has unread message) or false
            'is_expert': self.is_expert,
        }
        return info
