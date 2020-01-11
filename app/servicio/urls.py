from django.conf.urls import url
from servicio.views import *

urlpatterns=[
    url(r'^servicio',EmpleadoList.as_view(),name='empleados')
]
