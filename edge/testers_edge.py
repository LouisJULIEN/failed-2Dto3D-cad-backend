from vertex.vertex import reconstruct_vertices


class TestersEdge:
    id_number = 0

    @staticmethod
    def reconstruct_vertices(input, expected_vertices):
        reconstruct_vertices(input)
