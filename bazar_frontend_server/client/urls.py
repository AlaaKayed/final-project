from django.urls import path
from .views import search, purchase, info

urlpatterns = [
    path('search/<str:topic>', search),
    path('info/<int:pk>', info), 
    path('purchase/<int:pk>', purchase)
]