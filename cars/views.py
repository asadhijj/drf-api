from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView
from .serializers  import carsSerializer
from .models import cars


class carsListView(ListCreateAPIView):
    queryset=cars.objects.all()
    serializer_class= carsSerializer


class carsDetailView(RetrieveUpdateDestroyAPIView):
    queryset=cars.objects.all()
    serializer_class= carsSerializer
