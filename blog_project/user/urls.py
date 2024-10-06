from django.urls import path
from . import views

urlpatterns = [
    path('signup/', views.user_signup, name='user_signup'),
    path('login/', views.user_login, name='user_login'),
    path('profile/', views.user_profile, name='user_profile'),
    path('profile/edit_profile/', views.edit_profile, name='edit_profile'),
    path('profile/edit_profile/change_password/', views.change_password, name='change_password'),
    path('profile/edit_profile/change_password_without_old_password/', views.change_password_without_old_password, name='change_password_without_old_password'),
    path('logout/', views.user_logout, name='user_logout'),
]
