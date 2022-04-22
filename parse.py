from typing import List, Dict, TypedDict, Tuple

from shapely.geometry import LineString

from superclasses import PointWithId, PolygonWithId, LineStringWithId
from type import parsed_2D_projections


class Raw2DShape(TypedDict):
    type: str
    constAxis: str
    id: int
    vertices: Dict[int, tuple]
    edges: Dict[int, Tuple[int, int]]


Raw2DProjections = List[List[Raw2DShape]]


def parse_two_D_projections(two_D_projections: Raw2DProjections) -> parsed_2D_projections:
    parsed_two_D_projections = []
    for a_projection in two_D_projections:
        a_parsed_shapes_two_D_projection = []
        a_parsed_edges_two_D_projection = []
        a_parsed_vertices_two_D_projection = []

        a_shape: Raw2DShape
        for a_shape in a_projection:

            dict_of_parsed_vertices = {
                _id: PointWithId(_id, a_vertex) for _id, a_vertex in a_shape["vertices"].items()
            }
            a_parsed_vertices_two_D_projection += list(dict_of_parsed_vertices.values())

            for edge_id, points_id in a_shape["edges"].items():
                a_parsed_edges_two_D_projection.append(
                    LineStringWithId(edge_id, [dict_of_parsed_vertices[a_point_id] for a_point_id in points_id])
                )

            assert a_shape["type"] == "polygon"
            a_parsed_shapes_two_D_projection.append(
                PolygonWithId(a_shape['id'], a_parsed_vertices_two_D_projection))

        parsed_two_D_projections.append({
            "shapes": a_parsed_shapes_two_D_projection,
            "edges": a_parsed_edges_two_D_projection,
            "vertices": a_parsed_vertices_two_D_projection,
        })

    return parsed_two_D_projections
