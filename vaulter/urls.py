from django.urls import path
from .views import (
    SafeListView, 
    SafeDetailView,
    SafeCreateView,
    SafeUpdateView,
    SafeDeleteView
)
from . import views

urlpatterns = [
    path('', SafeListView.as_view(), name='vaulter-home'),
    path('safe/<int:pk>/', SafeDetailView.as_view(), name='safe-detail'),
    path('safe/new/', SafeCreateView.as_view(), name='safe-create'),
    path('safe/<int:pk>/update/', SafeUpdateView.as_view(), name='safe-update'),
    path('safe/<int:pk>/delete/', SafeDeleteView.as_view(), name='safe-delete'),
    path('about/', views.about, name='vaulter-about'),

]
