from django.urls import path
from .views import carsListView, carsDetailView

urlpatterns = [
    path("cars/", carsListView.as_view(), name="cars-list"),
    path("cars/<int:pk>", carsDetailView.as_view(), name="cars-detail"),
 
]