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
            'edges': {'100000': {'ancestorsIds': ['1', '5'],
                                 'id': '100000',
                                 'threeDPointsIds': ['10000', '10002']},
                      '100001': {'ancestorsIds': ['2', '6'],
                                 'id': '100001',
                                 'threeDPointsIds': ['10002', '10004']}},
            'vertices': {
                '10000': {'id': '10000', 'ancestorsIds': ['1', '3', '7'], 'x': 0.0, 'y': 0.0, 'z': 0.0},
                '10002': {'id': '10002', 'ancestorsIds': ['2', '4', '7'], 'x': 0.0, 'y': 1.0, 'z': 0.0},
                '10004': {'id': '10004', 'ancestorsIds': ['5', '6', '7'], 'x': 0.0, 'y': 4.0, 'z': 0.0}}},
        'dandling': {'edges': {}, 'vertices': {}}}

    assert result == expected


def test_small_square_e2e():
    result = two_D_to_three_D({
        'xy': {'1': {
            "vertices": {
                'v1': {'x': 0.0, 'y': 0.0, 'z': 0.0},
                'v2': {'x': 1.0, 'y': 0.0, 'z': 0.0},
                'v3': {'x': 1.0, 'y': 1.0, 'z': 0.0},
                'v4': {'x': 0.0, 'y': 1.0, 'z': 0.0},
            },
            "edges": {
                'e1': {'verticesIds': ['v1', 'v2']},
                'e2': {'verticesIds': ['v2', 'v3']},
                'e3': {'verticesIds': ['v3', 'v4']},
                'e4': {'verticesIds': ['v4', 'v1']},
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
                'e14': {'verticesIds': ['v14', 'v11']},
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
                'e24': {'verticesIds': ['v24', 'v21']},
            },
            "type": "polygon",
        }}
    })

    # should have 12 edges
    expected = {'dandling': {'edges': {}, 'vertices': {}},
                'reconstructed': {
                    'edges': {'100000': {'ancestorsIds': ['e1', 'e21'],
                                         'id': '100000',
                                         'threeDPointsIds': ['10000', '10018']},
                              '100003': {'ancestorsIds': ['e1', 'e23'],
                                         'id': '100003',
                                         'threeDPointsIds': ['10014', '10028']},
                              '100004': {'ancestorsIds': ['e11', 'e2'],
                                         'id': '100004',
                                         'threeDPointsIds': ['10018', '10034']},
                              '100007': {'ancestorsIds': ['e13', 'e2'],
                                         'id': '100007',
                                         'threeDPointsIds': ['10028', '10044']},
                              '100008': {'ancestorsIds': ['e21', 'e3'],
                                         'id': '100008',
                                         'threeDPointsIds': ['10034', '10048']},
                              '100011': {'ancestorsIds': ['e23', 'e3'],
                                         'id': '100011',
                                         'threeDPointsIds': ['10044', '10062']},
                              '100012': {'ancestorsIds': ['e11', 'e4'],
                                         'id': '100012',
                                         'threeDPointsIds': ['10000', '10048']},
                              '100015': {'ancestorsIds': ['e13', 'e4'],
                                         'id': '100015',
                                         'threeDPointsIds': ['10014', '10062']},
                              '100020': {'ancestorsIds': ['e12', 'e22'],
                                         'id': '100020',
                                         'threeDPointsIds': ['10034', '10044']},
                              '100023': {'ancestorsIds': ['e12', 'e24'],
                                         'id': '100023',
                                         'threeDPointsIds': ['10048', '10062']},
                              '100028': {'ancestorsIds': ['e14', 'e24'],
                                         'id': '100028',
                                         'threeDPointsIds': ['10000', '10014']},
                              '100031': {'ancestorsIds': ['e14', 'e22'],
                                         'id': '100031',
                                         'threeDPointsIds': ['10018', '10028']}},
                    'vertices': {'10000': {'ancestorsIds': ['v1', 'v11', 'v21'],
                                           'id': '10000',
                                           'x': 0.0,
                                           'y': 0.0,
                                           'z': 0.0},
                                 '10014': {'ancestorsIds': ['v1', 'v14', 'v24'],
                                           'id': '10014',
                                           'x': 0.0,
                                           'y': 0.0,
                                           'z': 1.0},
                                 '10018': {'ancestorsIds': ['v11', 'v2', 'v22'],
                                           'id': '10018',
                                           'x': 1.0,
                                           'y': 0.0,
                                           'z': 0.0},
                                 '10028': {'ancestorsIds': ['v14', 'v2', 'v23'],
                                           'id': '10028',
                                           'x': 1.0,
                                           'y': 0.0,
                                           'z': 1.0},
                                 '10034': {'ancestorsIds': ['v12', 'v22', 'v3'],
                                           'id': '10034',
                                           'x': 1.0,
                                           'y': 1.0,
                                           'z': 0.0},
                                 '10044': {'ancestorsIds': ['v13', 'v23', 'v3'],
                                           'id': '10044',
                                           'x': 1.0,
                                           'y': 1.0,
                                           'z': 1.0},
                                 '10048': {'ancestorsIds': ['v12', 'v21', 'v4'],
                                           'id': '10048',
                                           'x': 0.0,
                                           'y': 1.0,
                                           'z': 0.0},
                                 '10062': {'ancestorsIds': ['v13', 'v24', 'v4'],
                                           'id': '10062',
                                           'x': 0.0,
                                           'y': 1.0,
                                           'z': 1.0}}}}

    assert result == expected
