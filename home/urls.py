from django.urls import path
from . import views
urlpatterns = [
    path('', views.HomeView.as_view(), name='homepage'),
    path('contact_us', views.ContactUsView.as_view(), name='contact-us'),
]
