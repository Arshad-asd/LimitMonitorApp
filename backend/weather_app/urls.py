from django.urls import path
from .views import *

urlpatterns = [
    path('user-criteria/', UserCriteriaListCreateAPIView.as_view(), name='user-criteria-list-create'),
    path('user-criteria/<int:pk>/', UserCriteriaRetrieveUpdateDestroyAPIView.as_view(), name='user-criteria-detail'),
]