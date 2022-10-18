from django.urls import path
from . import views
urlpatterns = [
    path('',views.userlogin, name='login'),
    path('result', views.result, name='result'),
    path('logout', views.userlogout, name='logout')
]
