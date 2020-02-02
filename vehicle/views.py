from django.contrib.auth.models import User
from django.views.generic import View, ListView
from .models import *
from twilio.rest import Client
from django.conf import settings
from django.shortcuts import render
import datetime


def broadcast_sms(request):
    message_to_broadcast = "Welcome to Topline Limited,Hey Bashir am sorry but ur Insurance is expiring today"
    client = Client(settings.TWILIO_ACCOUNT_SID, settings.TWILIO_AUTH_TOKEN)
    today = datetime.datetime.now().date()
    print(today)
    today = datetime.datetime(2020, 2, 7)
    print(today.date())
    insurance = Insurance.objects.all()
    result = insurance.filter(expiry_date__icontains=today.date())
    print("almost there", len(result))
    for i in result:
        car = i.car_id
        cars = Cars.objects.all()
        sorted_cars = cars.filter(id=car)
        print("cars are ", len(sorted_cars))
        for b in sorted_cars:
            owner = b.car_owner_id
            owners = Owner.objects.all()
            sorted_owners = owners.filter(id=owner)

            print("owners are ", len(sorted_owners))
            for n in sorted_owners:
                settings.SMS_BROADCAST_TO_NUMBERS.append(n.phone_no)

    for recipient in settings.SMS_BROADCAST_TO_NUMBERS:
        if recipient:
            client.messages.create(to=recipient,
                                   from_=settings.TWILIO_NUMBER,
                                   body=message_to_broadcast)
    return render(request, "vehicle/home.html")


class home(ListView):
    template_name = 'vehicle/home.html'

    def get_queryset(self):
        return Cars.objects.all()


class cars(ListView):
    template_name = 'vehicle/cars.html'

    def get_queryset(self):

        query1 = self.request.GET.get("plate_no")
        result = Cars.objects.all()
        if query1:
            logbooks = Logbook.objects.all()
            result = logbooks.filter(vehicle_registration__icontains=query1)
            for i in result:
                result = Cars.objects.filter(logbook=i.id)

        query = self.request.GET.get('date')

        if query:
            insurance = Insurance.objects.all()
            result = insurance.filter(expiry_date__icontains=query)
            print("almost there", len(result))

        return result


class Insurance_list(ListView):
    template_name = 'vehicle/insurance.html'

    def less(self):
        base = datetime.datetime.today().date()
        start_week = base - datetime.timedelta(base.weekday())
        start = datetime.datetime(start_week.year, start_week.month, start_week.day)
        end_week = start_week + datetime.timedelta(7)
        end = datetime.datetime(end_week.year, end_week.month, end_week.day)

        result = Insurance.objects.filter(expiry_date__range=[start, end])
        print(len(result))
        return result

    def get_queryset(self):
        query = self.request.GET.get('date')
        query1 = self.request.GET.get('less')
        query2 = self.request.GET.get('all')
        result = self.less()

        if query1:
            result = self.less()
        if query2:
            result = Insurance.objects.all()
        if query:
            insurance = Insurance.objects.all()
            result = insurance.filter(expiry_date__icontains=query)
            print("almost there", len(result))

        return result


class Logbook_list(ListView):
    template_name = 'vehicle/logbooks.html'

    def get_queryset(self):
        query = self.request.GET.get('date')
        result = Logbook.objects.all()
        if query:
            insurance = Logbook.objects.all()
            result = insurance.filter(vehicle_registration__icontains=query)
            print("almost there", len(result))

        return result


class Admin(View):
    template_name = 'vehicle/admin.html'

    def get(self, request):
        return render(request, self.template_name)
