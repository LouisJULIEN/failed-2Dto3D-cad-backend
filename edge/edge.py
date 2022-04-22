from type import AParsedProjection, parsed_2D_projections, Reconstructed3DPoints


def reconstruct_edges(parsed_projections: parsed_2D_projections, reconstructed_3d_points: Reconstructed3DPoints):
    all_edges_projections = []
    for a_projection in parsed_projections:
        all_edges_projections.append(a_projection['edges'])
