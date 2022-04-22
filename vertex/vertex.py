from typing import Tuple

from constant import MAX_POINT_TO_POINT_ERROR_DISTANCE
from superclasses import PointWithId
from type import parsed_2D_projections, Reconstructed3DPoints


def reconstruct_vertices(parsed_two_D_projections: parsed_2D_projections) \
        -> Tuple[Reconstructed3DPoints, Reconstructed3DPoints]:
    found_3D_points = []

    edges_xy = parsed_two_D_projections[0]["vertices"]
    edges_yz = parsed_two_D_projections[1]["vertices"]
    edges_xz = parsed_two_D_projections[2]["vertices"]

    matched_a_3D_point: bool
    an_xy_point: PointWithId
    an_yz_point: PointWithId
    an_xz_point: PointWithId

    three_d_point_id = 10000

    for an_xy_point in edges_xy:
        for an_yz_point in edges_yz:
            if abs(an_xy_point.y - an_yz_point.y) < MAX_POINT_TO_POINT_ERROR_DISTANCE:  # to lower computation cost
                for an_xz_point in edges_xz:

                    first_point = PointWithId(three_d_point_id, an_xy_point.x, an_yz_point.y, an_xz_point.z)
                    three_d_point_id += 1
                    second_point = PointWithId(three_d_point_id, an_xz_point.x, an_xy_point.y, an_yz_point.z)
                    three_d_point_id += 1

                    if first_point.distance(second_point) < MAX_POINT_TO_POINT_ERROR_DISTANCE:
                        first_point.link_to_multiples([an_xy_point, an_xz_point, an_yz_point])
                        found_3D_points.append(first_point)
                        an_xy_point.link_to(first_point)
                        an_xz_point.link_to(first_point)
                        an_yz_point.link_to(first_point)

    dandling_points = []

    for a_project_point in edges_xy + edges_xz + edges_yz:
        if a_project_point.is_linked_to_none():
            dandling_points.append(a_project_point)

    return found_3D_points, dandling_points
