from django.urls import path
from .views import *

app_name = 'home'
urlpatterns = [
    path('', DashboardListView.as_view(), name="dashboard"),
]
