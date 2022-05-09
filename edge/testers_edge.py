from typing import Dict, List, Tuple

from edge.edge import reconstruct_edges
from preprocess.parse import parse_two_D_projections
from superclasses import PointWithId
from type import Reconstructed3DVertices, Parsed2DProjections
import unittest


class TestersEdge:
    @staticmethod
    def format_3_D_points(parsed_input: Parsed2DProjections, three_D_points: Dict[str, Tuple[str, str]]
                          ) -> Reconstructed3DVertices:
        formatted_3D_points = {}

        all_vertices_projections = {}
        for a_projection in parsed_input.values():
            for a_shape in a_projection.values():
                for a_vertex_id, a_vertex_point in a_shape['vertices'].items():
                    all_vertices_projections[a_vertex_id] = {
                        'x': a_vertex_point[0],
                        'y': a_vertex_point[1],
                        'z': a_vertex_point[2],
                    }

        for a_3D_point_id, projected_vertices_ids in three_D_points.items():
            formatted_3D_points[a_3D_point_id] = PointWithId(a_3D_point_id, all_vertices_projections[a_3D_point_id])
            formatted_3D_points[a_3D_point_id].attach_to_multiple_ancestors([
                all_vertices_projections[_id] for _id in projected_vertices_ids
            ])

            for a_projection_point_id in projected_vertices_ids:
                all_vertices_projections[a_projection_point_id].attach_to_ancestor(all_vertices_projections[a_3D_point_id])

        return formatted_3D_points

    @staticmethod
    def reconstruct_edges(input, reconstructed_3_D_points,
                          expected_edge_reconstructed: List[List[str]], expected_edge_dandling: List[List[str]] = None):
        expected_edge_dandling = expected_edge_dandling or []

        parsed_input = parse_two_D_projections(input)
        parsed_reconstructed_3_D_points = TestersEdge.format_3_D_points(parsed_input, reconstructed_3_D_points)
        reconstructed_3_D_edges_output, dandling_3_D_edges_output = \
            reconstruct_edges(parsed_input, parsed_reconstructed_3_D_points)

        reconstructed_3_D_edges = []
        for a_reconstructed_edge in reconstructed_3_D_edges_output.values():
            reconstructed_3_D_edges.append(tuple([
                a_three_D_point.id for a_three_D_point in a_reconstructed_edge.three_D_points
            ]))

        dandling_3_D_edges = []
        for a_dandling_edge in dandling_3_D_edges_output.values():
            dandling_3_D_edges.append(tuple([
                a_three_D_point.id for a_three_D_point in a_dandling_edge.three_D_points
            ]))

        unittest.TestCase().assertCountEqual(expected_edge_reconstructed, reconstructed_3_D_edges)
        unittest.TestCase().assertCountEqual(expected_edge_dandling, dandling_3_D_edges)
