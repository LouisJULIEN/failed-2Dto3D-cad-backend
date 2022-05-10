from typing import Dict

from superclasses import ThreeDLineStringWithId, ProjectedLineStringWithId
from type import Parsed2DProjections, Reconstructed3DVertices, Reconstructed3DEdges


def reconstruct_edges(parsed_projections: Parsed2DProjections, reconstructed_3d_points: Reconstructed3DVertices
                      ) -> (Reconstructed3DEdges, Reconstructed3DEdges):
    all_edges_projections: Dict[str, ProjectedLineStringWithId] = {}
    for a_projection in parsed_projections.values():
        for a_shape in a_projection.values():
            all_edges_projections.update(a_shape['edges'])

    reconstructed_edges = {}
    for an_edge_projection_id, an_edge_projection in all_edges_projections.items():
        # projected vertex have only one ancestor, the 3D point
        # we assume everything is consistent
        reconstructed_edge_3D_points = [
            list(a_projected_vertex_of_edge.ancestors)[0] for a_projected_vertex_of_edge in an_edge_projection.ancestors
        ]

        # sort 3D_points by id to enhance stability
        reconstructed_edge_3D_points.sort(key=lambda x: x.id)

        reconstructed_edges[an_edge_projection_id] = ThreeDLineStringWithId(an_edge_projection_id,
                                                                            reconstructed_edge_3D_points)
        reconstructed_edges[an_edge_projection_id].attach_to_ancestor(all_edges_projections[an_edge_projection_id])
        # TODO: add link projected vertex to reconstructed vertex

    def get_vertices_ids(edge):
        return [pt.id for pt in edge.three_D_points]

    # remove duplicates
    reconstructed_edges_list = list(reconstructed_edges.values())
    reconstructed_edges_list.sort(key=get_vertices_ids)

    for i in range(len(reconstructed_edges_list) - 1):
        if get_vertices_ids(reconstructed_edges_list[i]) == get_vertices_ids(reconstructed_edges_list[i + 1]):
            reconstructed_edges_list[i].attach_to_multiple_ancestors(reconstructed_edges_list[i + 1].ancestors)

            # move for projected edge too
            # for a_projected_edge in reconstructed_edges_list[i + 1].ancestors:
            #     a_projected_edge.remove_ancestor(reconstructed_edges_list[i + 1])
            #     a_projected_edge.attach_to_ancestor(reconstructed_edges_list[i])

            del reconstructed_edges[reconstructed_edges_list[i + 1].id]

    return reconstructed_edges, {}
