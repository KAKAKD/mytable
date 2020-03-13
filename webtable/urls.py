from django.urls import path
from . import views


app_name = 'webtable'

urlpatterns = [
    path('', views.index, name='index'),
    path('info/', views.info, name='info'),
    path('create/', views.create, name='create'),
    path('update/<int:num>', view.update, name='update'),
]
