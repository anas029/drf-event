from event.permissions import AuthenticatedOrReadOnly
from .models import Event, Venue
from .serializers import EventSerializer, VenueSerializer
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated


class EventListCreate(generics.ListCreateAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    permission_classes = [AuthenticatedOrReadOnly]


class EventRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer


class VenueListCreate(generics.ListCreateAPIView):
    queryset = Venue.objects.all()
    serializer_class = VenueSerializer
    permission_classes = [IsAuthenticated]


class VenueRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Venue.objects.all()
    serializer_class = VenueSerializer
