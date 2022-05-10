from math import sqrt

from shapely.geometry import Point, LineString


class AncestorWithId:
    def __init__(self, _id: str, ancestor_class=object):
        self.id = _id
        self.ancestors = set()
        self.ancestors_class = ancestor_class

    def __hash__(self):
        return hash(self.id)

    def __eq__(self, other):
        return self.id == other.id

    def __ne__(self, other):
        return not self.__eq__(other)

    def attach_to_ancestor(self, new_link):
        assert isinstance(new_link, self.ancestors_class)
        self.ancestors.add(new_link)

    def attach_to_multiple_ancestors(self, new_links: list):
        for a_new_link in new_links:
            assert isinstance(a_new_link, self.ancestors_class)

        self.ancestors.update(new_links)

    def has_no_ancestor(self) -> bool:
        return len(self.ancestors) == 0

    def remove_ancestor(self, link_to_remove):
        assert isinstance(link_to_remove, self.ancestors_class)
        self.ancestors.remove(link_to_remove)


class __PointWithId(AncestorWithId, Point):
    def __init__(self, _id, *args):
        Point.__init__(self, *args)
        AncestorWithId.__init__(self, _id, ancestor_class=__PointWithId)

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


class ThreeDPoint(__PointWithId):
    def __init__(self, _id, *args):
        Point.__init__(self, *args)
        AncestorWithId.__init__(self, _id, ancestor_class=TwoDPoint)


class TwoDPoint(__PointWithId):
    def __init__(self, _id, *args):
        Point.__init__(self, *args)
        AncestorWithId.__init__(self, _id, ancestor_class=ThreeDPoint)


class ProjectedLineStringWithId(AncestorWithId, LineString):
    def __init__(self, _id, *args, **kwargs):
        LineString.__init__(self, *args, **kwargs)
        AncestorWithId.__init__(self, _id, ancestor_class=ThreeDLineStringWithId)
        self.two_D_points = tuple(args[0])  # the id of the start and end points.

    def export(self):
        return {
            'id': self.id,
            'ancestorsIds': sorted([a.id for a in self.ancestors]),
            'twoDPointsIds': sorted([pt.id for pt in self.two_D_points]),
        }

    def __str__(self):
        two_d_points = sorted([f"{pt.id} at ({pt.x};{pt.y};{pt.z})" for pt in self.two_D_points])
        return f"2D edge {self.id} with points {two_d_points}"


class ThreeDLineStringWithId(AncestorWithId, LineString):
    def __init__(self, _id, *args, **kwargs):
        LineString.__init__(self, *args, **kwargs)
        AncestorWithId.__init__(self, _id, ancestor_class=ProjectedLineStringWithId)
        self.three_D_points = tuple(args[0])  # the id of the start and end points.

    def export(self):
        return {
            'id': self.id,
            'ancestorsIds': sorted([a.id for a in self.ancestors]),
            'threeDPointsIds': sorted([pt.id for pt in self.three_D_points]),
        }

    def __str__(self):
        three_d_points = sorted([f"{pt.id} at ({pt.x};{pt.y};{pt.z})" for pt in self.three_D_points])
        return f"3D edge {self.id} with points {three_d_points}"
