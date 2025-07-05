from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import Profile_Serializers
from .models import Profile

# Create your views here.


class Register_View(APIView):
    def post(self, request):
        data = request.data
        print(data)
        password = data.get('password')
        confirm_password = data.get('confirm_password')

        if not password or not confirm_password: 
            data = {
                "error" : True,
                "msg" : "Password yoki Confirm_Password lardan 1 tasi kirtilmagan"
            }
            return Response(data=data, status=status.HTTP_400_BAD_REQUEST)
        
        if password != confirm_password:
            data = {
                "error" : True,
                "msg" : "Password va Confirm_Password 1 xil emas"
            }
            return Response(data=data, status=status.HTTP_400_BAD_REQUEST)
        
        username_check = Profile.objects.filter(username = data.get('username')).exists()
        username1 = Profile.objects.filter(username = data.get('username')).first()
        email_check = Profile.objects.filter(email = data.get('email')).exists()
        email1 = Profile.objects.filter(email = data.get('email')).first()

        if username_check:
            data = {
                "error" : True,
                "msg" : f"{username1.username} nomli username allaqachon bor"
            }
            return Response(data=data, status=status.HTTP_400_BAD_REQUEST)          
        print("username checked")
        if email_check:
            data = {
                "error" : True,
                "msg" : f"{email1} nomli email allaqachon bor"
            }
            return Response(data=data, status=status.HTTP_400_BAD_REQUEST)   
        print('email checked')
        serializer = Profile_Serializers(data=data)
        if serializer.is_valid():
            print('serislizer checked')
            user = serializer.save()
            user.set_password(password)
            user.save()
            # user.refresh_from_db()
            data = {
                "error" : True,
                "msg" : f"Foydalanuvchi muvaffaqiyatli yaratildi",
                "user" : {
                    "username" : user.username,
                    "email" : user.email,
                    "phone_number" : user.phone_number,
                    "birth" : user.birth,
                    "bio" : user.bio,
                }
            }
            return Response(data=data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class List_Profiles(APIView):
    def get(self, request):
        # data = data.request
        user = Profile.objects.all()
        serializer = Profile_Serializers(user, many=True)

        return Response(serializer.data)