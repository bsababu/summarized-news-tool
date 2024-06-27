from django.urls import path
from .views import InshamakeZinkuru

urlpatterns = [
    path('inshamake/', InshamakeZinkuru.as_view(), name='inshamake'),
]