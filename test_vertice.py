from testers import Testers


def test_parallelepiped():
    # a 2 x 1 x 3 parallelepiped
    Testers.candidate_vertices([
        [{
            'type': "polygon",
            "constAxis": "z",
            "vertices": [(0.0, 0.0, 3.0), (0.0, 1.0, 3.0), (2.0, 1.0, 3.0), (2.0, 0.0, 3.0)]}],
        # X;Y with Z=3
        [{
            'type': "polygon",
            "constAxis": "x",
            "vertices": [(0.0, 0.0, 0.0), (0.0, 0.0, 3.0), (0.0, 1.0, 3.0), (0.0, 1.0, 0.0)]}],
        # Y;Z with X=0
        [{
            'type': "polygon",
            "constAxis": "y",
            "vertices": [(0.0, 0.0, 0.0), (0.0, 0.0, 3.0), (2.0, 0.0, 3.0), (2.0, 0.0, 0.0)]
        }],
        # X;Z with Y=0
    ], 8)


def skip_test_home_shape():
    Testers.candidate_vertices([
        [{
            'type': "polygon",
            "constAxis": "z",
            "vertices": [(0.0, 0.0, 0.0), (0.0, 2.0, 0.0), (2.0, 2.0, 0.0),
                         (3.0, 2.0, 0.0), (3.0, 0.0, 0.0), (2.0, 0.0, 0.0)]
        }],
        # X;Y with Z=0
        [{
            'type': "polygon",
            "constAxis": "x",
            "vertices": [(3.0, 0.0, 0.0), (3.0, 0.0, 5.0), (3.0, 2.0, 5.0), (3.0, 2.0, 0.0)]
        }],
        # Y;Z with X=3
        [{
            'type': "polygon",
            "constAxis": "y",
            "vertices": [(0.0, 0.0, 0.0), (0.0, 0.0, 4.0), (2.0, 0.0, 4.0), (3.0, 0.0, 5.0), (3.0, 0.0, 0.0)]
        }],
        # X;Z with Y=0
    ], 10)
