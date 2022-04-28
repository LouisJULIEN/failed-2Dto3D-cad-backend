from superclasses import LineStringWithId
from type import Parsed2DProjections, Reconstructed3DPoints, Reconstructed3DEdges


def reconstruct_edges(parsed_projections: Parsed2DProjections, reconstructed_3d_points: Reconstructed3DPoints
                      ) -> Reconstructed3DEdges:
    all_edges_projections = {}
    for a_projection in parsed_projections.values():
        for a_shape in a_projection.values():
            all_edges_projections.update(a_shape['edges'])

    reconstructed_edges = {}
    for an_edge_projection_id, an_edge_projection in all_edges_projections.items():
        # projected vertex have only one link, the 3D point
        reconstructed_edge_3D_points = [
            list(a_projected_vertex_of_edge.links)[0] for a_projected_vertex_of_edge in an_edge_projection.links
        ]

        reconstructed_edges[an_edge_projection_id] = LineStringWithId(an_edge_projection_id,
                                                                      reconstructed_edge_3D_points)
        reconstructed_edges[an_edge_projection_id].link_to(all_edges_projections[an_edge_projection_id])
        # TODO: add link projected vertex to reconstructed vertex

    def get_vertices_ids(edge):
        return [pt.id for pt in edge.three_D_points]

    # remove duplicates
    reconstructed_edges_list = list(reconstructed_edges.values())
    reconstructed_edges_list.sort(key=get_vertices_ids)

    for i in range(len(reconstructed_edges_list) - 1):
        if get_vertices_ids(reconstructed_edges_list[i]) == get_vertices_ids(reconstructed_edges_list[i + 1]):
            del reconstructed_edges[reconstructed_edges_list[i + 1].id]
            # TODO: clean link projected vertex

    return reconstructed_edges
