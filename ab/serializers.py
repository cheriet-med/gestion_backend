from djoser.serializers import UserCreateSerializer
from rest_framework import serializers
from . models import *

from django.contrib.auth import get_user_model

User = get_user_model()

class UserCreateSerializer(UserCreateSerializer):
    class Meta(UserCreateSerializer.Meta):
        model = User
        fields = '__all__'


class UserUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserAccount
        fields = '__all__'



class UpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserAccount
        fields = '__all__'





class PersonelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Personel
        fields = '__all__'
        
class AvancementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Avancement
        fields = '__all__'
        


class AbsanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Absance
        fields = '__all__'
        

class SanctionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sanction
        fields = '__all__'
        
class RandementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Randement
        fields = '__all__'




class CongeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Conge
        fields = '__all__'
