from math import sqrt

from shapely.geometry import Point, LineString, Polygon


# TODO: separate projected and 3D classes
# TODO: switch to vanilla classes
# TODO: rename links to better name (twoDAncestors)

class AncestorWithId:
    def __init__(self, _id: str):
        self.id = _id
        self.ancestors = set()

    def __hash__(self):
        return hash(self.id)

    def __eq__(self, other):
        return self.id == other.id

    def __ne__(self, other):
        return not self.__eq__(other)

    def attach_to_ancestor(self, new_link):
        self.ancestors.add(new_link)

    def attach_to_multiple_ancestors(self, new_links: list):
        self.ancestors.update(new_links)

    def has_no_ancestor(self) -> bool:
        return len(self.ancestors) == 0

    def remove_ancestor(self, link_to_remove):
        self.ancestors.remove(link_to_remove)


class PointWithId(AncestorWithId, Point):
    def __init__(self, _id, *args):
        Point.__init__(self, *args)
        AncestorWithId.__init__(self, _id)

    def __str__(self):
        ancestors_ids = [f"{l.id} {list(l.coords)}" for l in self.ancestors]
        return f"{list(self.coords)} with id {self.id} linked to {ancestors_ids}"

    def distance(self, other) -> float:
        # shapely is a 2D library
        return sqrt((self.x - other.x) ** 2 + (self.y - other.y) ** 2 + (self.z - other.z) ** 2)

    def export(self):
        return {
            'id': self.id,
            'ancestorsIds': sorted([a.id for a in self.ancestors]),
            'x': self.x,
            'y': self.y,
            'z': self.z,
        }


class LineStringWithId(AncestorWithId, LineString):
    def __init__(self, _id, *args, **kwargs):
        LineString.__init__(self, *args, **kwargs)
        AncestorWithId.__init__(self, _id)
        self.three_D_points = tuple(args[0])  # the id of the start and end points.

    def export(self):
        return {
            'id': self.id,
            'ancestorsIds': sorted([a.id for a in self.ancestors]),
            'threeDPointsIds': sorted([pt.id for pt in self.three_D_points]),
        }


class PolygonWithId(AncestorWithId, Polygon):
    def __init__(self, _id, *args, **kwargs):
        Polygon.__init__(self, *args, **kwargs)
        AncestorWithId.__init__(self, _id)
