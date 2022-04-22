from graphics import draw_3D_points_list
from parse import parse_two_D_projections
from vertice import find_candidate_vertices


class Testers:
    id_number = 0

    @staticmethod
    def __add_ids(input):
        all_axis_projection_with_ids = []
        for an_axis_projection in input:
            an_axis_projection_with_ids = []

            for a_shape in an_axis_projection:
                a_shape['id'] = Testers.id_number
                Testers.id_number += 1

                formatted_vertices = {}
                for a_point in a_shape["vertices"]:
                    formatted_vertices[Testers.id_number] = a_point
                    Testers.id_number += 1

                a_shape["vertices"] = formatted_vertices
                an_axis_projection_with_ids.append(a_shape)

            all_axis_projection_with_ids.append(an_axis_projection_with_ids)
        return all_axis_projection_with_ids

    @staticmethod
    def __parse_input(input):
        input_with_ids = Testers.__add_ids(input)
        return parse_two_D_projections(input_with_ids)

    @staticmethod
    def candidate_vertices(input,
                           expected_found_vertices_number: int = 0, expected_dandling_vertices_number: int = 0,
                           draw=False):
        parsed_input = Testers.__parse_input(input)
        found, dandling = find_candidate_vertices(parsed_input)

        print("\nFOUND \n")
        [print(f) for f in found]
        print("DANDLING \n")
        [print(f) for f in dandling]

        if draw:
            draw_3D_points_list([found, dandling])

        assert len(found) == expected_found_vertices_number, \
            f"{len(found)} vs {expected_found_vertices_number}"
        assert len(dandling) == expected_dandling_vertices_number, \
            f"{len(dandling)} vs {expected_dandling_vertices_number}"
