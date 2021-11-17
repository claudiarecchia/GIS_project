"""Polyhedron Module"""
import copy

from .body import GeoBody
from .point import Point
from .polygon import ConvexPolygon, Parallelogram, Circle, get_circle_point_list
from .pyramid import Pyramid
from .segment import Segment
from ..utils.constant import *
from ..utils.logger import get_main_logger
from ..utils.vector import Vector, z_unit_vector
from ...global_variables import *


class ConvexPolyhedron(GeoBody):
    class_level = 5  # the class level of ConvexPolyhedron
    """
    **Input:**
    
    - convex_polygons: tuple of ConvexPolygons

    **Output:**

    - ConvexPolyhedron
    
    - The correctness of convex_polygons are checked According to Euler's formula.

    - The normal of the convex polygons are checked and corrected which should be toward the outer direction
    """
    @classmethod
    def Parallelepiped(cls,base_point,v1,v2,v3):
        """
        A special function for creating Parallelepiped

        **Input:**

        - base_point: a Point

        - v1, v2, v3: three Vectors

        **Output:**

        - A parallelepiped which is a ConvexPolyhedron instance.
        """
        if isinstance(base_point,Point) and isinstance(v1,Vector) and isinstance(v2,Vector) and isinstance(v3,Vector):
            if v1.length() == 0 or v2.length == 0 or v3.length == 0:
                raise ValueError("The length for the three vector shouldn't be zero")
            elif v1.parallel(v2) or v1.parallel(v3) or v2.parallel(v3):
                raise ValueError("The three vectors shouldn't be parallel to each other")
            else:
                p_diag = copy.deepcopy(base_point).move(v1).move(v2).move(v3)
                rectangle0=Parallelogram(base_point,v1,v2)
                rectangle1=Parallelogram(base_point,v2,v3)
                rectangle2=Parallelogram(base_point,v1,v3)
                rectangle3=Parallelogram(p_diag,-v1,-v2)
                rectangle4=Parallelogram(p_diag,-v2,-v3)
                rectangle5=Parallelogram(p_diag,-v1,-v3)
                return cls((rectangle0,rectangle1,rectangle2,rectangle3,rectangle4,rectangle5))

        else:
            raise TypeError("Parallelepiped should be initialized with Point, Vector, Vector and Vector, but the given types are %s, %s, %s and %s" %(type(base_point),type(v1),type(v2),type(v3)))

    @classmethod
    def Sphere(cls,center,radius,n1=10,n2=3):
        """
        A special function for creating the inscribed polyhedron of a sphere 

        **Input:**

        - center: The center of the sphere

        - radius: The radius of the sphere

        - n1=10: The number of Points on a longitude circle

        - n2=3: The number sections of a quater latitude circle 

        **Output:**

        - An inscribed polyhedron of the given sphere.
        """
        import copy
        import math
        cpg_list = []
        mc = get_circle_point_list(center = center,normal = z_unit_vector(),radius = radius,n=n1) # medium circle
        top_point = copy.deepcopy(center).move(radius * z_unit_vector())
        bottom_point = copy.deepcopy(center).move(-radius * z_unit_vector())
        # heights=[]
        # radii = []
        tc = [] # top circles
        bc = [] # bottom circles
        for i in range(n2-1):
            angle_i = math.pi / 2 / n2 *(i+1) 
            height_i=radius * math.sin(angle_i)
            r_i=radius * math.cos(angle_i)
            tc.append(get_circle_point_list(
                center = copy.deepcopy(center).move(height_i * z_unit_vector()),
                normal = z_unit_vector(),
                radius = r_i,
                n=n1
            ))
            bc.append(get_circle_point_list(
                center = copy.deepcopy(center).move(-height_i * z_unit_vector()),
                normal = z_unit_vector(),
                radius = r_i,
                n=n1
            ))
        for i in range(n1):
            start = i
            end = (i + 1) % n1 
            cpg_list.append(ConvexPolygon((mc[start],mc[end],tc[0][end],tc[0][start])))
            cpg_list.append(ConvexPolygon((mc[start],mc[end],bc[0][end],bc[0][start])))
            for j in range(1,n2-1):
                cpg_list.append(ConvexPolygon((tc[j-1][start],tc[j-1][end],tc[j][end],tc[j][start])))
                cpg_list.append(ConvexPolygon((bc[j-1][start],bc[j-1][end],bc[j][end],bc[j][start])))
            cpg_list.append(ConvexPolygon((top_point,tc[n2-2][end],tc[n2-2][start])))
            cpg_list.append(ConvexPolygon((bottom_point,bc[n2-2][end],bc[n2-2][start])))
        return cls(tuple(cpg_list))
        # return cpg_list

    @classmethod
    def Cylinder(cls,circle_center,radius,height_vector,n=10):
        """
        A special function for creating the inscribed polyhedron of a sphere 

        **Input:**

        - circle_center: The center of the bottom circle

        - radius: The radius of the bottom circle

        - height_vector: The Vector from the bottom circle center to the top circle center 

        - n=10: The number of Points on the bottom circle

        **Output:**

        - An inscribed polyhedron of the given cylinder.
        """
        import copy
        top_point = copy.deepcopy(circle_center).move(height_vector)
        # print(top_point)
        bottom_circle = Circle(center=circle_center,normal=height_vector,radius=radius,n=n)
        bottom_circle_point_list = get_circle_point_list(center=circle_center,normal=height_vector,radius=radius,n=n)

        top_circle = Circle(center=top_point,normal=height_vector,radius=radius,n=n)
        top_circle_point_list = get_circle_point_list(center=top_point,normal=height_vector,radius=radius,n=n)
        cpg_list = [top_circle,bottom_circle]
        for i in range(len(top_circle_point_list)):
            start = i
            end = (i + 1) % len(top_circle_point_list)
            cpg_list.append(ConvexPolygon((top_circle_point_list[start],top_circle_point_list[end],bottom_circle_point_list[end],bottom_circle_point_list[start])))
        return cls(tuple(cpg_list))

    @classmethod
    def Cone(cls,circle_center,radius,height_vector,n=10):
        """
        A special function for creating the inscribed polyhedron of a sphere 

        **Input:**

        - circle_center: The center of the bottom circle

        - radius: The radius of the bottom circle

        - height_vector: The Vector from the bottom circle center to the top circle center 

        - n=10: The number of Points on the bottom circle

        **Output:**

        - An inscribed polyhedron of the given cone.
        """
        import copy
        top_point = copy.deepcopy(circle_center).move(height_vector)
        # print(top_point)
        circle = Circle(center=circle_center,normal=height_vector,radius=radius,n=n)
        circle_point_list = get_circle_point_list(center=circle_center,normal=height_vector,radius=radius,n=n)
        cpg_list = [circle]
        for i in range(len(circle_point_list)):
            start = i
            end = (i + 1) % len(circle_point_list)
            cpg_list.append(ConvexPolygon((top_point,circle_point_list[start],circle_point_list[end])))
        return cls(tuple(cpg_list))

    def __init__(self,convex_polygons):
        self.convex_polygons = list(copy.deepcopy(convex_polygons))
        # self.convex_polygons = list(convex_polygons)
        self.point_set = set()
        self.segment_set = set()
        self.pyramid_set = set()
        
        for convex_polygon in self.convex_polygons:    
            for point in convex_polygon.points:
                self.point_set.add(point)
            for segment in convex_polygon.segments():
                self.segment_set.add(segment)
        
        self.center_point = self._get_center_point()

        for i in range(len(self.convex_polygons)):
            convex_polygon = self.convex_polygons[i]
            if Vector(self.center_point,convex_polygon.plane.p) * convex_polygon.plane.n < -get_eps():
                self.convex_polygons[i] = - convex_polygon
            self.pyramid_set.add(Pyramid(convex_polygon,self.center_point,direct_call=False))
        if not self._check_normal():
            raise ValueError('Check Normal Fails For The Convex Polyhedron')
        if not self._euler_check():
            get_main_logger().critical('V:{} E:{} F:{}'.format(len(self.point_set),len(self.segment_set),len(self.convex_polygons)))
            raise ValueError('Check for the number of vertices, faces and edges fails, the polyhedron may not be closed')

    def _euler_check(self):
        number_points = len(self.point_set)
        number_segments = len(self.segment_set)
        number_polygons = len(self.convex_polygons)
        return number_points - number_segments + number_polygons == 2

    def _check_normal(self):
        """return True if all the polygons' normals point to the outside"""
        for convex_polygon in self.convex_polygons:
            if Vector(self.center_point,convex_polygon.plane.p) * convex_polygon.plane.n < -get_eps():
                return False
        return True
    
    def _get_center_point(self):
        """
        **Input:**
        
        - self

        **Output:**

        - The center point of this point set
        """
        x,y,z = 0,0,0
        num_points = len(self.point_set)
        for point in self.point_set:
            x += point.x
            y += point.y
            z += point.z
        return Point(x / num_points,y / num_points, z / num_points)
    
    def __repr__(self):
        return "ConvexPolyhedron({})".format(self.point_set)

    def __contains__(self, other):
        """
        **Input:**

        - point: a Object

        **Output:**

        - Whether the polyhedron self contains:
            - the point
            - the segment
            - the convexPolygon
            - the convexPolyhedron
        """
        if isinstance(other, Point):
            for polygon in self.convex_polygons:
                direction_vector = Vector(polygon.center_point, other)
                if direction_vector * polygon.plane.n > get_eps():
                    return False
            return True

        elif isinstance(other, Segment):
            return ((other.start_point in self) and (other.end_point in self))
        
        elif isinstance(other, ConvexPolygon):
            for point in other.points:
                if not point in self:
                    return False
            return True

        elif isinstance(other, ConvexPolyhedron):
            return self.convex_polyhedron_contains(other)
        else:
            raise NotImplementedError("")

    def __eq__(self,other):
        if isinstance(other,ConvexPolyhedron):
            return (hash(self) == hash(other))
        else:
            return False

    def move(self,v):
        """Return the ConvexPolyhedron that you get when you move self by vector v, self is also moved"""
        if isinstance(v,Vector):
            convexpolygon_list = []
            for convexpolygon in self.convex_polygons:
                convexpolygon_list.append(convexpolygon.move(v))
            self.convex_polygons = tuple(convexpolygon_list)   
            self.point_set = set()
            self.segment_set = set()
            self.pyramid_set = set()
            for convex_polygon in self.convex_polygons: 
                for point in convex_polygon.points:
                    self.point_set.add(point)
                for segment in convex_polygon.segments():
                    self.segment_set.add(segment)
        
            self.center_point = self._get_center_point()

            for i in range(len(self.convex_polygons)):
                convex_polygon = self.convex_polygons[i]
                if Vector(self.center_point,convex_polygon.plane.p) * convex_polygon.plane.n < -get_eps():
                    self.convex_polygons[i] = - convex_polygon
                self.pyramid_set.add(Pyramid(convex_polygon,self.center_point,direct_call=False))
            if not self._check_normal():
                raise ValueError('Check Normal Fails For The Convex Polyhedron')
            if not self._euler_check():
                get_main_logger().critical('V:{} F:{} E:{}'.format(len(self.point_set),len(self.segment_set),len(self.convex_polygons)))
                raise ValueError('Check for the number of vertices, faces and edges fails, the polyhedron may not be closed')
            return ConvexPolyhedron(self.convex_polygons)
        else:
            raise NotImplementedError("The second parameter for move function must be Vector")

    def _get_polygon_hash_sum(self):
        """return the sum of hash value of all the ConvexPolygons"""
        hash_sum = 0
        for polygon in self.convex_polygons:
            hash_sum += hash(polygon)
        return hash_sum

    def _get_point_hash_sum(self):
        """return the sum of hash value of all the points"""
        hash_sum = 0
        for point in self.point_set:
            hash_sum += hash(point)
        return hash_sum

    # the hash function is not accurate
    # in some extreme case, this function may fail
    # which means it's vulnerable to attacks.
    def __hash__(self):
        """return the hash value of the ConvexPolyhedron"""
        return hash((
            "ConvexPolyhedron",
            round(self._get_polygon_hash_sum(),SIG_FIGURES),
            round(self._get_point_hash_sum(),SIG_FIGURES)
        ))

    #no in_ function

    def length(self):
        """return the total length of the polyhedron"""
        l = 0
        for segment in self.segment_set:
            l += segment.length()
        return l

    def area(self):
        """return the total area of the polyhedron"""
        a = 0
        for polygon in self.convex_polygons:
            a += polygon.area()
        return a

    def volume(self):
        """return the total volume of the polyhedron"""
        v = 0
        for pyramid in self.pyramid_set:
            v += pyramid.volume()
        return v

    """
        Added functions for ConvexPolyhedron objects
    """

    def get_dimension(self):
        """
            Added function
            ConvexPolyherdons are three-dimensional objects
        """
        return 3

    def __boundary__(self):
        """
            Added function
            **Input:**
            - self: a ConvexPolyhedron
            **Output:**
            - The boundary or self (a set of ConvexPolygons)
        """
        return self.convex_polygons

    def __interior__(self):
        """
            Added function
            If all the polyhedrons' normals point to the outside it means that
            building a little bit smaller ConvexPolyhedron, we'll consider just the
            interior of self
        """
        if self._check_normal():
            convex_polygons = self.convex_polygons
            pol_copy = copy.deepcopy(self)
            new_convex_plygons = []
            for cp in convex_polygons:
                new_points_convex_polygons = []
                for point in cp.points:
                    if pol_copy.check_interior_point(Point(point[0] - toll, point[1] - toll, point[2] - toll)):
                        new_points_convex_polygons.append(Point(point[0] - toll, point[1] - toll, point[2] - toll))
                    elif pol_copy.check_interior_point(Point(point[0] + toll, point[1] - toll, point[2] - toll)):
                        new_points_convex_polygons.append(Point(point[0] + toll, point[1] - toll, point[2] - toll))
                    elif pol_copy.check_interior_point(Point(point[0] + toll, point[1] + toll, point[2] - toll)):
                        new_points_convex_polygons.append(Point(point[0] + toll, point[1] + toll, point[2] - toll))
                    elif pol_copy.check_interior_point(Point(point[0] + toll, point[1] + toll, point[2] + toll)):
                        new_points_convex_polygons.append(Point(point[0] + toll, point[1] + toll, point[2] + toll))
                    elif pol_copy.check_interior_point(Point(point[0] - toll, point[1] + toll, point[2] - toll)):
                        new_points_convex_polygons.append(Point(point[0] - toll, point[1] + toll, point[2] - toll))
                    elif pol_copy.check_interior_point(Point(point[0] - toll, point[1] - toll, point[2] + toll)):
                        new_points_convex_polygons.append(Point(point[0] - toll, point[1] - toll, point[2] + toll))
                    elif pol_copy.check_interior_point(Point(point[0] - toll, point[1] + toll, point[2] + toll)):
                        new_points_convex_polygons.append(Point(point[0] - toll, point[1] + toll, point[2] + toll))
                    elif pol_copy.check_interior_point(Point(point[0] + toll, point[1] - toll, point[2] + toll)):
                        new_points_convex_polygons.append(Point(point[0] + toll, point[1] - toll, point[2] + toll))

                new_convex_plygons.append(ConvexPolygon(new_points_convex_polygons))

            interior = ConvexPolyhedron((new_convex_plygons))
            return interior

    def check_interior_point(self, point):
        """
            Added function
            returns True if the considered point is behind all faces of self
            and the point does not belong to the boundary of the polyhedron
        """
        for convex_polygon in self.convex_polygons:
            if Vector(point, convex_polygon.plane.p) * convex_polygon.plane.n < -get_eps() or point in [pol for pol in self.__boundary__()]:
                return False
        return True

    def __crosses__(self, obj):
        """
            Added function
            **Input:**

            - self: a ConvexPolyhedron
            - obj: another object (except Point)

            **Output:**
            - Whether the polyhedron self crosses obj
            - The dimension of self and obj must be different
            - They have some but not all interior points in common, and the dimension of
            the intersection is less than that of at least one of them
            source: https://en.wikipedia.org/wiki/DE-9IM#cite_note-davis2007-10
        """
        # The dimension of self and obj must be different
        if self.get_dimension() == obj.get_dimension() or self.__eq__(obj) or isinstance(obj, Point):
            return False

        interior_1 = self.__interior__()
        interior_2 = obj.__interior__()

        # They have some but not all interior points in common
        if interior_1.__eq__(interior_2):
            return False

        # the dimension of the intersection is less than that of at least one of them
        if self.intersection(obj).get_dimension() < self.get_dimension() or self.intersection(obj).get_dimension() < obj.get_dimension():
            return True
        else:
            return False

    def convex_polyhedron_contains(self, cp_2):
        """
            Added function
            **Input:**

            - self: a ConvexPolyhedron
            - cp_2: a ConvexPolyhedron

            **Output:**
            - Whether the polyhedron self contains the polyhedron cp_2 and
                self!=cp_2 (contains - equals)

            convex_polyhedron_contains(a, b) = convex_polyhedron_within(b, a)
        """
        result = True
        polygons = cp_2.convex_polygons
        for pol in polygons:
            if not self.__contains__(pol):
                result = False
        if self.__eq__(cp_2):  # cp_1!=cp_2 (contains - equals)
            result = False
        return result

    def __disjoint__(self, obj):
        """
            Added function
            **Input:**
            - self: a ConvexPolyhedron
            - obj: another object

            **Output:**
            - Whether the polyhedron self disjoints obj
        """
        if self.intersection(obj) is None:
            return True
        else:
            return False

    def __overlaps__(self, cp_2):
        """
            Added function
           **Input:**

           - self: a ConvexPolyhedron
           - obj: another ConvexPolyhedron

           **Output:**
           - Whether the polyhedron self overlaps obj
           - The dimension of self and obj must be the same
           - They have some but not all points in common, they have the same dimension,
            and the intersection of the interiors of the two geometries has the same dimension
            as the geometries themselves
            source: https://en.wikipedia.org/wiki/DE-9IM#cite_note-davis2007-10
       """
        # The dimension of self and obj must be the same
        # They have some but not all points in common
        if self.get_dimension() != cp_2.get_dimension() or self.__eq__(cp_2):
            return False

        interior_1 = self.__interior__()
        interior_2 = cp_2.__interior__()
        intersection = self.intersection(cp_2)
        # the intersection of the interiors of the two geometries has the same dimension
        # as the geometries themselves
        if interior_1.intersection(interior_2) and interior_1.intersection(interior_2):
            if interior_1.intersection(interior_2).get_dimension() != self.get_dimension() or \
                    interior_1.intersection(interior_2).get_dimension() != cp_2.get_dimension() or \
                    intersection.__eq__(self) or intersection.__eq__(cp_2):
                return False
            return True
        # otherwise the intersection is None
        return False

    def __touches__(self, obj):
        """
            Added function
            **Input:**

            - self: a ConvexPolyhedron
            - obj: another object

            **Output:**
            - Whether the polyhedron self touches obj
            - It returns True if the only points shared between self and obj are on the
                boundary of self and obj
        """
        intersection = self.intersection(obj)
        if intersection:
            # intersection is a ConvexPolyhedron
            if intersection.get_dimension() == 3:
                return False
            # intersection can be a ConvexPolygon, a Segment or a Point
            if intersection.get_dimension() == 2:
                # the intersection is a ConvexPolygon
                if self.__interior__() not in intersection and obj.__interior__() not in intersection:
                    return True
                return False

            if intersection.get_dimension() == 1:
                # the intersection is a Segment
                if self.__interior__() not in intersection and obj.__interior__() not in intersection:
                    return True
                return False

            if intersection.get_dimension() == 0:
                # the intersection is a Point
                if obj.get_dimension() != 0:
                    if intersection not in self.__interior__() and intersection not in obj.__interior__():
                        return True
                    return False
                else:
                    # second object is a point
                    if self.check_interior_point(intersection):
                        return False
                    return True
        return False

    def __within__(self, obj):
        """
            Added function
            **Input:**

            - self: a ConvexPolyhedron
            - obj: another object

            **Output:**
            - Whether the polyhedron self is within obj and
                self!=obj (within - equals)
        """

        if self.get_dimension() == obj.get_dimension():
            if obj.__eq__(self):  # self!=obj (within - equals)
                return False

            polygons = self.convex_polygons
            for pol in polygons:
                if not obj.__contains__(pol):
                    return False
                return True

        # objects don't have the same dimension
        # but a convexPolyhedron can't be contained in a smaller object
        else:
            return False


Parallelepiped = ConvexPolyhedron.Parallelepiped
Cone = ConvexPolyhedron.Cone
Sphere = ConvexPolyhedron.Sphere
Cylinder = ConvexPolyhedron.Cylinder

__all__=("ConvexPolyhedron","Parallelepiped","Cone","Sphere","Cylinder")