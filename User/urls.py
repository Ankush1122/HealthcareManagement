from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home, name='home'),
    path('login_signup/', views.login_signup, name='login_signup'),
    path('complete_profile_admin/', views.complete_profile_admin, name='complete_profile_admin'),
    path('complete_profile_doctor/', views.complete_profile_doctor, name='complete_profile_doctor'),
    path('complete_profile_hospital/', views.complete_profile_hospital, name='complete_profile_hospital'),
    path('complete_profile_insurance/', views.complete_profile_insurance, name='complete_profile_insurance'),
    path('complete_profile_law_enforcement/', views.complete_profile_law_enforcement, name='complete_profile_law_enforcement'),
    path('complete_profile_pathologist/', views.complete_profile_pathologist, name='complete_profile_pathologist'),
    path('complete_profile_patient/', views.complete_profile_patient, name='complete_profile_patient'),
    path('complete_profile_pharmacist/', views.complete_profile_pharmacist, name='complete_profile_pharmacist'),
    path('complete_profile_nurse/', views.complete_profile_nurse, name='complete_profile_nurse'),

    path('logout/', views.logout, name='logout')
]
