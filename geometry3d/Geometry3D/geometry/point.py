# -*- coding: utf-8 -*-
"""Point Module"""
from ..utils.util import unify_types
import math
from ..utils.logger import get_main_logger
from ..utils.constant import get_sig_figures,get_eps
from ..utils.vector import Vector


class Point(object):
    """
    - Point(a, b, c)
    
    - Point([a, b, c]):
    
    The point with coordinates (a | b | c)

    - Point(Vector):
    
    The point that you get when you move the origin by the given
    vector. If the vector has coordinates (a | b | c), the point
    will have the coordinates (a | b | c) (as easy as pi).
    """
    class_level = 0 # the class level of Point
    @classmethod
    def origin(cls):
        """Returns the Point (0 | 0 | 0)"""
        return cls(0, 0, 0)
    
    def __init__(self, *args):
        if len(args) == 1:
            # Initialisation by Vector is also handled by this
            coords = args[0]
        elif len(args) == 3:
            coords = args
        else:
            raise TypeError("Point() takes one or three arguments, not {}"
                    .format(len(args)))
        self.x, self.y, self.z = unify_types(coords)
        get_main_logger().debug('Create %s' %(self.__repr__(),))


    def __repr__(self):
        return "Point({}, {}, {})".format(
                self.x,
                self.y,
                self.z,
                )

    def __hash__(self):
        """return the hash of a point"""
        return hash(("Point",
        round(self.x,get_sig_figures()),
        round(self.y,get_sig_figures()),
        round(self.z,get_sig_figures()),
        round(self.x,get_sig_figures()) * round(self.y,get_sig_figures()),
        round(self.x,get_sig_figures()) * round(self.z,get_sig_figures()),
        round(self.y,get_sig_figures()) * round(self.z,get_sig_figures()),
        ))

    def __eq__(self, other):
        """Checks if two Points are equal. Always use == and not 'is'!"""
        if isinstance(other,Point):
            return (abs(self.x - other.x) < get_eps() and
                    abs(self.y - other.y) < get_eps() and
                    abs(self.z - other.z) < get_eps())
        else:
            return False

    def __getitem__(self, item):
        """return the i element of a Point"""
        return (self.x, self.y, self.z)[item]

    def __setitem__(self, item, value):
        """set the i element of a Point"""
        setattr(self, "xyz"[item], value)
    

    def pv(self):
        """Return the position vector of the point."""
        return Vector(self.x, self.y, self.z)

    def move(self, v):
        """Return the point that you get when you move self by vector v, self is also moved"""
        if isinstance(v,Vector):
            self.x += v[0]
            self.y += v[1]
            self.z += v[2]
            return Point(self.pv())
        else:
            raise NotImplementedError("The second parameter for move function must be Vector")
    
    def distance(self,other):
        """Return the distance between self and other"""
        return math.sqrt((self.x -other.x) ** 2 + (self.y -other.y) ** 2 + (self.z -other.z) ** 2)

    """
        Added functions for Point objects
    """
    def get_dimension(self):
        """
            Added function
            Points are zero-dimensional objects
        """
        return 0

    # CLARIFY il boundary di un punto è il punto stesso? (per l'operatore touch è necessario che sia boundary)
    #   perchè anche interior è il punto stesso
    def __boundary__(self):
        """
            Added function
            :return The boundary of a point: the point itself
        """
        return self

    def __interior__(self):
        """
            Added function
            The interior of a point is the point itself
        """
        return self

    def __disjoint__(self, obj):
        """
            Added function
            **Input:**
            - self: a Point
            - obj: another object

            **Output:**
            - Whether the point self disjoints obj
        """
        if isinstance(obj, Point):
            if not self.__eq__(obj):
                return False
            return True

        elif obj.__contains__(self):
            return False
        return True

    def __touches__(self, obj):
        """
            Added function
            **Input:**
            - self: a Point
            - obj: another object

            **Output:**
            - Whether the point self touches obj
            - It returns True if the only points shared between self and obj are on the
                boundary of self and obj
            - Can not compute in point/point case
                source: https://www.researchgate.net/publication/221471671_A_Small_Set_of_Formal_Topological_Relationships_Suitable_for_End-User_Interaction
        """
        if not isinstance(obj, Point):
            self_boundary = self.__boundary__()
            cp_2_boundary = obj.__boundary__()
            intersection = obj.intersection(self)  # intersection is a symmetric operation
            if intersection:
                if isinstance(intersection, list):
                    for point in intersection:
                        if point != self_boundary or point not in cp_2_boundary:
                            return False
                    return True
                elif isinstance(intersection, Point):
                    if intersection != self_boundary or intersection not in cp_2_boundary:
                        return False
                return True
        return False

    def __within__(self, obj):
        """
            Added function
            **Input:**

            - self: a Point
            - obj: another object

            **Output:**
            - Whether the point self is within obj and
                self!=obj (within - equals)
        """
        if self.get_dimension() == obj.get_dimension():
            return False

        # ConvexPolygon
        if obj.get_dimension() == 2:
            if not obj.check_interior_point_polygon(self):
                return False
            return True

        # ConvexPolyhedron
        if obj.get_dimension() == 3:
            if not obj.check_interior_point(self):
                return False
            return True

        # Segment
        if obj.get_dimension() == 1:
            if not obj.__interior__().__contains__(self):
                return False
            return True

        else:
            return False

    # CLARIFY: un punto deve avere il metodo __overlaps__?
    #   restituirà un valore positivo quando self EQ obj
    #   quindi il risultato è uguale alla relazione EQ
    # def __overlaps__(self, obj):
    #     """
    #     **Input:**
    #     - self: a Point
    #     - obj: another object
    #
    #     **Output:**
    #     - Whether the point self touches obj
    #     - It returns True if obj equals self
    #     """
    #     if self.__eq__(obj):
    #         return True
    #     return False


origin = Point.origin

__all__ = ("Point","origin")
