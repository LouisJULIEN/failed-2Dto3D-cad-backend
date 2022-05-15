from preprocess.parse import parse_two_D_projections
from vertex.vertex import reconstruct_vertices


class TestersVertex:
    id_number = '0'

    @staticmethod
    def __reformat(input):
        for an_axis, a_shape in input.items():

            a_formatted_shape = {
                "edges": {},
                "vertices": {},
                "type": a_shape["type"]
            }
            for a_point in a_shape["vertices"]:
                a_formatted_shape["vertices"][TestersVertex.id_number] = {
                    'x': a_point[0],
                    'y': a_point[1],
                    'z': a_point[2],
                    'id': TestersVertex.id_number
                }
                TestersVertex.id_number = str(int(TestersVertex.id_number) + 1)
            input[an_axis] = a_formatted_shape

        return input

    @staticmethod
    def __parse_input(input):
        input_with_ids = TestersVertex.__reformat(input)
        return parse_two_D_projections(input_with_ids)

    @staticmethod
    def reconstruct_vertices(input,
                             expected_found_vertices_number: int = 0, expected_dandling_vertices_number: int = 0):
        parsed_input = TestersVertex.__parse_input(input)
        found, dandling = reconstruct_vertices(parsed_input)

        print("\nFOUND")
        [print(f) for f in found.values()]
        print("DANDLING")
        [print(f) for f in dandling.values()]

        assert len(found) == expected_found_vertices_number, \
            f"{len(found)} vs {expected_found_vertices_number}"
        assert len(dandling) == expected_dandling_vertices_number, \
            f"{len(dandling)} vs {expected_dandling_vertices_number}"
