from django.contrib.gis.geos import Point
from rest_framework import generics
from rest_framework.response import Response

from world.models import WorldBorder
from world.serializers import WorldBorderSerializer


class WorldBordersPointSearch(generics.RetrieveAPIView):
    queryset = WorldBorder.objects.all()
    serializer_class = WorldBorderSerializer

    def get_object(self):
        try:
            lon = self.request.query_params["lon"]
            lat = self.request.query_params["lat"]
        except KeyError:
            return Response({"error": "lon and lat are required"}, status=400)

        point = Point(float(lon), float(lat))
        border = WorldBorder.objects.filter(mpoly__intersects=point).first()

        return border
