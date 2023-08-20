from rest_framework import serializers
from tracking.models import TrackingData

class apiSerializer(serializers.ModelSerializer):
     class Meta:
        model = TrackingData
        fields ='__all__'
    