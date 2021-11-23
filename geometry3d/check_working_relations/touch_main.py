from geometry3d.Geometry3D import *
import copy
"""
Touch is a symmetric relation
It returns True if the only points shared between self and obj are on the
boundary of self and obj
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

r = Renderer()
r.add((cp_blue, 'b', 1), normal_length=0)
r.add((cp_red, 'r', 1), normal_length=0)
r.show()

# poliedro - poliedro
print("Blue touches red: ", cp_blue.__touches__(cp_red))  # false: l'intersezione ha dimensione 3 (ConvexPolyhedron)
print("\n")
r1 = Renderer()
cp_blue_copy = copy.deepcopy(cp_blue)
blue_2 = cp_blue_copy.move(Vector(2,0,0))
r1.add((cp_red, 'r', 1), normal_length=0)
r1.add((blue_2, 'b', 1), normal_length=0)
print("Blue touches red: ", blue_2.__touches__(cp_red))
r1.show()

# poliedro - segmento
print("\n")
s1 = Segment(b, Point(2, 1, 0))
r2 = Renderer()
r2.add((cp_red, 'r', 1), normal_length=0)
r2.add((s1, 'b', 1), normal_length=0)
print("red touches segment: ", cp_red.__touches__(s1))  # false: l'interior del segmento è all'interno dell'intersezione
r2.show()

# poliedro - segmento
# segmento - poliedro
print("\n")
s1 = Segment(b, Point(3, 0, 0))
r3 = Renderer()
r3.add((cp_red, 'r', 1), normal_length=0)
r3.add((s1, 'b', 1), normal_length=0)
print("red touches segment: ", cp_red.__touches__(s1))  # true
print("segment touches red: ", s1.__touches__(cp_red))
r3.show()

# poliedro - poliedro
print("\n")
r4 = Renderer()
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
r4.add((cp_orange, 'orange', 1), normal_length=0)
r4.add((cp_blue, 'blue', 1), normal_length=0)
print("Blue touches orange: ", cp_blue.__touches__(cp_orange))  # true: l'intersezione è un segmento
print("Orange touches blue: ", cp_orange.__touches__(cp_blue))
r4.show()

# poliedro - punto
print("\n")
a = origin()
b = Point(0.5,0.5,0)  # punto interno
r5 = Renderer()
r5.add((a, 'orange', 10), normal_length=0)
r5.add((b, 'r', 10), normal_length=0)
r5.add((cp_blue, 'blue', 1), normal_length=0)
print("point A touches blue: ", a.__touches__(cp_blue))  # true
print("blue touches point A: ", cp_blue.__touches__(a))  # true
print("point B touches blue: ", b.__touches__(cp_blue))  # false: punto interno
print("blue touches point B: ", cp_blue.__touches__(b))  # false: punto interno
r5.show()


# poliedro - poligono
# poligono - poligono
print("\n")

r6 = Renderer()

cp_1_copy = copy.deepcopy(cp_1)
cp1_2 = cp_1_copy.move(Vector(0,-1,0))

cp_1_copy_2 = copy.deepcopy(cp_1)
cp1_3 = cp_1_copy_2.move(Vector(-0.5,-1,0))

r6.add((cp_1, 'orange', 1), normal_length=0)
r6.add((cp1_2, 'red', 1), normal_length=0)
r6.add((cp1_3, 'green', 1), normal_length=0)
r6.add((cp_blue, 'blue', 1), normal_length=0)

print("orange touches blue: ", cp_1.__touches__(cp_blue))  # true
print("blue touches orange: ", cp_blue.__touches__(cp_1))  # true
print("blue touches red: ", cp_blue.__touches__(cp1_2))  # true
print("red touches blue: ", cp1_2.__touches__(cp_blue))  # true
print("blue touches green: ", cp_blue.__touches__(cp1_3))  # false
print("red touches green: ", cp1_2.__touches__(cp1_3))  # false
r6.show()

# poligono - segmento - punto
print("\n")
r7 = Renderer()
s = Segment(Point(1,0,0), Point(1,1,0))
p = Point(1,0,0)
p1 = Point(1, 0.1, 0)
r7.add((cp_1, 'orange', 1), normal_length=0)
r7.add((s, 'red', 1), normal_length=0)
r7.add((p, 'blue', 10), normal_length=0)
r7.add((p1, 'black', 10), normal_length=0)
print("orange touches red: ", cp_1.__touches__(s))  # true
print("red touches orange: ", s.__touches__(cp_1))  # true
print("blue touches orange: ", p.__touches__(cp_1))  # false
print("blue touches red: ", p.__touches__(s))  # true
print("black touches red: ", p1.__touches__(s))  # false: punto interno
print("red touches black: ", s.__touches__(p1))  # false: punto interno
r7.show()