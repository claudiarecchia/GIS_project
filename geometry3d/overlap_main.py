from geometry3d.Geometry3D import *

""" 
Overlap is a symmetric relation
- The dimension of self and s2 must be the same
- They have some but not all points in common, they have the same dimension,
and the intersection of the interiors of the two geometries has the same dimension
as the geometries themselves
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


a = Point(0.5, 0.5, 0)
b = Point(1.5, 0.5, 0)
c = Point(1.5, 1.5, 0)
d = Point(0.5, 1.5, 0)
e = Point(0.5, 0.5, 1)
f = Point(1.5, 0.5, 1)
g = Point(1.5, 1.5, 1)
h = Point(0.5, 1.5, 1)
cp_1 = ConvexPolygon((a, b, c, d))  # base inf
cp_2 = ConvexPolygon((e, f, g, h))  # base sup
cp_3 = ConvexPolygon((a, b, f, e))
cp_4 = ConvexPolygon((b, c, g, f))
cp_5 = ConvexPolygon((c, d, g, h))
cp_6 = ConvexPolygon((d, a, h, e))
cp_gray = ConvexPolyhedron((cp_1, cp_2, cp_3, cp_4, cp_5, cp_6))

a = Point(0, 0, 0.5)
b = Point(2, 0, 0.5)
c = Point(2, 2, 0.5)
d = Point(0, 2, 0.5)
plane = ConvexPolygon((a, b, c, d))

print("Blue overlaps gray: ", cp_blue.__overlaps__(cp_gray))
print("Gray overlaps blue: ", cp_gray.__overlaps__(cp_blue))
print("Violet overlaps gray: ", cp_violet.__overlaps__(cp_gray))
print("Violet overlaps plane: ", cp_violet.__overlaps__(plane))
print("Plane overlaps violet: ", plane.__overlaps__(cp_gray))

r = Renderer()
r.add((cp_blue, 'b', 1), normal_length=0)
r.add((cp_violet, 'violet', 1), normal_length=0)
r.add((cp_gray, 'gray', 1), normal_length=0)
r.add((plane, 'y', 1), normal_length=0)
r.show()


# polygons
r1 = Renderer()
a = Point(1, 1, 0.5)
b = Point(2, 1, 0.5)
c = Point(2, 2, 0.5)
d = Point(1, 2, 0.5)
s = Segment(b,d)
p = Point(b)
plane_2 = ConvexPolygon((a, b, c, d))
r1.add((plane, 'y', 1), normal_length=0)
r1.add((plane_2, 'g', 1), normal_length=0)
r1.add((s, 'r', 1), normal_length=0)
r1.add((p, 'black', 10), normal_length=0)

r1.show()


print("Yellow overlaps green: ", plane.__overlaps__(plane_2))  # true: simmetrica
print("Green overlaps yellow: ", plane_2.__overlaps__(plane))  # true: simmetrica
print("segment overlaps green: ", s.__overlaps__(plane_2))  # false: non sono della stessa dimensione
print("segment overlaps point: ", s.__overlaps__(p))  # false: non sono della stessa dimensione

# segments
r1 = Renderer()
a = Point(1, 1, 0.5)
b = Point(2, 1, 0.5)
c = Point(2, 2, 0.5)
d = Point(1, 2, 0.5)
s = Segment(b,d)
p = Point(b)
plane_2 = ConvexPolygon((a, b, c, d))
r1.add((plane, 'y', 1), normal_length=0)
r1.add((plane_2, 'g', 1), normal_length=0)
r1.add((s, 'r', 1), normal_length=0)
r1.add((p, 'black', 10), normal_length=0)
r1.show()


r2 = Renderer()
a = origin()
b = Point(0, 2, 0)

c = Point(0, 1, 0)

s1 = Segment(a, b)
s2 = Segment(c, b)

r2.add((s1, 'b', 1), normal_length=0)
r2.add((s2, 'r', 1), normal_length=0)
r2.show()
print("Blue overlaps red: ", s1.__overlaps__(s2))  # true: simmetrica
print("Red overlaps blue: ", s2.__overlaps__(s1))  # true: simmetrica
