from rest_framework import serializers
from .models import Event, Venue


class VenueSerializer(serializers.ModelSerializer):
    class Meta:
        model = Venue
        fields = '__all__'


class EventSerializer(serializers.ModelSerializer):
    venue = VenueSerializer(read_only=True)
    venue_id = serializers.PrimaryKeyRelatedField(
        queryset=Venue.objects.all(), write_only=True, source='venue'
    )  # Use venue_id for write operations

    class Meta:
        model = Event
        fields = '__all__'
