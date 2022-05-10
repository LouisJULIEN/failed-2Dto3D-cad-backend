from typing import Dict

from superclasses import ThreeDLineStringWithId, ProjectedLineStringWithId
from type import Parsed2DProjections, Reconstructed3DVertices, Reconstructed3DEdges


def reconstruct_edges(parsed_projections: Parsed2DProjections, reconstructed_3d_points: Reconstructed3DVertices
                      ) -> (Reconstructed3DEdges, Reconstructed3DEdges):
    all_edges_projections: Dict[str, ProjectedLineStringWithId] = {}
    for a_projection in parsed_projections.values():
        for a_shape in a_projection.values():
            all_edges_projections.update(a_shape['edges'])

    reconstruct_edge_id = '100000'

    reconstructed_edges = {}
    for an_edge_projection_id, an_edge_projection in all_edges_projections.items():
        # we do the cross product of all possible 3D point. The extra vertices are deleted afterwards
        edge_3D_points_couple = []
        for three_d_pt_first in an_edge_projection.two_D_points[0].ancestors:
            for three_d_pt_second in an_edge_projection.two_D_points[1].ancestors:
                edge_3D_points_couple.append((three_d_pt_first, three_d_pt_second))

        # sort 3D_points by id to enhance stability
        edge_3D_points_couple.sort(key=lambda x: (x[0].id, x[1].id))

        for a_3D_pt_couple in edge_3D_points_couple:
            reconstructed_edges[reconstruct_edge_id] = ThreeDLineStringWithId(reconstruct_edge_id,
                                                                              a_3D_pt_couple)
            reconstructed_edges[reconstruct_edge_id].attach_to_ancestor(all_edges_projections[an_edge_projection_id])
            all_edges_projections[an_edge_projection_id].attach_to_ancestor(reconstructed_edges[reconstruct_edge_id])

            reconstruct_edge_id = str(int(reconstruct_edge_id) + 1)

    # remove duplicates i.e. edges with the exact same three_D_points
    def get_vertices_ids(edge):
        return [pt.id for pt in edge.three_D_points]

    reconstructed_edges_list = list(reconstructed_edges.values())
    reconstructed_edges_list.sort(key=get_vertices_ids)

    print('found ', len(reconstructed_edges_list))
    for i in range(len(reconstructed_edges_list) - 1):
        if get_vertices_ids(reconstructed_edges_list[i]) == get_vertices_ids(reconstructed_edges_list[i + 1]):
            reconstructed_edges_list[i].attach_to_multiple_ancestors(reconstructed_edges_list[i + 1].ancestors)

            print('removing redundant edge ', reconstructed_edges_list[i].three_D_points)

            for a_projected_edge in reconstructed_edges_list[i + 1].ancestors:
                a_projected_edge.remove_ancestor(reconstructed_edges_list[i + 1])
                a_projected_edge.attach_to_ancestor(reconstructed_edges_list[i])

            del reconstructed_edges[reconstructed_edges_list[i + 1].id]

    # TODO: remove edges that are not coherent

    return reconstructed_edges, {}
