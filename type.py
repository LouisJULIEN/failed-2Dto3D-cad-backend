from typing import TypedDict, Dict, Tuple

from superclasses import PointWithId, LineStringWithId


class AnEdge(TypedDict):
    verticesIds: Tuple[str, str]


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
    edges: Dict[str, LineStringWithId]
    vertices: Dict[str, PointWithId]
    type: str


class Parsed2DProjections(TypedDict):
    xy: Dict[str, AParsedShape]  # shapeId -> shapeData (for projections face = shape)
    xz: Dict[str, AParsedShape]
    yz: Dict[str, AParsedShape]


Reconstructed3DVertices = Dict[str, PointWithId]
Reconstructed3DEdges = Dict[str, LineStringWithId]


class PointWithIdOutput(TypedDict):
    id: str
    x: float
    y: float
    z: float
    twoDAncestorsIds: list


class LineStringWithIdOutput(TypedDict):
    id: str
    twoDAncestorsIds: list
    verticesIds: list


class ReconstructedGeometry(TypedDict):
    vertices: Dict[str, PointWithIdOutput]
    edges: Dict[str, LineStringWithIdOutput]


class Reconstructed3DModel(TypedDict):
    reconstructed: ReconstructedGeometry
    dandling: ReconstructedGeometry
