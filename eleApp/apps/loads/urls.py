from django.urls import path
from .views import LoadTemplateView

urlpatterns = [
    path('', LoadTemplateView.as_view(), name='load_file'),
]