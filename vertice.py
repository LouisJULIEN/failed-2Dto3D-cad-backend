from constant import MAX_POINT_TO_POINT_ERROR_DISTANCE
from superclasses import PointWithId
from type import parsed_2D


def find_candidate_vertices(parsed_two_D_projections: parsed_2D):
    # we suppose Y is the common dimension
    # first element of the list is on (X;Y)
    # second element of the list is on (Y;Z)

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

    found_3D_points = remove_duplicated_reconstructed_points(found_3D_points)
    dandling_points = []
    return found_3D_points, dandling_points


def remove_duplicated_reconstructed_points(found_3D_points):
    # Remove duplicates created by aligned in an ignored direction
    # for example two an_xy_point with different z value

    def get_coordinates(item1):
        return item1.x, item1.y, item1.z

    found_3D_points.sort(key=get_coordinates)

    i = 0
    while i < len(found_3D_points) - 1:
        if found_3D_points[i].distance(found_3D_points[i + 1]) < MAX_POINT_TO_POINT_ERROR_DISTANCE:

            point_with_links_to_remove = found_3D_points[i + 1].links - found_3D_points[i].links
            for a_point_with_link_to_remove in point_with_links_to_remove:
                a_point_with_link_to_remove.remove_link(found_3D_points[i + 1])

            found_3D_points[i].link_to_multiples(found_3D_points[i + 1].links)
            print(f"{list(found_3D_points[i].coords)} {list(found_3D_points[i + 1].coords)}")
            del found_3D_points[i + 1]
        else:
            i += 1
    return found_3D_points
