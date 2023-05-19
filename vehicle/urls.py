from django.urls import re_path
from . import views

app_name = 'vehicle'

urlpatterns = [
    re_path(r'^$', views.home.as_view(), name='home'),
    re_path(r'broadcast/$', views.broadcast_sms, name="sms"),
    re_path(r'topline/admin/$', views.Admin.as_view(), name="admin"),
    re_path(r'^cars/$', views.cars.as_view(), name='car-details'),
    re_path(r'^insurance_lists/$', views.Insurance_list.as_view(), name='insurance-details'),
    re_path(r'^logbook_lists/$', views.Logbook_list.as_view(), name='logbook-details'),

]