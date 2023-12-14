from django.urls import path
from . import views

urlpatterns = [
    path("", views.home),
    path("logout/", views.logout_view),
    path("user/", views.UserView.as_view(), name='user_view'),
    path("landing/", views.landing)
]