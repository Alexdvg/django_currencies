from django.urls import path
from exchanger import views


urlpatterns = [
    path('',views.converter, name='exchange')
]