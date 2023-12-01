from . import views
from django.urls import path

urlpatterns = [
    path('',views.index,name="index"),
    path('signup/',views.signup,name='signup'),
    path('contact/',views.contact,name='contact'),
    path('contact/reset-password',views.reset_password,name="reset-password"),
    path('login/',views.login,name='login'),
    path('logout/',views.logout,name='logout'),
    path('login/reset-password',views.reset_password,name="reset-password"),
    path('forgot-password/',views.forgot_password,name="forgot-password"),
    path('otp_verification/',views.otp_verification,name="otp_verification"),
    path('new_password/',views.new_password,name="new_password")
]
