from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Profile

class Profile_Serializers(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ['icon', 'bio', 'phone_number', 'birth']

    def create(self, validated_data):
        return Profile.objects.create(**validated_data)