from vertex.testers_vertex import TestersVertex


def test_dandling():
    TestersVertex.reconstruct_vertices({
        'xy': {

            'type': "polygon",
            "vertices": [(3.0, 3.0, 3.0)]
        },
        'yz': {
            'type': "polygon",
            "vertices": [(2.0, 2.0, 2.0)]
        },
        'xz': {
            'type': "polygon",
            "vertices": [(1.0, 1.0, 1.0)]
        },
    }, expected_dandling_vertices_number=3)


def test_parallelepiped():
    # a 2 x 1 x 3 parallelepiped
    TestersVertex.reconstruct_vertices({
        'xy': {
            'type': "polygon",
            "vertices": [(0.0, 0.0, 3.0), (0.0, 1.0, 3.0), (2.0, 1.0, 3.0), (2.0, 0.0, 3.0)]
        },
        'yz': {
            'type': "polygon",
            "vertices": [(0.0, 0.0, 0.0), (0.0, 0.0, 3.0), (0.0, 1.0, 3.0), (0.0, 1.0, 0.0)],
        },
        'xz': {
            'type': "polygon",
            "vertices": [(0.0, 0.0, 0.0), (0.0, 0.0, 3.0), (2.0, 0.0, 3.0), (2.0, 0.0, 0.0)]
        },
    }, 8)

