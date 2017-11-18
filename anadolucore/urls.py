from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns

from anadolucore.views import CustomerList, CustomerDetail

urlpatterns = [
    url(r'^customer/$', CustomerList.as_view()),
    url(r'^customer/(?P<pk>[0-9]+)$', CustomerDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)