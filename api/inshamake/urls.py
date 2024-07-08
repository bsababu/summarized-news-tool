from django.urls import path
from .views import InshamakeZinkuru, SubscribeView

urlpatterns = [
    path('inshamake/', InshamakeZinkuru.as_view(), name='inshamake'),
    path('inshamake/subscribe/', SubscribeView.as_view(), name='subscribe')
]