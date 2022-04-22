from edge.testers_edge import TestersEdge


def test_two_points():
    TestersEdge.reconstruct_vertices({
        "vertices": {
            1: (0.0, 0.0, 0.0),
            2: (0.0, 1.0, 0.0)
        },
        "edges": {
            1: (1, 2)
        }
    }, {
        1: (1, 2)
    })
