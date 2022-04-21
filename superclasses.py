from shapely.geometry import Point, LineString, Polygon


class LinkedWithId:
    def __init__(self, _id):
        self.id = _id
        self.links = []

    def link_to(self, new_link):
        self.links.append(new_link)

    def link_to_multiples(self, *new_links):
        for a_new_link in new_links:
            self.links.append(a_new_link)

    def is_linked_to_none(self) -> bool:
        return len(self.links) == 0


class PointWithId(Point, LinkedWithId):
    def __init__(self, _id, *args):
        Point.__init__(self, *args)
        LinkedWithId.__init__(self, _id)

    def __str__(self):
        ids_linked_to = [f"{l.id} {list(l.coords)}" for l in self.links]
        return f"{list(self.coords)} with id {self.id} linked to {ids_linked_to}"


class LineStringWithId(LineString, LinkedWithId):
    def __init__(self, _id, *args, **kwargs):
        LineString.__init__(self, *args, **kwargs)
        LinkedWithId.__init__(self, _id)


class PolygonWithId(Polygon, LinkedWithId):
    def __init__(self, _id, *args, **kwargs):
        Polygon.__init__(self, *args, **kwargs)
        LinkedWithId.__init__(self, _id)
