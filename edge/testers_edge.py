from typing import Dict, List, Tuple

from edge import reconstruct_edges
from preprocess.parse import parse_two_D_projections
from superclasses import PointWithId
from type import Reconstructed3DPoints, Parsed2DProjections
import unittest


class TestersEdge:
    id_number = 0

    @staticmethod
    def format_3_D_points(parsed_input: Parsed2DProjections, three_D_points: Dict[int, List[int]]
                          ) -> Reconstructed3DPoints:
        formatted_3D_points = {}

        all_vertices_projections = {}
        for a_projection in parsed_input.values():
            for a_shape in a_projection.values():
                for a_vertex_id, a_vertex_point in a_shape['vertices'].items():
                    all_vertices_projections[a_vertex_id] = a_vertex_point

        for a_3D_point_id, projected_vertices_ids in three_D_points.items():
            formatted_3D_points[a_3D_point_id] = PointWithId(a_3D_point_id)
            formatted_3D_points[a_3D_point_id].link_to_multiples([
                all_vertices_projections[_id] for _id in projected_vertices_ids
            ])

            for a_projection_point_id in projected_vertices_ids:
                all_vertices_projections[a_projection_point_id].link_to(formatted_3D_points[a_3D_point_id])

        return formatted_3D_points

    @staticmethod
    def reconstruct_edges(input, reconstructed_3_D_points, expected_vertices: List[Tuple[int, int]]):
        parsed_input = parse_two_D_projections(input)
        parsed_reconstructed_3_D_points = TestersEdge.format_3_D_points(parsed_input, reconstructed_3_D_points)
        reconstructed_3_D_edges = reconstruct_edges(parsed_input, parsed_reconstructed_3_D_points)

        unittest.TestCase().assertCountEqual(expected_vertices, reconstructed_3_D_edges.values())
