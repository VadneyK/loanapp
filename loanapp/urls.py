from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from loanapp import views

urlpatterns = [
    path('applications/', views.ApplicationList.as_view(), name='application-list'),
    path('applications/<int:pk>/', views.ApplicationDetail.as_view(), name='application-detail'),
    path('users/', views.UserList.as_view(), name='user-list'),
    path('users/<int:pk>/', views.UserDetail.as_view(), name='user-detail'),
    path('', views.api_root),
]

urlpatterns = format_suffix_patterns(urlpatterns)