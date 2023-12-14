from django.shortcuts import render, redirect
from django.contrib.auth import logout
from .models import UserProfile
from django.views import generic
# Create your views here.
def home(request):
    return render(request, 'home.html')

def landing(request):
    return render(request, 'landing.html')
def logout_view(request):
    logout(request)
    return redirect("/")

class UserView(generic.DetailView):
    model = UserProfile
    template_name = "logged_in.html"

    def get_queryset(self, queryset = None):
        return self.request.user.userprofile