from typing import List, TypedDict

from superclasses import PointWithId, PolygonWithId, LineStringWithId


class AParsedProjection(TypedDict):
    shapes: List[PolygonWithId]
    edges: List[LineStringWithId]
    vertices: List[PointWithId]


parsed_2D_projections = List[AParsedProjection]

Reconstructed3DPoints = List[PointWithId]
Reconstructed3DEdges = List[LineStringWithId]
