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
            'edges': {'1': {'id': '1', 'ancestorsIds': ['1', '5'], 'threeDPointsIds': ['10000', '10002']},
                      '2': {'id': '2', 'ancestorsIds': ['2', '6'], 'threeDPointsIds': ['10002', '10004']}},
            'vertices': {'10000': {'id': '10000', 'ancestorsIds': ['1', '3', '7'], 'x': 0.0, 'y': 0.0, 'z': 0.0},
                         '10002': {'id': '10002', 'ancestorsIds': ['2', '4', '7'], 'x': 0.0, 'y': 1.0, 'z': 0.0},
                         '10004': {'id': '10004', 'ancestorsIds': ['5', '6', '7'], 'x': 0.0, 'y': 4.0, 'z': 0.0}}},
        'dandling': {'edges': {}, 'vertices': {}}}

    assert result == expected


def test_small_square_e2e():
    result = two_D_to_three_D({
        'xy': {'1': {
            "vertices": {
                'v1': {'x': 0.0, 'y': 0.0, 'z': 0.0},
                'v2': {'x': 0.0, 'y': 1.0, 'z': 0.0},
                'v3': {'x': 0.0, 'y': 1.0, 'z': 1.0},
                'v4': {'x': 0.0, 'y': 0.0, 'z': 1.0},
            },
            "edges": {
                'e1': {'verticesIds': ['v1', 'v2']},
                'e2': {'verticesIds': ['v2', 'v3']},
                'e3': {'verticesIds': ['v3', 'v4']},
                'e4': {'verticesIds': ['v3', 'v1']},
            },
            "type": "polygon",
        }},
        'yz': {'2': {
            "vertices": {
                'v11': {'x': 0.0, 'y': 0.0, 'z': 0.0},
                'v12': {'x': 0.0, 'y': 1.0, 'z': 0.0},
                'v13': {'x': 0.0, 'y': 1.0, 'z': 1.0},
                'v14': {'x': 0.0, 'y': 0.0, 'z': 1.0},
            },
            "edges": {
                'e11': {'verticesIds': ['v11', 'v12']},
                'e12': {'verticesIds': ['v12', 'v13']},
                'e13': {'verticesIds': ['v13', 'v14']},
                'e14': {'verticesIds': ['v13', 'v11']},
            },
            "type": "polygon",
        }},
        'xz': {'3': {
            "vertices": {
                'v21': {'x': 0.0, 'y': 0.0, 'z': 0.0},
                'v22': {'x': 1.0, 'y': 0.0, 'z': 0.0},
                'v23': {'x': 1.0, 'y': 0.0, 'z': 1.0},
                'v24': {'x': 0.0, 'y': 0.0, 'z': 1.0},
            },
            "edges": {
                'e21': {'verticesIds': ['v21', 'v22']},
                'e22': {'verticesIds': ['v22', 'v23']},
                'e23': {'verticesIds': ['v23', 'v24']},
                'e24': {'verticesIds': ['v23', 'v21']},
            },
            "type": "polygon",
        }}
    })

    expected = {
        'reconstructed': {
            'edges': {'1': {'id': '1', 'ancestorsIds': ['1', '5'], 'threeDPointsIds': ['10000', '10002']},
                      '2': {'id': '2', 'ancestorsIds': ['2', '6'], 'threeDPointsIds': ['10002', '10004']}},
            'vertices': {'10000': {'id': '10000', 'ancestorsIds': ['1', '3', '7'], 'x': 0.0, 'y': 0.0, 'z': 0.0},
                         '10002': {'id': '10002', 'ancestorsIds': ['2', '4', '7'], 'x': 0.0, 'y': 1.0, 'z': 0.0},
                         '10004': {'id': '10004', 'ancestorsIds': ['5', '6', '7'], 'x': 0.0, 'y': 4.0, 'z': 0.0}}},
        'dandling': {'edges': {}, 'vertices': {}}}

    assert result == expected
