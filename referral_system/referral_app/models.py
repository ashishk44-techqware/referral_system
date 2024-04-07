from django.db import models
from django.contrib.auth.models import User
import string
import random

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    referral_code = models.CharField(max_length=10, blank=True, null=True,unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    #to genrate the unique referal code for each user
    def generate_referral_code(self):
        user_id_str = str(self.user.id)
        random_chars = ''.join(random.choices(string.ascii_uppercase + string.digits, k=5))  # Generate 5 random characters
        return user_id_str + random_chars

    def save(self, *args, **kwargs):
        if not self.referral_code:
            self.referral_code = self.generate_referral_code()
        super().save(*args, **kwargs)

    def __str__(self):
        return str(self.user.email)+"with referral_code"+str(self.referral_code)

class Referral(models.Model):
    referred_user = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='referrals')
    referring_user = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='referred_by')
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.referred_user.user.email)+"referr by"+str(self.referring_user.user.email)
