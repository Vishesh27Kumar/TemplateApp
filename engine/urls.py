from django.urls import re_path
from . import views

urlpatterns = [
    re_path('customer/(?P<customer_id>[0-9]{5})/templates', views.handleGetAndCreateCustomerTemplates, name='getAndCreateCustomerTemplates'),
]