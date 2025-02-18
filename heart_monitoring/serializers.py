from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import Patient, HeartRateRecord



class UserRegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = get_user_model()
        fields = ('id', 'email', 'username', 'password')

    def create(self, validated_data):
        user = get_user_model().objects.create_user(
            email=validated_data['email'],
            username=validated_data['username'],
            password=validated_data['password']
        )
        return user



class UserLoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField()



class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patient
        fields = '__all__'



class HeartRateRecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = HeartRateRecord
        fields = '__all__'
