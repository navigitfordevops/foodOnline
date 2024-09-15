from django.urls import path, include
from .views import vprofile
from accounts import views as AccountViews

urlpatterns = [
    path("", AccountViews.vendorDashboard),
    path("profile/", vprofile, name='vprofile')

]
