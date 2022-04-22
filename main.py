from preprocess.parse import parse_two_D_projections
from type import Raw2DProjections
from preprocess.validate import validateTwoDProjections
from vertex.vertex import reconstruct_vertices


def two_D_to_three_D(two_D_projections: Raw2DProjections):
    assert validateTwoDProjections(two_D_projections), "invalid twoDProjections"
    parsed_two_D_projections = parse_two_D_projections(two_D_projections)

    candidate_vertices, dandling_points = reconstruct_vertices(parsed_two_D_projections)
    # draw_3D_points_list([candidate_vertices, dandling_points])
    print(f"candidate_vertices : {len(candidate_vertices)}, dandling_points : {len(dandling_points)}")

