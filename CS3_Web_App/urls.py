from django.contrib import admin
from django.urls import path

from CS3_Web_App import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('login/', views.login, name='login'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('signup/', views.signup, name='signup'),
    path('profile/', views.ownprofile, name='ownprofile'),
    path('profile/<name>', views.publicprofile, name='publicprofile'),
    path('reset/', views.reset),
    path('postReset/', views.postReset),
]
