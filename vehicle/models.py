from django.db import models


# Create your models here.
class Owner(models.Model):
    first_name = models.CharField(max_length=20)
    second_name = models.CharField(max_length=20)
    phone_no = models.CharField(max_length=13)
    id_no = models.CharField(max_length=8)
    location = models.CharField(max_length=20)

    def __str__(self):
        return self.first_name


class Logbook(models.Model):
    chases_no = models.CharField(max_length=20)
    engine = models.CharField(max_length=30)
    color = models.CharField(max_length=20)
    rating = models.CharField(max_length=30)
    vehicle_registration = models.CharField(max_length=50)
    seating_capacity = models.IntegerField()
    model = models.CharField(max_length=30)
    image = models.FileField()

    def __str__(self):
        return self.vehicle_registration


class Cars(models.Model):
    car_owner = models.ForeignKey(Owner,on_delete=models.CASCADE,related_name='owners')
    logbook = models.OneToOneField(Logbook, on_delete=models.CASCADE, related_name='cars')
    active_insurance = models.BooleanField(default=False)
    vehicle_image = models.FileField()


    def __str__(self):
        return self.logbook.vehicle_registration


class Insurance(models.Model):
    car = models.ForeignKey(Cars, on_delete=models.CASCADE, related_name='insurance')
    insurer = models.CharField(max_length=200)
    policy_number = models.CharField(max_length=200)
    commencing_date = models.DateTimeField()
    expiry_date = models.DateField()
    insurance_image = models.FileField()

    def __str__(self):
        return self.car.logbook.vehicle_registration
