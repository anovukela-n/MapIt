import re
from django.utils.timezone import datetime
from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import get_object_or_404, render
from django.http import JsonResponse
from .models import TrackingData
import pandas as pd

def home(request):
    return HttpResponse("Hello, Django!")


def load_csv_data(request):
    # Read data from CSV using pandas
    csv_data = pd.read_csv('tracking/tests.csv')

    # Loop through the CSV data and populate the database
    for index, row in csv_data.iterrows():
        vehicleid= row['vehicleid']
        timestamp =row['timestamp']
        coordinate_longitude=row['coordinate_longitude']
        coordinate_latitude =row['coordinate_latitude']
        event_description=row['event_description']
        speed=row['speed']
        heading=row['heading']
        ignitionState=row['ignitionState']
        gps_accuracy=row['gps_accuracy']
        gps_fix_type=row['gps_fix_type']

        TrackingData.objects.create(vehicleid=vehicleid, timestamp=timestamp,
                                    coordinate_longitude=coordinate_longitude,
                                    coordinate_latitude=coordinate_latitude,event_description=event_description,
                                    speed=speed,heading=heading,ignitionState=ignitionState,
                                    gps_accuracy=gps_accuracy,gps_fix_type=gps_fix_type)

    return JsonResponse({"message": "CSV data loaded successfully."})

def hello_there(request, name):
    print(request.build_absolute_uri()) #optional
    return render(
        request,
        'tracking/hello_there.html',
        {
            'name': name,
            'date': datetime.now()
        }
    )
def get_records(request):
    records = TrackingData.objects.all()
    data =[
    {"vehicleid" :TrackingData.vehicleid,
    "timestamp" :TrackingData.timestamp,
    "coordinate_longitude" : TrackingData.coordinate_longitude,
    "coordinate_latitude" :TrackingData.coordinate_latitude,
    "event_description":TrackingData.event_description, 
    "speed" :TrackingData.speed,
    "heading" :TrackingData.heading,
    "ignitionState":TrackingData.ignitionState,
    "gps_accuracy":TrackingData.gps_accuracy,
    "gps_fix_type":TrackingData.gps_fix_type
    } for record in records]

    return JsonResponse(data, safe=False)

def create_record(request):
    if request.method == 'POST':
        vehicleid= request.POST.get('vehicleid')
        timestamp =request.POST.get('timestamp')
        coordinate_longitude=request.POST.get('coordinate_longitude')
        coordinate_latitude =request.POST.get('coordinate_latitude')
        event_description=request.POST.get('event_description')
        speed=request.POST.get('speed')
        heading=request.POST.get('heading')
        ignitionState=request.POST.get('ignitionState')
        gps_accuracy=request.POST.get('gps_accuracy')
        gps_fix_type=request.POST.get('gps_fix_type')
        trackingData = TrackingData.objects.create(vehicleid=vehicleid, timestamp=timestamp,
                                            coordinate_longitude=coordinate_longitude,
                                            coordinate_latitude=coordinate_latitude,event_description=event_description,
                                            speed=speed,heading=heading,ignitionState=ignitionState,
                                            gps_accuracy=gps_accuracy,gps_fix_type=gps_fix_type)
        return JsonResponse({"message": "trackingData created successfully."})
    return JsonResponse({"message": "Invalid request."})