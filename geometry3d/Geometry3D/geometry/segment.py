# -*- coding: utf-8 -*-
"""Segment Module"""
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
        return ((self.start_point == other.start_point and self.end_point == other.end_point) or
                (self.end_point == other.start_point and self.start_point == other.end_point))

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
            return (other.start_point in self) and (other.end_point in self)
        else:
            get_main_logger().warning(
                "Calling type {} in type {} which is always False".format(type(other), type(self)))
            return False

    def in_(self, other):
        """other can be plane or line"""
        if isinstance(other, Line):
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

    def get_dimension(self):
        """
            Added function
            Segments are one-dimensional objects
        """
        return 1

    def get_interior(self):
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
            elif self.__contains__(Point(element[0] - toll, element[1] , element[2] + toll)):
                points.append(Point(element[0] - toll, element[1], element[2] + toll))
            elif self.__contains__(Point(element[0] + toll, element[1], element[2] - toll)):
                points.append(Point(element[0] + toll, element[1], element[2] - toll))
            elif self.__contains__(Point(element[0] - toll, element[1] , element[2] - toll)):
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

        new_segment = Segment(points[0], points[1])
        print(new_segment)


__all__ = ("Segment",)
