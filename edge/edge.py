from type import Parsed2DProjections, Reconstructed3DPoints, Reconstructed3DEdges


def reconstruct_edges(parsed_projections: Parsed2DProjections, reconstructed_3d_points: Reconstructed3DPoints
                      ) -> Reconstructed3DEdges:
    all_edges_projections = {}
    for a_projection in parsed_projections.values():
        for a_shape in a_projection.values():
            all_edges_projections.update(a_shape['edges'])

    print()
    for an_edge_projection_id, an_edge_projection in all_edges_projections.items():
        for a_point_of_edge in an_edge_projection.links:
            print(an_edge_projection_id, a_point_of_edge.id, a_point_of_edge.links)

    return {}
