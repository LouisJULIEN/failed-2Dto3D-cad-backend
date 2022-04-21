from typing import List, Dict, TypedDict

from shapely.geometry import LineString

from superclasses import PointWithId, PolygonWithId
from type import parsed_2D


class Raw2DShape(TypedDict):
    type: str
    constAxis: str
    id: int
    vertices: Dict[int, tuple]


Raw2DProjections = List[List[Raw2DShape]]


def parse_two_D_projections(two_D_projections: Raw2DProjections) -> parsed_2D:
    parsed_two_D_projections = []
    for a_projection in two_D_projections:
        a_parsed_shapes_two_D_projection = []
        a_parsed_edges_two_D_projection = []
        a_parsed_vertices_two_D_projection = []

        a_shape: Raw2DShape
        for a_shape in a_projection:
            a_parsed_vertices_two_D_projection += [
                PointWithId(_id, a_vertex) for _id, a_vertex in a_shape["vertices"].items()
            ]

            assert a_shape["type"] == "polygon"

            a_parsed_edges_two_D_projection += [
                LineString([a_parsed_vertices_two_D_projection[i], a_parsed_vertices_two_D_projection[i + 1]])
                for i in range(len(a_parsed_vertices_two_D_projection) - 1)
            ]
            a_parsed_edges_two_D_projection += [
                LineString([a_parsed_vertices_two_D_projection[-1], a_parsed_vertices_two_D_projection[0]])]

            a_parsed_shapes_two_D_projection.append(
                PolygonWithId(a_shape['id'], a_parsed_vertices_two_D_projection))

        parsed_two_D_projections.append({
            "shapes": a_parsed_shapes_two_D_projection,
            "edges": a_parsed_edges_two_D_projection,
            "vertices": a_parsed_vertices_two_D_projection,
        })

    return parsed_two_D_projections
