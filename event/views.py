from event.permissions import AuthenticatedOrReadOnly
from .models import Event, Venue
from .serializers import EventSerializer, VenueSerializer
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response


class EventListCreate(generics.ListCreateAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    permission_classes = [AuthenticatedOrReadOnly]

    def post(self, request):
        user = request.user
        data = request.data
        data['organizer'] = user.id
        serializer = EventSerializer(data=data)
        if serializer.is_valid():
            # Saves that data to the Database
            serializer.save()
            return Response(serializer.data, status=200)
        return Response(None, status=500)


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
