from django.urls import path

from UserApp.views import LoginView,SignupView

urlpatterns = [
    path('',LoginView),
    path('signup/',SignupView)
]