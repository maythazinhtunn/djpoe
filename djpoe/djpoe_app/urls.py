from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about', views.about, name='about'),
    path('add/<int:num1>/<int:num2>', views.add, name='add'),
    path('info/<str:name>/<int:age>', views.info, name='info')
    
]
