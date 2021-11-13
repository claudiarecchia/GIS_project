
from Geometry3D import *
from geometry3d.my_functions import *

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
print(cp_blue)

a = origin()
b = Point(2, 0, 0)
c = Point(2, 2, 0)
d = Point(0, 2, 0)
e = Point(0, 0, 2)
f = Point(2, 0, 2)
g = Point(2, 2, 2)
h = Point(0, 2, 2)
cp_1 = ConvexPolygon((a, b, c, d))  # base inf
cp_2 = ConvexPolygon((e, f, g, h))  # base sup
cp_3 = ConvexPolygon((a, b, f, e))
cp_4 = ConvexPolygon((b, c, g, f))
cp_5 = ConvexPolygon((c, d, g, h))
cp_6 = ConvexPolygon((d, a, h, e))
cp_red = ConvexPolyhedron((cp_1, cp_2, cp_3, cp_4, cp_5, cp_6))

a = Point(0, 1, 0)
b = Point(2, 1, 0)
c = Point(2, 3, 0)
d = Point(0, 3, 0)
cp_1 = ConvexPolygon((a, b, c, d))  # base inf
e = Point(0, 1, 2)
f = Point(2, 1, 2)
g = Point(2, 3, 2)
h = Point(0, 3, 2)
cp_2 = ConvexPolygon((e, f, g, h))  # base sup
cp_3 = ConvexPolygon((a, b, f, e))
cp_4 = ConvexPolygon((b, c, g, f))
cp_5 = ConvexPolygon((c, d, g, h))
cp_6 = ConvexPolygon((d, a, h, e))
cp_green = ConvexPolyhedron((cp_1, cp_2, cp_3, cp_4, cp_5, cp_6))

# cph4 = intersection(cph1, cph2)
r = Renderer()
# r.add((cp_blue, 'b', 1), normal_length=0)
r.add((cp_red, 'r', 1), normal_length=0)
r.add((cp_green, 'g', 1), normal_length=0)
# r.add((cpg, 'r', 1), normal_length=0)
conv_pol_1 = cp_red.convex_polygons
for el in conv_pol_1:
    print("uno:", cp_blue.__contains__(el))

print("\n")

conv_pol_2 = cp_blue.convex_polygons
print(cp_red)
for el in conv_pol_2:
    print(el, ": ", cp_red.__contains__(el))

print(cp_red)
print(cp_blue)
print("Red contains blue: ", convex_polyhedron_contains(cp_red, cp_blue))
print("Red contains red: ", convex_polyhedron_contains(cp_red, cp_red))
print("Blue contains red: ", convex_polyhedron_contains(cp_blue, cp_red))
print("\n")


conv_pol_3 = cp_green.convex_polygons
print(cp_red)
for el in conv_pol_3:
    print(el, ": ", cp_red.__contains__(el))
print(cp_red)
print(cp_green)
print("Red contains green: ", convex_polyhedron_contains(cp_red, cp_green))
print("Green contains red: ", convex_polyhedron_contains(cp_green, cp_red))
print("Green contains green: ", convex_polyhedron_contains(cp_green, cp_green))

# print("tre:", cp.__eq__(cpp))
print("quattro:", cp_blue.intersection(cp_red))

# print(par_2.__contains__(pa))
# print(par_2.__contains__(Point(-1, -1, 0)))
r.show()
# cph.move(x_unit_vector())
# print(cph)
# r.add((cph, 'y', 1), normal_length=0)
# r.add((cph.move(z_unit_vector()), 'g', 1), normal_length=0)
# r.add((cph.move(y_unit_vector()), 'r', 1), normal_length=0)

# r.add((cph1, 'r', 1), normal_length=0.5)
# r.add((cph2, 'g', 1), normal_length=0)
# r.add((cph4, 'y', 3), normal_length=0.5)

