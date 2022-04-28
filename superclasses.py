from math import sqrt

from shapely.geometry import Point, LineString, Polygon


# TODO: separate projected and 3D classes
# TODO: switch to vanilla classes

class LinkedWithId:
    def __init__(self, _id):
        self.id = _id
        self.links = set()

    def __hash__(self):
        return self.id

    def __eq__(self, other):
        return self.id == other.id

    def __ne__(self, other):
        return not self.__eq__(other)

    def link_to(self, new_link):
        self.links.add(new_link)

    def link_to_multiples(self, new_links: list):
        self.links.update(new_links)

    def is_linked_to_none(self) -> bool:
        return len(self.links) == 0

    def remove_link(self, link_to_remove):
        self.links.remove(link_to_remove)


class PointWithId(LinkedWithId, Point):
    def __init__(self, _id, *args):
        Point.__init__(self, *args)
        LinkedWithId.__init__(self, _id)

    def __str__(self):
        ids_linked_to = [f"{l.id} {list(l.coords)}" for l in self.links]
        return f"{list(self.coords)} with id {self.id} linked to {ids_linked_to}"

    def distance(self, other) -> float:
        # shapely is a 2D library
        return sqrt((self.x - other.x) ** 2 + (self.y - other.y) ** 2 + (self.z - other.z) ** 2)


class LineStringWithId(LinkedWithId, LineString):
    def __init__(self, _id, *args, **kwargs):
        LineString.__init__(self, *args, **kwargs)
        LinkedWithId.__init__(self, _id)
        self.three_D_points = tuple(args[0]) # the id of the start and end points.


class PolygonWithId(LinkedWithId, Polygon):
    def __init__(self, _id, *args, **kwargs):
        Polygon.__init__(self, *args, **kwargs)
        LinkedWithId.__init__(self, _id)
