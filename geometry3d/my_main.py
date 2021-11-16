
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
cp_gray = ConvexPolyhedron((cp_1, cp_2, cp_3, cp_4, cp_5, cp_6))
# r.add((cp_gray, 'y', 1), normal_length=0)
intersection_b_y = cp_blue.intersection(cp_gray)
print("blue intersection yellow: ", intersection_b_y)
area_inter = cp_blue.intersection(cp_gray).area()
area_blue = cp_blue.area()
area_yellow = cp_gray.area()

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
print("Blue touches orange: ", cp_blue.__touches__(cp_orange))
print("Orange touches blue: ", cp_orange.__touches__(cp_blue))

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
print("Blue disjoint violet: ", cp_blue.__disjoint__(cp_violet))

print(cp_blue)
interior = cp_blue.__interior__()
print(interior)
print(cp_blue)
print("Interior contains Segment(0, 0.6, 0),(0, 1, 0)): ", interior.__contains__(Segment(Point(0, 0.6, 0), Point(0, 1, 0))))
print("Interior contains Segment(1, 0.6, 0),(1, 1, 0)): ", interior.__contains__(Segment(Point(1, 0.6, 0), Point(1, 1, 0))))
print("Blue polyhedron contains Segment(1, 0.6, 0),(1, 1, 0)): ", cp_blue.__contains__(Segment(Point(1, 0.6, 0), Point(1, 1, 0))))
print("Interior contains point (0, 0, 0): ", interior.__contains__(Point(0, 0, 0)))
print("Blue polyhedron contains point (0, 0, 0): ", cp_blue.__contains__(Point(0, 0, 0)))
print("Interior contains point (0, 0.6, 0): ", interior.__contains__(Point(0, 0.6, 0)))
# r.add((interior, 'black', 1), normal_length=0)
# r.add((cp_violet.__interior__(), 'black', 1), normal_length=0)

import copy

red_pol = copy.deepcopy(cp_blue)
print("cross :", cp_blue.__crosses__(red_pol))


segment2 = Segment(Point(0,0,0), Point(2, 0, 0))

interior2 = segment2.__interior__()
print("Segmento_1: ", segment2)
print("Interior_1: ", interior2)

segment = Segment(Point(0,0,0), Point(2,2,2))
interior = segment.__interior__()
print("Segmento_2: ", segment)
print("Interior_2: ", interior)
print("Interior_2 contiene punto (0,0,0): ", interior2.__contains__(Point(0,0,0)))
print("Interior_2 contiene punto (2,2,2): ", interior2.__contains__(Point(2,2,2)))
# render = Renderer()
# render.add((segment2, 'b', 1), normal_length=0)
# render.add((interior2, 'r', 1), normal_length=0)
# render.show()

print(cp_blue.__interior__())
print(segment2.__interior__())

print("\n")
a = Point(0, 0, 0.5)
b = Point(2, 0, 0.5)
c = Point(2, 2, 0.5)
d = Point(0, 2, 0.5)
plane = ConvexPolygon((a, b, c, d))
print("Piano: ", plane)
# print("Interior del piano: ", plane.__interior__())
r.add((plane, 'y', 1), normal_length=0)
# r.add((plane.__interior__(), 'black', 1), normal_length=0)
#
# print("Interior del piano contains Point(1, 0 , 0.5): ", plane.__interior__().__contains__(Point(1, 0, 0.5)))
# print("Piano crosses poliedro blu: ", plane.__crosses__(cp_blue))
# print("Piano crosses poliedro viola: ", plane.__crosses__(cp_violet))
# print("Poliedro viola crosses piano: ", cp_violet.__crosses__(plane))
#

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
print(cp_gray)
r.add((cp_gray, 'gray', 1), normal_length=0)

print("Blue overlaps gray: ", cp_blue.__overlaps__(cp_gray))
print("Gray overlaps blue: ", cp_gray.__overlaps__(cp_blue))
print("Violet overlaps gray: ", cp_violet.__overlaps__(cp_gray))
print("Violet overlaps plane: ", cp_violet.__overlaps__(plane))
print("Plane overlaps violet: ", plane.__overlaps__(cp_gray))
r.show()


render = Renderer()
segment_1 = Segment(origin(), Point(2,2,2))
segment_2 = Segment(origin(), Point(1,1,1))
segment_3 = Segment(origin(), Point(2,0,0))

render.add((segment_2, 'r', 1), normal_length=0)
render.add((segment_1, 'b', 1), normal_length=0)
render.add((segment_3, 'g', 1), normal_length=0)
render.add((cp_blue, 'b', 1), normal_length=0)
print("Segment 1: ", segment_1)
print("Segment 2: ", segment_2)
print("Segment 3: ", segment_3)
print("Segment 1 overlaps segment 2: ", segment_1.__overlaps__(segment_2))
print("Segment 2 overlaps segment 1: ", segment_2.__overlaps__(segment_1))
print("Segment 1 overlaps segment 3: ", segment_1.__overlaps__(segment_3))
print("Segment 1 overlaps blue polyhedron: ", segment_1.__overlaps__(cp_blue))
render.show()

print(cp_blue.__contains__(segment_2))
print(cp_blue.__within__(segment_2))
print(plane.__within__(cp_blue))

a = Point(0, 0, 0.5)
b = Point(1, 0, 0.5)
c = Point(1, 1, 0.5)
d = Point(0, 1, 0.5)

cp_1 = ConvexPolygon((a, b, c, d))  # base inf
print(cp_1.__within__(cp_blue))
print(cp_blue.__contains__(cp_1))

