# views.py
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate
from .models import User,UserProfile, Referral
from .serializers import UserProfileSerializer, ReferralSerializer
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

@api_view(['POST'])
def user_registration(request):

    name = request.data.get('name')
    email = request.data.get('email')
    password = request.data.get('password')
    
    if 'referral_code' in request.data:
        referral_code = request.data.get('referral_code')

        try:
            refered_by=UserProfile.objects.get(referral_code=referral_code)   
            
        except Exception as e:
            return Response({'message': 'Referral code not correct'}, status=status.HTTP_404_NOT_FOUND)
    else:
        refered_by=None
    
    try:
        user = User.objects.create_user(username=email, email=email, password=password)
        user.first_name = name
        user.save()

        user_profile = UserProfile.objects.create(user=user)
        user_profile.save()
        
        if refered_by:
            refered=Referral.objects.create(referred_user=user_profile,referring_user=refered_by)
            refered.save()
    except Exception as e:
        return Response({'message': 'somthing went wrong else user already exists'}, status=status.HTTP_400_BAD_REQUEST)
    

    return Response({'user_id': user_profile.id, 'message': 'User registered successfully'}, status=status.HTTP_201_CREATED)

@api_view(['POST'])
def login_user(request):
    email = request.data.get('email')
    password = request.data.get('password')
    print(password,"password")
    user = authenticate(username=email, password=password)
    print(user,"user")
    if user:
        refresh = RefreshToken.for_user(user)
        print(refresh,"refresh")
        return Response({
            'refresh': str(refresh),
            'access': str(refresh.access_token),
            'user_id': user.id,
            'message': 'Login successful.'
        }, status=status.HTTP_200_OK)
    return Response({'message': 'Invalid credentials.'}, status=status.HTTP_401_UNAUTHORIZED)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def user_details(request):
    try:
        user_profile = UserProfile.objects.get(user=request.user)
        
    except Exception as e:
        return Response({'message': 'Invalid credentials.'}, status=status.HTTP_401_UNAUTHORIZED)

    serializer = UserProfileSerializer(user_profile)
    result={
        "message":"user profile",
        "data":serializer.data
    }
    return Response(data=result,status=status.HTTP_200_OK)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def referrals(request):
    print(request,"request")
    try:
        user_profile = UserProfile.objects.get(user=request.user)
        referred_users=Referral.objects.filter(referring_user=user_profile)
    except Exception as e:
        return Response({'message': 'Invalid credentials.'}, status=status.HTTP_401_UNAUTHORIZED)

    paginator = Paginator(referred_users, 2)  # Update the number of items per page to 2

    page = request.query_params.get('page', 1)
    try:
        referrals_data_page = paginator.page(page)
    except PageNotAnInteger:
        referrals_data_page = paginator.page(1)
    except EmptyPage:
        referrals_data_page = paginator.page(paginator.num_pages)

    serializer = ReferralSerializer(referrals_data_page, many=True)
    result={
        "message":"referral user list",
        "data":serializer.data
    }
    return Response(data=result,status=status.HTTP_200_OK)