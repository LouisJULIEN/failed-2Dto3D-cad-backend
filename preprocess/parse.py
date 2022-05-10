from superclasses import PointWithId, ProjectedLineStringWithId
from type import Parsed2DProjections, Raw2DShape, Raw2DProjections


def parse_two_D_projections(two_D_projections: Raw2DProjections) -> Parsed2DProjections:
    parsed_two_D_projections = {}
    for a_projection_axes, a_projection in two_D_projections.items():
        parsed_two_D_projections[a_projection_axes] = {}

        a_shape: Raw2DShape
        for a_shape_id, a_shape in a_projection.items():

            dict_of_parsed_vertices = {
                _id: PointWithId(_id, (a_vertex['x'], a_vertex['y'], a_vertex['z'])) for _id, a_vertex in a_shape["vertices"].items()
            }

            dict_of_parsed_edges = {}
            for edge_id, edge_data in a_shape["edges"].items():
                dict_of_parsed_edges[edge_id] = (
                    ProjectedLineStringWithId(edge_id, [
                        dict_of_parsed_vertices[a_point_id] for a_point_id in edge_data['verticesIds']
                    ])
                )

            parsed_two_D_projections[a_projection_axes][a_shape_id] = {
                "type": a_shape["type"],
                "edges": dict_of_parsed_edges,
                "vertices": dict_of_parsed_vertices,
            }

    return parsed_two_D_projections
