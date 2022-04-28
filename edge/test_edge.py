from testers_edge import TestersEdge


def test_two_points():
    TestersEdge.reconstruct_edges({
        'xy': {1: {
            "vertices": {
                1: (0.0, 0.0, 0.0),
                2: (0.0, 1.0, 0.0)
            },
            "edges": {
                1: (1, 2)
            },
            "type": "polygon"
        }},
        'yz': {2: {
            "vertices": {
                3: (0.0, 0.0, 0.0),
                4: (0.0, 1.0, 0.0)
            },
            "edges": {
                5: (3, 4)
            },
            "type": "polygon"
        }},
        'xz': {}
    }, {
        10: [1, 3],
        11: [2, 4],
    }, [[10, 11]])


def skip_test_three_points():
    pass
