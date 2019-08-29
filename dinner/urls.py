from django.contrib.auth.decorators import login_required
from django.urls import path
from django.views.generic import TemplateView

urlpatterns = [
    path('', login_required(TemplateView.as_view(template_name='home.html')), name='home'),
]
