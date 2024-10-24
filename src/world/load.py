from pathlib import Path
from django.contrib.gis.utils import LayerMapping
from .models import WorldBorder

world_mapping = {
    "fips": "fips",
    "iso2": "iso2",
    "iso3": "iso3",
    "un": "un",
    "name": "name",
    "area": "area",
    "pop2005": "pop2005",
    "region": "region",
    "subregion": "subregion",
    "lon": "lon",
    "lat": "lat",
    "mpoly": "multipolygon",
}

world_shp = Path(__file__).resolve().parent / "data" / "tm_world_borders_0_3.shp"


def run(verbose=True):
    lm = LayerMapping(WorldBorder, world_shp, world_mapping, transform=False)
    lm.save(strict=True, verbose=verbose)