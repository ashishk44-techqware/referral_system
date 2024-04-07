# serializers.py
from rest_framework import serializers
from .models import User, UserProfile, Referral

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'email']

class UserProfileSerializer(serializers.ModelSerializer):
    user=UserSerializer()
    class Meta:
        model = UserProfile
        fields = ['id', 'user', 'referral_code']

class UserDataSerializer(serializers.ModelSerializer):
    user=UserSerializer()
    class Meta:
        model = UserProfile
        fields = ['id', 'user',]

class ReferralSerializer(serializers.ModelSerializer):
    referred_user_email = serializers.SerializerMethodField()
    class Meta:
        model = Referral
        fields = ['referred_user','referred_user_email', 'timestamp']

    def get_referred_user_email(self, obj):
        referred_user_email = obj.referred_user.user.email
        

        return referred_user_email