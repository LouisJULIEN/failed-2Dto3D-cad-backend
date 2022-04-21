from typing import List, TypedDict

from shapely.geometry import LineString

from superclasses import PointWithId, PolygonWithId


class AParsedProjection(TypedDict):
    shapes: List[PolygonWithId]
    edges: List[LineString]
    vertices: List[PointWithId]


parsed_2D = List[AParsedProjection]
