from geometry3d.Geometry3D import *

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

# CLARIFY: relazione within: in questo caso i due boundary si toccano
#   si dovrebbe considerare la relazione within in cui si esclude che i
#   boundary si tocchino?
print("Blue within red: ", cp_blue.__within__(cp_red))  #  true
print("Red within blue: ", cp_red.__within__(cp_blue))
print("Red contains blue: ", cp_red.__contains__(cp_blue))
print("\n")

# ConvexPolygons
a = Point(0, 0, 0.5)
b = Point(2, 0, 0.5)
c = Point(2, 2, 0.5)
d = Point(0, 2, 0.5)
plane = ConvexPolygon((a, b, c, d))
r.add((plane, 'y', 1), normal_length=0)
# CLARIFY anche in questi casi i boundary si toccano
print("Plane within blue: ", plane.__within__(cp_blue))
print("Plane within red: ", plane.__within__(cp_red))  # true


print("\n")
r2 = Renderer()
a = Point(0.5, 0.5, 0.5)
b = Point(2, 0.5, 0.5)
c = Point(2, 2, 0.5)
d = Point(0.5, 2, 0.5)
orange = ConvexPolygon((a, b, c, d))
r2.add((orange, 'orange', 1), normal_length=0)
r2.add((plane, 'y', 1), normal_length=0)
# CLARIFY anche in questi casi i boundary si toccano
print("Orange within yellow: ", orange.__within__(plane))
print("Yellow within orange: ", plane.__within__(orange))


a = Point(0.5, 0.5, 0.5)
b = Point(1, 0.5, 0.5)
c = Point(1, 1, 0.5)
d = Point(0.5, 1, 0.5)
plane3 = ConvexPolygon((a, b, c, d))
r2.add((plane3, 'red', 1), normal_length=0)
print("Red within yellow: ", plane3.__within__(plane))
print("\n")

# Segments
r3 = Renderer()
segment_1 = Segment(origin(), Point(2,2,2))
segment_2 = Segment(origin(), Point(1,1,1))
segment_3 = Segment(origin(), Point(2,0,0))

#  CLARIFY i due segmenti verificano within e overlaps
#   condividono il primo punto del segmento (boundary)
#   => within senza boundary?
r3.add((segment_2, 'r', 1), normal_length=0)
r3.add((segment_1, 'b', 1), normal_length=0)
print("SEGMENT red within blue: ", segment_2.__within__(segment_1))
print("Red overlaps blue: ", segment_2.__overlaps__(segment_1))

print("\n")
# Points
a = Point(0.5, 0.5, 0.5)
b = Point(1, 0.5, 0.5)
c = Point(0.5, 0.5, 0.5)
#  CLARIFY due punti possono verificare la within solo se sono uguali
#   ma se sono uguali sarà verificata la EQ => due punti sono sono mai in within
#   (ma dovrebbero esserlo= https://community.esri.com/t5/python-questions/how-to-use-the-geometry-within-function-in-arcpy/td-p/66834)
print("A within B: ", a.__within__(b))
print("A within C: ", a.__within__(c))
print("A equals C: ", a.__eq__(c))

r4 = Renderer()
r4.add((cp_red, 'r', 1), normal_length=0)
r4.add((plane, 'y', 1), normal_length=0)
r4.add((a, 'b', 10), normal_length=0)
print("A within red polyhedron: ", a.__within__(cp_red))
print("A within yellow plane: ", a.__within__(plane))
print("Yellow plane contains point a: ", plane.__contains__(a))

s = Segment(Point(0, 0.5, 0.5), Point(2, 0.5, 0.5))
r4.add((s, 'g', 1), normal_length=0)
print("A within segment ", s, a.__within__(s))  # true: il punto è un punto intermedio del segmento

s = Segment(a, Point(2, 0.5, 0.5))
r4.add((s, 'black', 1), normal_length=0)
print("A within segment ", s,  a.__within__(s))  # false: il punto coincide con il primo punto del segmento
r.show()
r2.show()
r3.show()
r4.show()
