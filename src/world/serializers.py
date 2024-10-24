from rest_framework_gis.serializers import GeoModelSerializer

from world.models import WorldBorder

class WorldBorderSerializer(GeoModelSerializer):
    class Meta:
        model = WorldBorder
        geo_field = "mpoly"
        fields = ("id", "name", "mpoly")