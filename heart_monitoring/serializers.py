from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import Patient, HeartRateRecord



class UserRegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = get_user_model()
        fields = ('id', 'email', 'username', 'password')
        extra_kwargs = {
            'username': {'required': False},  
        }

    def create(self, validated_data):
        username = validated_data.get('username', validated_data['email'])
        password = validated_data.pop('password')

        user = get_user_model().objects.create_user(
            email=validated_data['email'],
            username=username,
            password=password
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
