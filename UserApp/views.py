from django.shortcuts import render

# Create your views here.
def LoginView(request):
    return render(request,'login.html');

def SignupView(request):
    return render(request,'signup.html')