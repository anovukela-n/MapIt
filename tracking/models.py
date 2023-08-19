from django.db import models

class TrackingData(models.Model):
    id =models.AutoField(primary_key=True)
    vehicleid = models.IntegerField()
    timestamp = models.DateTimeField()
    coordinate_longitude = models.FloatField()
    coordinate_latitude =models.FloatField() #PointField()
    event_description=models.CharField(max_length=100)
    speed =models.IntegerField()
    heading =models.IntegerField()
    ignitionState=models.CharField(max_length=25)
    gps_accuracy=models.IntegerField()
    gps_fix_type =models.IntegerField()

    class Meta:
        verbose_name = 'Tracking Data'
        verbose_name_plural = 'Tracking Data Entries'
        
    def __str__(self):
        return f"TrackingData for Vehicle ID {self.vehicleid}"