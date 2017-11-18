from django.conf.urls import url, include
from .views import *

urlpatterns = [
    url('getComboValues/', getAllFields),
    url('getCorMatrix/', getCorMatrix),
    url('getDistMatrix/', getDistMatrix),
    url('getCountMatrix/', getCountMatrix),
    url('getAssociationRules/', getAssociationRules),
    url('getPolicyFields/', getPolicyFields),
    url('predictionSystem/', predictionSystem),
    url('predictUser/', predictUser),
    url(r'^results/$', RecommendationList.as_view()),
    url(r'^results/(?P<pk>[0-9]+)$', RecommendationDetail.as_view()),
]
