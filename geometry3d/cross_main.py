from geometry3d.Geometry3D import *
import copy
"""
Cross is a symmetric relation
- The dimension of the two objects must be different
- They have some but not all interior points in common, and the dimension of
the intersection is less than that of at least one of them
- Points are not considered for this relation neither as self, nor as parameter
"""

#  ConvexPolyhedrons
a = origin()
b = Point(1, 0, 0)
c = Point(1, 1, 0)
d = Point(0, 1, 0)
e = Point(0, 0, 1)
f = Point(1, 0, 1)
g = Point(1, 1, 1)
h = Point(0, 1, 1)
cp_1 = ConvexPolygon((a, b, c, d))  # base inf
cp_2 = ConvexPolygon((e, f, g, h))  # base sup
cp_3 = ConvexPolygon((a, b, f, e))
cp_4 = ConvexPolygon((b, c, g, f))
cp_5 = ConvexPolygon((c, d, g, h))
cp_6 = ConvexPolygon((d, a, h, e))
cp_blue = ConvexPolyhedron((cp_1, cp_2, cp_3, cp_4, cp_5, cp_6))

a = Point(1.5, 1, 0)
b = Point(2, 1, 0)
c = Point(2, 2, 0)
d = Point(1, 2, 0)
e = Point(1.5, 1, 1)
f = Point(2, 1, 1)
g = Point(2, 2, 1)
h = Point(1, 2, 1)
cp_1 = ConvexPolygon((a, b, c, d))  # base inf
cp_2 = ConvexPolygon((e, f, g, h))  # base sup
cp_3 = ConvexPolygon((a, b, f, e))
cp_4 = ConvexPolygon((b, c, g, f))
cp_5 = ConvexPolygon((c, d, g, h))
cp_6 = ConvexPolygon((d, a, h, e))
cp_violet = ConvexPolyhedron((cp_1, cp_2, cp_3, cp_4, cp_5, cp_6))

a = Point(0, 0, 0.5)
b = Point(2, 0, 0.5)
c = Point(2, 2, 0.5)
d = Point(0, 2, 0.5)
plane = ConvexPolygon((a, b, c, d))


r = Renderer()
r.add((cp_blue, 'b', 1), normal_length=0)
r.add((cp_violet, 'violet', 1), normal_length=0)
r.add((plane, 'y', 1), normal_length=0)



print("Piano crosses poliedro blu: ", plane.__crosses__(cp_blue))
print("Piano crosses poliedro viola: ", plane.__crosses__(cp_violet))
print("Poliedro viola crosses piano: ", cp_violet.__crosses__(plane))


# segments
s = Segment(Point(0,0,0.5), Point(2, 2, 0.5))
r.add((s, 'red', 1), normal_length=0)
r.show()
print("Piano crosses segment: ", plane.__crosses__(s))
print("Segment crosses piano: ", s.__crosses__(plane))
print("Poliedro viola crosses segment: ", cp_violet.__crosses__(s))
print("Segment crosses poliedro viola: ", s.__crosses__(cp_violet))


