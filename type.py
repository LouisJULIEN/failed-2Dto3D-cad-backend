from typing import TypedDict, Dict, Tuple

from superclasses import PointWithId, LineStringWithId


class Raw2DShape(TypedDict):
    type: str
    vertices: Dict[int, tuple]
    edges: Dict[int, Tuple[int, int]]


Raw2DProjections = Dict[str, Dict[int, Raw2DShape]]  # projection[axes] -> shape[id] -> [edge, vertices, faces]


class AParsedShape(TypedDict):
    edges: Dict[int, LineStringWithId]
    vertices: Dict[int, PointWithId]
    type: str


class Parsed2DProjections(TypedDict):
    xy: Dict[int, AParsedShape]  # shapeId -> shapeData (for projections face = shape)
    xz: Dict[int, AParsedShape]
    yz: Dict[int, AParsedShape]


Reconstructed3DPoints = Dict[int, PointWithId]
Reconstructed3DEdges = Dict[int, LineStringWithId]
