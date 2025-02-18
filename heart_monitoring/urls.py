from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import AuthViewSet, PatientViewSet, HeartRateRecordViewSet

router = DefaultRouter()
router.register(r'auth', AuthViewSet, basename='auth')
router.register(r'patients', PatientViewSet)
router.register(r'heart-rates', HeartRateRecordViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
