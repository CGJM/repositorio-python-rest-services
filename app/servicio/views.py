from rest_framework import generics
from .models import Empleado
from .serializer import EmpleadoSerializer
from django.shortcuts import get_object_or_404

class EmpleadoList(generics.ListCreateAPIView):
    queryset=Empleado.objects.all()
    serializer_class=EmpleadoSerializer

    def get_object(self):
        queryset=self.get_queryset()
        obj=get_object_or_404(
            queryset,
            pk=self.kwargs['pk']
        )
        return obj
