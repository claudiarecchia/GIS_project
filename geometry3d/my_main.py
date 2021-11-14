
from geometry3d.Geometry3D import *

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

r = Renderer()
r.add((cp_blue, 'b', 1), normal_length=0)

conv_pol_1 = cp_red.convex_polygons
# for el in conv_pol_1:
#     print("uno:", cp_blue.__contains__(el))

print("\n")

# conv_pol_2 = cp_blue.convex_polygons
# print(cp_red)
# for el in conv_pol_2:
#     print(el, ": ", cp_red.__contains__(el))
#
# print(cp_red)
# print(cp_blue)
# print("Red contains blue: ", cp_red.__contains__(cp_blue))
# print("Blue within red: ", cp_blue.convex_polyhedron_within(cp_red))
# print("Red contains red: ", cp_red.__contains__(cp_red))
# print("Blue contains red: ", cp_blue.__contains__(cp_red))
# print("\n")
#
#
# conv_pol_3 = cp_green.convex_polygons
# print(cp_red)
# for el in conv_pol_3:
#     print(el, ": ", cp_red.__contains__(el))
# print(cp_red)
# print(cp_green)
# print("Red contains green: ", cp_red.__contains__(cp_green))
# print("Green contains red: ", cp_green.__contains__(cp_red))
# print("Green contains green: ", cp_green.__contains__(cp_green))

intersection_r_g = cp_red.intersection(cp_green)
print("red intersection green: ", intersection_r_g)
# r.add((intersection_r_g, 'black', 1), normal_length=0)
area_inter = cp_red.intersection(cp_green).area()
area_red = cp_red.area()
area_green = cp_green.area()

print("area red pol: ", area_red)
print("area green pol: ", area_green)
print("area intersection: ", area_inter)


# render = Renderer()
# polygons_inter = intersection_r_g.convex_polygons
# for el in polygons_inter:
#     print(el)
#
# render.add((intersection_r_g, 'black', 1), normal_length=0)
# render.show()


a = Point(1, 0, 0)
b = Point(2, 0, 0)
c = Point(2, 1, 0)
d = Point(1, 1, 0)
e = Point(1, 0, 1)
f = Point(2, 0, 1)
g = Point(2, 1, 1)
h = Point(1, 1, 1)
cp_1 = ConvexPolygon((a, b, c, d))  # base inf
cp_2 = ConvexPolygon((e, f, g, h))  # base sup
cp_3 = ConvexPolygon((a, b, f, e))
cp_4 = ConvexPolygon((b, c, g, f))
cp_5 = ConvexPolygon((c, d, g, h))
cp_6 = ConvexPolygon((d, a, h, e))
cp_yellow = ConvexPolyhedron((cp_1, cp_2, cp_3, cp_4, cp_5, cp_6))
# r.add((cp_yellow, 'y', 1), normal_length=0)
intersection_b_y = cp_blue.intersection(cp_yellow)
print("blue intersection yellow: ", intersection_b_y)
area_inter = cp_blue.intersection(cp_yellow).area()
area_blue = cp_blue.area()
area_yellow = cp_yellow.area()

# esempio di intersezione PIANO
print("area blue pol: ", area_blue)
print("area yellow pol: ", area_yellow)
print("area intersection: ", area_inter)





# esempio di intersezione LINEA
a = Point(1, 1, 0)
b = Point(2, 1, 0)
c = Point(2, 2, 0)
d = Point(1, 2, 0)
e = Point(1, 1, 1)
f = Point(2, 1, 1)
g = Point(2, 2, 1)
h = Point(1, 2, 1)
cp_1 = ConvexPolygon((a, b, c, d))  # base inf
cp_2 = ConvexPolygon((e, f, g, h))  # base sup
cp_3 = ConvexPolygon((a, b, f, e))
cp_4 = ConvexPolygon((b, c, g, f))
cp_5 = ConvexPolygon((c, d, g, h))
cp_6 = ConvexPolygon((d, a, h, e))
cp_orange = ConvexPolyhedron((cp_1, cp_2, cp_3, cp_4, cp_5, cp_6))
# r.add((cp_orange, 'orange', 1), normal_length=0)

intersection_b_o = cp_blue.intersection(cp_orange)
print("Blue intersection orange: ", intersection_b_o)
# print("dimension:", intersection_b_o.get_dimension())
print("Blue touches orange: ", cp_blue.convex_polyhedron_touches(cp_orange))
print("Orange touches blue: ", cp_orange.convex_polyhedron_touches(cp_blue))

# esempio di intersezione VUOTA
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
r.add((cp_violet, 'violet', 1), normal_length=0)
#
intersection_b_v = cp_blue.intersection(cp_violet)
print("Blue intersection violet: ", intersection_b_v)
print("Blue disjoint violet: ", cp_blue.convex_polyhedron_disjoint(cp_violet))

print(cp_blue)
interior = cp_blue.polyhedron_interior()
print(interior)
print(cp_blue)
print("Interior contains Segment(0, 0.6, 0),(0, 1, 0)): ", interior.__contains__(Segment(Point(0, 0.6, 0), Point(0, 1, 0))))
print("Interior contains Segment(1, 0.6, 0),(1, 1, 0)): ", interior.__contains__(Segment(Point(1, 0.6, 0), Point(1, 1, 0))))
print("Blue polyhedron contains Segment(1, 0.6, 0),(1, 1, 0)): ", cp_blue.__contains__(Segment(Point(1, 0.6, 0), Point(1, 1, 0))))
print("Interior contains point (0, 0, 0): ", interior.__contains__(Point(0, 0, 0)))
print("Blue polyhedron contains point (0, 0, 0): ", cp_blue.__contains__(Point(0, 0, 0)))
print("Interior contains point (0, 0.6, 0): ", interior.__contains__(Point(0, 0.6, 0)))
r.add((interior, 'black', 1), normal_length=0)
r.add((cp_violet.polyhedron_interior(), 'black', 1), normal_length=0)

import copy

red_pol = copy.deepcopy(cp_blue)
print("cross :", cp_blue.convex_polyhedron_crosses(red_pol))

vector = Vector(Point(0, 0, 0), Point(8, 0, 0))
print(vector)
vector = vector.__sub__(Vector(1, 0, 0))
print(vector)

segment = Segment(Point(0,0,0), Point(2,2,2))
v = Vector(segment.start_point, segment.end_point)
print(v)

segment2 = Segment(Point(2, 2, 2), Point(0, 0, 0))
v = Vector(segment2.start_point, segment2.end_point)
print(v)

segment2 = Segment(Point(0,0,0), Point(2, 0, 0))
segment2.get_interior()
segment = Segment(Point(0,0,0), Point(2,2,2))
segment.get_interior()





r.show()



