from typing import Dict

from superclasses import PointWithId, LineStringWithId
from type import Reconstructed3DModel, ExportedPoint, ExportedLine


def export_reconstructed_model(reconstructed_model: Reconstructed3DModel):
    def export_edges(edges: Dict[str, LineStringWithId]) -> Dict[str, ExportedLine]:
        exported_edges = {}
        for (edge_id, edge) in edges.items():
            exported_edges[edge_id] = edge.export()
        return exported_edges

    def export_vertices(vertices: Dict[str, PointWithId]) -> Dict[str, ExportedPoint]:
        exported_vertices = {}
        for (vertex_id, vertex_object) in vertices.items():
            exported_vertices[vertex_id] = vertex_object.export()
        return exported_vertices

    return {
        **reconstructed_model,
        'reconstructed': {
            'edges': export_edges(reconstructed_model['reconstructed']['edges']),
            'vertices': export_vertices(reconstructed_model['reconstructed']['vertices']),
        },
        'dandling': {
            'edges': export_edges(reconstructed_model['dandling']['edges']),
            'vertices': export_vertices(reconstructed_model['dandling']['vertices']),
        },
    }
