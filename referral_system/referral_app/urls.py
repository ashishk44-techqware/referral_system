from django.urls import path
from .views import *
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('register',user_registration, name="register"),
    path('login',login_user, name="login_user"),
    path('user-profile',user_details, name="user_profile"),
    path('referred-users',referrals, name="reffered_user_list"),
    
    ] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)