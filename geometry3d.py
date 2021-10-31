
from Geometry3D import *


a = Point(1,1,1)
b = Point(-1,1,1)
c = Point(-1,-1,1)
d = Point(1,-1,1)
e = Point(1,1,-1)
f = Point(-1,1,-1)
g = Point(-1,-1,-1)
h = Point(1,-1,-1)
cpg0 = ConvexPolygon((a,d,h,e))
cpg1 = ConvexPolygon((a,e,f,b))
cpg2 = ConvexPolygon((c,b,f,g))
cpg3 = ConvexPolygon((c,g,h,d))
cpg4 = ConvexPolygon((a,b,c,d))
cpg5 = ConvexPolygon((e,h,g,f))
cph0 = ConvexPolyhedron((cpg0,cpg1,cpg2,cpg3,cpg4,cpg5))
print(cph0)

r = Renderer(backend='matplotlib')
r.add((cph0,'y',1),normal_length=1)
r.show()