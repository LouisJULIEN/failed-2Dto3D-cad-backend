from edge.testers_edge import TestersEdge


def test_two_points():
    TestersEdge.reconstruct_edges({
        'xy': {
            "vertices": {
                '1': {'x': 0.0, 'y': 0.0, 'z': 0.0},
                '2': {'x': 0.0, 'y': 1.0, 'z': 0.0}
            },
            "edges": {
                '1': {'verticesIds': ['1', '2']}
            },
            "type": "polygon"
        },
        'yz': {
            "vertices": {
                '3': {'x': 0.0, 'y': 0.0, 'z': 0.0},
                '4': {'x': 0.0, 'y': 1.0, 'z': 0.0},
            },
            "edges": {
                '5': {'verticesIds': ['3', '4']}
            },
            "type": "polygon",
        },
        'xz': {
            "vertices": {},
            "edges": {},
            "type": "polygon",
        }
    }, {
        '10': {
            'coords': [0.0, 0.0, 0.0],
            'ancestors': ['1', '3']
        },
        '11': {
            'coords': [0.0, 1.0, 0.0],
            'ancestors': ['2', '4']
        }
    }, [['10', '11']])


def test_three_points_two_vertices():
    TestersEdge.reconstruct_edges({
        'xy': {
            "vertices": {
                '1': {'x': 0.0, 'y': 0.0, 'z': 0.0},
                '2': {'x': 0.0, 'y': 1.0, 'z': 0.0},
                '5': {'x': 0.0, 'y': 4.0, 'z': 0.0},
            },
            "edges": {
                '1': {'verticesIds': ['1', '2']},
                '2': {'verticesIds': ['2', '5']},
            },
            "type": "polygon"
        },
        'yz': {
            "vertices": {
                '3': {'x': 0.0, 'y': 0.0, 'z': 0.0},
                '4': {'x': 0.0, 'y': 1.0, 'z': 0.0},
                '6': {'x': 0.0, 'y': 4.0, 'z': 0.0},
            },
            "edges": {
                '5': {'verticesIds': ['3', '4']},
                '6': {'verticesIds': ['4', '6']},
            },
            "type": "polygon"
        },
        'xz': {
            "vertices": {},
            "edges": {},
            "type": "polygon",
        }
    }, {
        '10': {
            'ancestors': ['1', '3'],
            'coords': [0.0, 0.0, 0.0],
        },
        '11': {
            'ancestors': ['2', '4'],
            'coords': [0.0, 1.0, 0.0],
        },
        '12': {
            'ancestors': ['5', '6'],
            'coords': [0.0, 4.0, 0.0],
        }
    }, [['10', '11'], ['11', '12']])
