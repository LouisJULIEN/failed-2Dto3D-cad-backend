from typing import TypedDict, Dict, List

from superclasses import ProjectedLineStringWithId, ThreeDLineStringWithId, TwoDPoint, ThreeDPoint


class AnEdge(TypedDict):
    verticesIds: List[str]


class AVertex(TypedDict):
    x: float
    y: float
    z: float


class Raw2DShape(TypedDict):
    # a shape is made up of vertices linked by edges. Edges can be cyclic or acyclic, joint or disjointed.
    type: str
    vertices: Dict[str, AVertex]
    edges: Dict[str, AnEdge]


Raw2DProjections = Dict[str, Raw2DShape]  # projection[axes] -> shape[id] -> [edge, vertices, faces]


class AParsedShape(TypedDict):
    edges: Dict[str, ProjectedLineStringWithId]
    vertices: Dict[str, TwoDPoint]
    type: str


class Parsed2DProjections(TypedDict):
    xy: AParsedShape
    xz: AParsedShape
    yz: AParsedShape


Reconstructed3DVertices = Dict[str, ThreeDPoint]
Reconstructed3DEdges = Dict[str, ThreeDLineStringWithId]
DandlingEdges = Dict[str, ProjectedLineStringWithId]


class DandlingGeometry(TypedDict):
    vertices: Reconstructed3DVertices
    edges: DandlingEdges


class ReconstructedGeometry(TypedDict):
    vertices: Reconstructed3DVertices
    edges: Reconstructed3DEdges


class Reconstructed3DModel(TypedDict):
    reconstructed: ReconstructedGeometry
    dandling: DandlingGeometry


class ExportedPoint:
    id: str
    ancestorsIds: List[str]
    x: float
    y: float
    z: float


class ExportedLine:
    id: str
    ancestorsIds: List[str]
    threeDPointsIds: List[str]


class ExportedReconstructedGeometry(TypedDict):
    vertices: Dict[str, ExportedPoint]
    edges: Dict[str, ExportedLine]


class ExportedReconstructed3DModel(TypedDict):
    reconstructed: ExportedReconstructedGeometry
    dandling: ExportedReconstructedGeometry
