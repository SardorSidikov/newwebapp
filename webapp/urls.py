from django.urls import path
from . import views
from django.contrib.auth import views as authviews

urlpatterns = [
    path('reg/', views.reg, name = "reg"),
    path('auth/', authviews.LoginView.as_view(template_name = 'webapp/auth.html'), name = "auth"),
    path('home/', views.home, name = "Home" )
]