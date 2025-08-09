from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .views import UserProfileView, DoctorListView, AppointmentCreateView, AppointmentListView, RegisterView

urlpatterns = [
    # Auth
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    # Profile
    path('profile/', UserProfileView.as_view(), name='user_profile'),

    # Doctors
    path('doctors/', DoctorListView.as_view(), name='doctor_list'),

    # Appointments
    path('appointments/create/', AppointmentCreateView.as_view(), name='appointment_create'),
    path('appointments/', AppointmentListView.as_view(), name='appointment_list'),
]
