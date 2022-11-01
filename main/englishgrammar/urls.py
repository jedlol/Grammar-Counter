from django.urls import path, include
from . import views
from django.views.generic.base import TemplateView


urlpatterns = [
    path("accounts/", include("django.contrib.auth.urls")),
    path('', TemplateView.as_view(template_name='home.html'), name='home'),
    path("register/", views.register_request, name="register"),
    path('', views.button),
    path('external/', views.external),
    path('filternal/', views.filternal),
]
