import re
from django.utils.timezone import datetime
from django.http import HttpResponse
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.shortcuts import get_object_or_404, render
from django.http import JsonResponse
from .models import TrackingData
from django.contrib import messages
import pandas as pd

from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect
from api_serializer.serializer import apiSerializer
from django.template import loader

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

#this function pulls the data from db as json and exposes it in browser
@api_view(['GET'])
def GetDataAsJson(request):
    all_records= TrackingData.objects.all()
    jsonTracking =apiSerializer(all_records,many=True)
    return Response(jsonTracking.data)


def get_records(request):# you can put this one in a context and html file
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

    return JsonResponse(data, safe=False)#instead you would say return(request,context,html)"""

def getTable(request):
   records = TrackingData.objects.all().values()
   context = {
    'records': records,
   }
   return render(request,'tracking/table.html', context)#edit table

@api_view(['DELETE'])
def delete(request, id):
    try:
        #records = TrackingData.objects.get(id=id)
        records = get_object_or_404(TrackingData, id=id)
        print(records)
        records.delete()

        return Response({'message': f'Data with id {id} has been deleted.'})
    except TrackingData.DoesNotExist:
        return Response({'error': f'Data with id {id} does not exist.'}, status=404)


#this view is for creating a single new record for tracking data
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
    #return JsonResponse({"message": "Invalid request."})#render form wwith inputs
    return render(request, 'tracking/newRecord.html') 

def updateRecord(request, id):
    try:
        coordinate_longitude = request.POST.get('coordinate_longitude')
        coordinate_latitude = request.POST.get('coordinate_latitude')
        record = TrackingData.objects.get(id=id)
        record.coordinate_longitude = coordinate_longitude
        record.coordinate_latitude= coordinate_latitude
        record.save()
        return HttpResponseRedirect(reverse('table')) 
    except Exception as e:
         error_message = f"The id does not exist: {str(e)}"

    return render(request, 'tracking/errorMessage.html', {'error_message': error_message}) 