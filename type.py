from typing import TypedDict, Dict, Tuple

from superclasses import PointWithId, LineStringWithId


class AnEdge(TypedDict):
    vertexIds: Tuple[int, int]


class AVertex(TypedDict):
    x: int
    y: int


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


Reconstructed3DPoints = Dict[str, PointWithId]
Reconstructed3DEdges = Dict[str, LineStringWithId]
