from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns

from anadolucore.views import CustomerList, CustomerDetail, L0List, L1List, L2List, L3List, L4List, LList

urlpatterns = [
    url(r'^customer/$', CustomerList.as_view()),
    url(r'^customer/(?P<pk>[0-9]+)$', CustomerDetail.as_view()),
    url(r'^l0/$', L0List),
    url(r'^l1/$', L1List),
    url(r'^l2/$', L2List),
    url(r'^l3/$', L3List),
    url(r'^l4/$', L4List),
    url(r'^l/$', LList),
]

urlpatterns = format_suffix_patterns(urlpatterns)