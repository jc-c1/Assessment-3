from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('add_wackywidgets/', views.add_wackywidgets, name='add_wackywidgets'),

    path('wackywidgets/<int:pk>/delete/',
         views.wackywidgetsDelete.as_view(), name='wackywidgets_delete'),
]
