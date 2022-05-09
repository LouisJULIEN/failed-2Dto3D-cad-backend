from main import two_D_to_three_D


def test_three_points_two_vertices_e2e():
    result = two_D_to_three_D({
        'xy': {'1': {
            "vertices": {
                '1': {'x': 0.0, 'y': 0.0, 'z': 0.0},
                '2': {'x': 0.0, 'y': 1.0, 'z': 0.0},
                '5': {'x': 0.0, 'y': 4.0, 'z': 0.0},
            },
            "edges": {
                '1': {'verticesIds': ['1', '2']},
                '2': {'verticesIds': ['2', '5']},
            },
            "type": "polygon",
        }},
        'yz': {'2': {
            "vertices": {
                '3': {'x': 0.0, 'y': 0.0, 'z': 0.0},
                '4': {'x': 0.0, 'y': 1.0, 'z': 0.0},
                '6': {'x': 0.0, 'y': 4.0, 'z': 0.0},
            },
            "edges": {
                '5': {'verticesIds': ['3', '4']},
                '6': {'verticesIds': ['4', '6']},
            },
            "type": "polygon",
        }},
        'xz': {'3': {
            "vertices": {
                '7': {'x': 0.0, 'y': 0.0, 'z': 0.0},
            },
            "edges": {},
            "type": "polygon",
        }}
    })
    expected = {
        'reconstructed': {
            'edges': {'1': {'id': '1', 'ancestorsIds': ['1'], 'threeDPointsIds': ['10000', '10002']},
                      '2': {'id': '2', 'ancestorsIds': ['2'], 'threeDPointsIds': ['10002', '10004']}},
            'vertices': {'10000': {'id': '10000', 'ancestorsIds': ['1', '3', '7'], 'x': 0.0, 'y': 0.0, 'z': 0.0},
                         '10002': {'id': '10002', 'ancestorsIds': ['2', '4', '7'], 'x': 0.0, 'y': 1.0, 'z': 0.0},
                         '10004': {'id': '10004', 'ancestorsIds': ['5', '6', '7'], 'x': 0.0, 'y': 4.0, 'z': 0.0}}},
        'dandling': {'edges': {}, 'vertices': {}}}

    assert result == expected
