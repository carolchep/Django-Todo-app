from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
urlpatterns = [
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('', views.DashboardView.as_view(), name='dashboard'),
    path('register/',views.register, name='register'),
    path('profile/', views.ProfileView.as_view(), name='Profile'),
    path('update/<int:pk>',views.profileupdate, name='update'),
]

