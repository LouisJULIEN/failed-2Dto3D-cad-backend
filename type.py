from typing import TypedDict, Dict, List

from superclasses import PointWithId, ProjectedLineStringWithId, ThreeDLineStringWithId


class AnEdge(TypedDict):
    verticesIds: List[str]


class AVertex(TypedDict):
    x: float
    y: float
    z: float


class Raw2DShape(TypedDict):
    type: str
    vertices: Dict[str, AVertex]
    edges: Dict[str, AnEdge]


Raw2DProjections = Dict[str, Dict[str, Raw2DShape]]  # projection[axes] -> shape[id] -> [edge, vertices, faces]


class AParsedShape(TypedDict):
    edges: Dict[str, ProjectedLineStringWithId]
    vertices: Dict[str, PointWithId]
    type: str


class Parsed2DProjections(TypedDict):
    xy: Dict[str, AParsedShape]  # shapeId -> shapeData (for projections face = shape)
    xz: Dict[str, AParsedShape]
    yz: Dict[str, AParsedShape]


Reconstructed3DVertices = Dict[str, PointWithId]
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
