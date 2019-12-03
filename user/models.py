from django.db import models


class Information(models.Model):
    user_id = models.IntegerField()
    bus_name = models.CharField(max_length=1000)
    start_date = models.CharField(max_length=100)
    currency = models.CharField(max_length=100)
    bus_no = models.CharField(max_length=20)
    alt_bus_no = models.CharField(max_length=20)
    address = models.CharField(max_length=1000)
    address2 = models.CharField(max_length=1000)
    bus_website = models.CharField(max_length=1000)
    country = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    zip_code = models.CharField(max_length=100)
    bus_logo = models.FileField(upload_to='media')

    class Meta:
        db_table = 'information'
