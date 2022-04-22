from graphics import draw_3D_points_list
from parse import parse_two_D_projections
from vertex import reconstruct_vertices


class TestersVertex:
    id_number = 0

    @staticmethod
    def __add_ids(input):
        all_axis_projection_with_ids = []
        for an_axis_projection in input:
            an_axis_projection_with_ids = []

            for a_shape in an_axis_projection:
                a_shape['id'] = TestersVertex.id_number
                TestersVertex.id_number += 1

                formatted_vertices = {}
                for a_point in a_shape["vertices"]:
                    formatted_vertices[TestersVertex.id_number] = a_point
                    TestersVertex.id_number += 1

                a_shape["vertices"] = formatted_vertices
                a_shape["edges"] = {}
                an_axis_projection_with_ids.append(a_shape)

            all_axis_projection_with_ids.append(an_axis_projection_with_ids)
        return all_axis_projection_with_ids

    @staticmethod
    def __parse_input(input):
        input_with_ids = TestersVertex.__add_ids(input)
        return parse_two_D_projections(input_with_ids)

    @staticmethod
    def reconstruct_vertices(input,
                             expected_found_vertices_number: int = 0, expected_dandling_vertices_number: int = 0,
                             draw=False):
        parsed_input = TestersVertex.__parse_input(input)
        found, dandling = reconstruct_vertices(parsed_input)

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
