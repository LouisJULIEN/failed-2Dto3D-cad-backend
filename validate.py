def validateTwoDProjections(two_d_projections: list) -> bool:
    for an_axis_projection in two_d_projections:
        for a_projection in an_axis_projection:
            assert a_projection["constAxis"] in ("x", "y", "z")
            # TODO: check it really is constant
            assert a_projection["type"] in ("polygon")
    return True
