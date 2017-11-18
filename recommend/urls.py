from django.conf.urls import url, include
from .views import *

urlpatterns = [
    url('getComboValues/', getAllFields),
    url('getCorMatrix/', getCorMatrix),
    url('getDistMatrix/', getDistMatrix),
    url('getCountMatrix/', getCountMatrix),

]
