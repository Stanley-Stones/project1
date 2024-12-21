from django.urls import path
from . import views as authviews


urlpatterns = [
    path('register/', authviews.register, name = 'register'),
    path('login/', authviews.login, name = 'login'),
    path('logout/', authviews.logout, name = 'logout'),
]
