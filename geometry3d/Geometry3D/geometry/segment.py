# -*- coding: utf-8 -*-
"""Segment Module"""
from .body import GeoBody
from .body import GeoBody
from .point import Point
from .plane import Plane
from ..utils.vector import Vector
from .line import Line
from ..utils.constant import get_eps
from ..utils.logger import get_main_logger
import math
import copy
from ...global_variables import *

class Segment(GeoBody):
    """
    **Input:**
    
    - Segment(Point,Point)

    - Segment(Point,Vector)
    """
    class_level = 3  # the class level of Segment

    def __init__(self, a, b):
        a = copy.deepcopy(a)
        b = copy.deepcopy(b)
        if isinstance(a, Point) and isinstance(b, Point):
            if a == b:
                raise ValueError("Cannot initialize a Segment with two identical Points")
            self.line = Line(a, b)
            self.start_point = a
            self.end_point = b
        elif isinstance(a, Point) and isinstance(b, Vector):
            if b.length() < get_eps():
                raise ValueError("Cannot initialize a Segment with the length of Vector is 0")
            self.line = Line(a, b)
            self.start_point = a
            self.end_point = Point(a.pv() + b)
        else:
            raise ValueError('Cannot create segment with type:%s and %s' % (type(a), type(b)))

    def __eq__(self, other):
        if isinstance(other, Segment):
            return ((self.start_point == other.start_point and self.end_point == other.end_point) or
                    (self.end_point == other.start_point and self.start_point == other.end_point))
        return False

    def __repr__(self):
        return "Segment({}, {})".format(self.start_point, self.end_point)

    def __contains__(self, other):
        """Checks if a point lies on a segment"""
        if isinstance(other, Point):
            r1 = other in self.line
            v = Vector(self.start_point, self.end_point)
            v1 = Vector(self.start_point, other)
            if v1.length() < get_eps():
                return True
            else:
                reletive_length = v1 * v / (v.length()) / (v.length())
                return r1 and (reletive_length > -get_eps()) and (reletive_length < 1 + get_eps())
            # r1 = point in self.line
            # r2 = point.x >= (min(self.start_point.x,self.end_point.x) - get_eps())
            # r3 = point.x <= (max(self.start_point.x,self.end_point.x) + get_eps())
        elif isinstance(other, Segment):
            if self.__eq__(other):
                return False
            else:
                return (other.start_point in self) and (other.end_point in self)
        # cannot contain a bigger object
        elif other.get_dimension() > self.get_dimension():
            return False
        else:
            get_main_logger().warning(
                "Calling type {} in type {} which is always False".format(type(other), type(self)))
            return False

    def in_(self, other):
        """other can be plane or line"""
        if isinstance(other, Line):
            return (self.start_point in other) and (self.end_point in other)
        if isinstance(other, Segment):
            return (self.start_point in other) and (self.end_point in other)
        elif isinstance(other, Plane):
            return (self.start_point in other) and (self.end_point in other)
        else:
            return NotImplementedError("")

    def __hash__(self):
        """return the hash value of the segment"""
        return hash(("Segment",
                     hash(self.start_point) + hash(self.end_point),
                     hash(self.start_point) * hash(self.end_point)
                     ))

    def __getitem__(self, idx):
        """return the i point of the segment"""
        return (self.start_point, self.end_point)[idx]

    def __setitem__(self, idx, value):
        """set the i point of the segment"""
        if idx == 0:
            self.start_point = value
        elif idx == 1:
            self.end_point = value
        else:
            raise IndexError("Index out of range")

    def move(self, v):
        """Return the Segment that you get when you move self by vector v, self is also moved"""
        if isinstance(v, Vector):
            self.start_point.move(v)
            self.end_point.move(v)
            return Segment(self.start_point, self.end_point)
        else:
            raise NotImplementedError("The second parameter for move function must be Vector")

    def parametric(self):
        """Returns (start_point, end_point) so that you can build the information for the segment
        """
        return (self.start_point, self.end_point)

    def length(self):
        """retutn the length of the segment"""
        return self.start_point.distance(self.end_point)

    """
        Added functions for Segment objects
    """

    def get_dimension(self):
        """
            Added function
            Segments are one-dimensional objects
        """
        return 1

    def __boundary__(self):
        """
            Added function
            The boundary of a segment is the set (start_point, end_point)
        """
        return [self.start_point, self.end_point]

    def __interior__(self):
        """
            Added function
            :return: A segment object: the interior of a segment
        """
        start_end = [self.start_point, self.end_point]
        points = []
        for element in start_end:
            if self.__contains__(Point(element[0] - toll, element[1] - toll, element[2] - toll)):
                points.append(Point(element[0] - toll, element[1] - toll, element[2] - toll))
            elif self.__contains__(Point(element[0] + toll, element[1] - toll, element[2] - toll)):
                points.append(Point(element[0] + toll, element[1] - toll, element[2] - toll))
            elif self.__contains__(Point(element[0] + toll, element[1] + toll, element[2] - toll)):
                points.append(Point(element[0] + toll, element[1] + toll, element[2] - toll))
            elif self.__contains__(Point(element[0] + toll, element[1] + toll, element[2] + toll)):
                points.append(Point(element[0] + toll, element[1] + toll, element[2] + toll))
            elif self.__contains__(Point(element[0] - toll, element[1] + toll, element[2] - toll)):
                points.append(Point(element[0] - toll, element[1] + toll, element[2] - toll))
            elif self.__contains__(Point(element[0] - toll, element[1] - toll, element[2] + toll)):
                points.append(Point(element[0] - toll, element[1] - toll, element[2] + toll))
            elif self.__contains__(Point(element[0] - toll, element[1] + toll, element[2] + toll)):
                points.append(Point(element[0] - toll, element[1] + toll, element[2] + toll))
            elif self.__contains__(Point(element[0] + toll, element[1] - toll, element[2] + toll)):
                points.append(Point(element[0] + toll, element[1] - toll, element[2] + toll))
            elif self.__contains__(Point(element[0] + toll, element[1], element[2])):
                points.append(Point(element[0] + toll, element[1], element[2]))
            elif self.__contains__(Point(element[0] - toll, element[1], element[2])):
                points.append(Point(element[0] - toll, element[1], element[2]))
            elif self.__contains__(Point(element[0] + toll, element[1] + toll, element[2])):
                points.append(Point(element[0] + toll, element[1] + toll, element[2]))
            elif self.__contains__(Point(element[0] - toll, element[1] + toll, element[2])):
                points.append(Point(element[0] - toll, element[1] + toll, element[2]))
            elif self.__contains__(Point(element[0] + toll, element[1] - toll, element[2])):
                points.append(Point(element[0] + toll, element[1] - toll, element[2]))
            elif self.__contains__(Point(element[0] - toll, element[1] - toll, element[2])):
                points.append(Point(element[0] - toll, element[1] - toll, element[2]))
            elif self.__contains__(Point(element[0] + toll, element[1], element[2] + toll)):
                points.append(Point(element[0] + toll, element[1], element[2] + toll))
            elif self.__contains__(Point(element[0] - toll, element[1], element[2] + toll)):
                points.append(Point(element[0] - toll, element[1], element[2] + toll))
            elif self.__contains__(Point(element[0] + toll, element[1], element[2] - toll)):
                points.append(Point(element[0] + toll, element[1], element[2] - toll))
            elif self.__contains__(Point(element[0] - toll, element[1], element[2] - toll)):
                points.append(Point(element[0] - toll, element[1], element[2] - toll))
            elif self.__contains__(Point(element[0], element[1] + toll, element[2] + toll)):
                points.append(Point(element[0], element[1] + toll, element[2] + toll))
            elif self.__contains__(Point(element[0], element[1] - toll, element[2] + toll)):
                points.append(Point(element[0], element[1] - toll, element[2] + toll))
            elif self.__contains__(Point(element[0], element[1] + toll, element[2] - toll)):
                points.append(Point(element[0], element[1] + toll, element[2] - toll))
            elif self.__contains__(Point(element[0], element[1] - toll, element[2] - toll)):
                points.append(Point(element[0], element[1] - toll, element[2] - toll))
            elif self.__contains__(Point(element[0], element[1] + toll, element[2])):
                points.append(Point(element[0], element[1] + toll, element[2]))
            elif self.__contains__(Point(element[0], element[1] - toll, element[2])):
                points.append(Point(element[0], element[1] - toll, element[2]))
            elif self.__contains__(Point(element[0], element[1], element[2] + toll)):
                points.append(Point(element[0], element[1], element[2] + toll))
            elif self.__contains__(Point(element[0], element[1], element[2] - toll)):
                points.append(Point(element[0], element[1], element[2] - toll))
            elif self.__contains__(Point(element[0], element[1] + toll, element[2] - toll)):
                points.append(Point(element[0], element[1] + toll, element[2] - toll))

        new_segment = Segment(points[0], points[1])
        return new_segment

    def __crosses__(self, obj):
        """
            Added function
            **Input:**

            - self: a Segment
            - obj: another object (except Point)

            **Output:**
            - Whether the polyhedron self crosses s2
            - The dimension of self and obj must be different
            - They have some but not all interior points in common, and the dimension of
            the intersection is less than that of at least one of them
            source: https://en.wikipedia.org/wiki/DE-9IM#cite_note-davis2007-10
        """
        if isinstance(obj, Point):
            return False
        if isinstance(obj, Segment):
            if self.__eq__(obj):
                return False

        # The dimension of self and obj must be different (except by line/line inputs)
        if self.get_dimension() == obj.get_dimension() and not isinstance(obj, Segment):
            return False

        interior_1 = self.__interior__()
        interior_2 = obj.__interior__()

        # They have some but not all interior points in common
        # interior_1 is surely a Segment
        if isinstance(interior_2, Segment):
            if interior_1.__eq__(interior_2):
                return False

        intersection = self.intersection(obj)
        if intersection:
            # if intersection equals self or obj, there is no cross
            if intersection.__eq__(self) or intersection.__eq__(obj):
                return False
            # if the intersection is a point that lies on the boundary, then the relation can not be a cross (is a touch)

            # self is a Segment and intersection is a Point
            if intersection.get_dimension() == 0:
                if intersection in self.__boundary__():
                    return False

                # obj and self are two segments
                # check if the intersection is the first or the last point of the other segment
                # if so, then it's not a cross (but a touch)
                if obj.get_dimension() == 1:
                    if intersection in [obj.start_point, obj.end_point]:
                        return False

                # obj is a convexpolygon
                # if the intersection is on the boundary of obj, then it's not a cross but it's a touch
                if obj.get_dimension() == 2:
                    if any([intersection in el for el in obj.__boundary__()]):
                        return False

                # obj is a convexpolyhedron
                # if the intersection is on the boundary of obj, then it's not a cross but it's a touch
                if obj.get_dimension() == 3:
                    for cp in obj.__boundary__():
                        if intersection in cp:
                            return False



            # intersection and self are Segments
            if intersection.get_dimension() == 1:
                if obj.get_dimension() == 3:
                    if any([intersection in cp for cp in obj.__boundary__()]):
                        return False
                for el in self.__boundary__():
                    if intersection.__eq__(el):
                        return False
                # check if some elements of obj are in the intersection
                # otherwise it's a touch
                if obj.__interior__().intersection(intersection) is None:
                    return False
            # the dimension of the intersection is less than that of at least one of them
            if intersection.get_dimension() < self.get_dimension() or intersection.get_dimension() < obj.get_dimension():
                return True
        return False

    def __disjoint__(self, obj):
        """
            Added function
            **Input:**
            - self: a Segment
            - obj: another object

            **Output:**
            - Whether the segment self disjoints obj
        """
        if self.intersection(obj) is None:
            return True
        else:
            return False

    def __overlaps__(self, s2):
        """
            Added function
           **Input:**

           - self: a Segment
           - obj: another Segment

           **Output:**
           - Whether the segment self overlaps obj
           - The dimension of self and obj must be the same
           - They have some but not all points in common, they have the same dimension,
            and the intersection of the interiors of the two geometries has the same dimension
            as the geometries themselves
            source: https://en.wikipedia.org/wiki/DE-9IM#cite_note-davis2007-10
       """
        # The dimension of self and obj must be the same
        # They have some but not all points in common
        if self.get_dimension() != s2.get_dimension() or self.__eq__(s2):
            return False

        interior_1 = self.__interior__()
        interior_2 = s2.__interior__()
        intersection = self.intersection(s2)

        # the intersection of the interiors of the two geometries has the same dimension
        # as the geometries themselves
        if interior_1.intersection(interior_2) and interior_2.intersection(interior_1):
            if interior_1.intersection(interior_2).get_dimension() != self.get_dimension() or \
                    interior_1.intersection(interior_2).get_dimension() != s2.get_dimension() or \
                    intersection.__eq__(self) or intersection.__eq__(s2):
                return False
            return True
        # otherwise the intersection is None
        return False

    def __touches__(self, obj):
        """
            Added function
            **Input:**
            - self: a Segment
            - obj: another object

            **Output:**
            - Whether the segment self touches obj
        """
        intersection = self.intersection(obj)
        if intersection:
            # intersection is a ConvexPolyhedron, a ConvexPolygon or a Segment
            if intersection.get_dimension() >= 2:
                return False

            if intersection.get_dimension() == 1:
                if obj.get_dimension() != 3:
                    if intersection.intersection(self.__interior__()) is not None and intersection.intersection(obj.__interior__()) is not None:
                        return False
                else:
                    if intersection.intersection(self.__interior__()) is not None:
                        # if intersection.__interior__() not in self:
                        for cp in obj.__boundary__():
                            if intersection.start_point in cp and intersection.end_point in cp:
                                return True
                            if intersection.start_point in cp.__boundary__() and intersection.end_point in cp.__boundary__():
                                return True
                        # otherwise interiors touch
                        return False

                if self.__interior__() not in intersection or intersection not in obj.__interior__():
                    return True
                if all([self.__contains__(point) for point in intersection]):
                    if obj.__interior__().__contains__(intersection):
                        return False

                if all([obj.__contains__(point) for point in intersection]):
                    if self.__interior__().__contains__(intersection):
                        return False
                return True

            # Intersection can only be a point
            # to be a touch, the point can be an internal point of just one of the elements
            if intersection.get_dimension() == 0:
                if intersection not in self.__interior__() or intersection not in obj.__interior__():
                    return True
        return False

    def __within__(self, obj):
        """
            Added function
            **Input:**

            - self: a Segment
            - obj: another object

            **Output:**
            - Whether the segment self is within obj and
                self!=obj (within - equals)
        """
        intersection = self.intersection(obj)
        if self.get_dimension() == obj.get_dimension():
            if obj.__eq__(self):  # self!=obj (within - equals)
                return False
            # for point in [self.start_point, self.__interior__(), self.end_point]:
            for point in [self.start_point, self.end_point]:
                if not obj.__contains__(point):
                    return False
            return True

        # ConvexPolygon
        if obj.get_dimension() == 2:
            for point in [self.start_point, self.end_point]:
                if not obj.check_interior_point_polygon(point):
                    for el in obj.__boundary__():
                        if self in el or self.__eq__(el):
                            return False
                    if not any([point in p for p in obj.__boundary__()]):
                        return False
            return True

        # ConvexPolyhedron
        if obj.get_dimension() == 3:
            for point in [self.start_point, self.end_point]:
                if not obj.check_interior_point(point):
                    return False
            # check if segment completely belongs to the boundary of obj
            for cp in obj.__boundary__():
                if intersection in cp or intersection in cp.__boundary__():
                    return False
            # there must be some interior point shared between the two geometries
            if self.intersection(obj.__interior__()) is None:
                return False
            # within means that the intersection is in the interiors
            if self.__interior__() in intersection and \
                    not (obj.check_interior_point(intersection.start_point) or obj.check_interior_point(intersection.end_point)):
                return False
            return True

        # Segment can't be contained in a smaller object
        else:
            return False


__all__ = ("Segment",)
