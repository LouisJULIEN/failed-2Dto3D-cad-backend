from type import Parsed2DProjections, Reconstructed3DPoints, Reconstructed3DEdges


def reconstruct_edges(parsed_projections: Parsed2DProjections, reconstructed_3d_points: Reconstructed3DPoints
                      ) -> Reconstructed3DEdges:
    all_edges_projections = []
    for a_projection in parsed_projections.values():
        for a_shape in a_projection.values():
            all_edges_projections.append(a_shape['edges'])

    print(all_edges_projections)

    return {}
