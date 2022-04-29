from type import Raw2DProjections


def validateTwoDProjections(two_d_projections: Raw2DProjections) -> bool:
    for an_axis_projection, shapes in two_d_projections.items():
        # TODO: check that axis really is constant
    return True
