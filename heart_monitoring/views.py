
# Create your views here.

from rest_framework import viewsets, status, permissions
from rest_framework.response import Response
from rest_framework.decorators import action
from django.contrib.auth import authenticate, login, get_user_model
from .models import Patient, HeartRateRecord
from .serializers import (
    UserRegistrationSerializer, UserLoginSerializer,
    PatientSerializer, HeartRateRecordSerializer
)

User = get_user_model()


class AuthViewSet(viewsets.ViewSet):
    permission_classes = [permissions.AllowAny]

    @action(detail=False, methods=['post'])
    def register(self, request):
        serializer = UserRegistrationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    @action(detail=False, methods=['post'])
    def login(self, request):
        serializer = UserLoginSerializer(data=request.data)
        if serializer.is_valid():
            email_or_username = serializer.validated_data['email'] 
            password = serializer.validated_data['password']

            user = None
            # Check if the input is an email or username
            if '@' in email_or_username:
                user = User.objects.filter(email=email_or_username).first()
            else:
                user = User.objects.filter(username=email_or_username).first()

            # Authenticate if user is found
            if user:
                auth_user = authenticate(request, username=user.username, password=password)
                if auth_user:
                    login(request, auth_user)
                    return Response({'message': 'Login successful'}, status=status.HTTP_200_OK)
            return Response({'error': 'Invalid username or password'}, status=status.HTTP_401_UNAUTHORIZED)
       
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    


class PatientViewSet(viewsets.ModelViewSet):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer

    

class HeartRateRecordViewSet(viewsets.ModelViewSet):
    queryset = HeartRateRecord.objects.all()
    serializer_class = HeartRateRecordSerializer

    def get_queryset(self):
        queryset = HeartRateRecord.objects.all()
        patient_id = self.request.query_params.get('patient_id', None)
        if patient_id is not None:
            queryset = queryset.filter(patient_id=patient_id)
        return queryset
