from django.urls import path

from ProductApp.views import HomeView, ProductView


urlpatterns = [
    path('',HomeView),
    path('product/',ProductView)
]