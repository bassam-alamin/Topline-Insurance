from django.conf.urls import url
from . import views

app_name = 'vehicle'

urlpatterns = [
    url(r'^$', views.home.as_view(), name='home'),
    url(r'broadcast/$', views.broadcast_sms, name="sms"),
    url(r'topline/admin/$', views.Admin.as_view(), name="admin"),
    url(r'^cars/$', views.cars.as_view(), name='car-details'),
    url(r'^insurance_lists/$', views.Insurance_list.as_view(), name='insurance-details'),
    url(r'^logbook_lists/$', views.Logbook_list.as_view(), name='logbook-details'),

]