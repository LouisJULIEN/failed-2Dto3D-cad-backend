from type import Raw2DProjections


def validateTwoDProjections(two_d_projections: Raw2DProjections) -> bool:
    for an_axis_projection, shapes in two_d_projections.items():
        assert an_axis_projection in ('xy', 'xz', 'yz')
        # TODO: check that axis really is constant

        for a_shape in shapes.values():
            assert a_shape["type"] in ("polygon")
    return True
