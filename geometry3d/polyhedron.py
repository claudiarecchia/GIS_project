from geometry3d.Geometry3D import *
from geometry3d.global_variables import *
import copy


def generate_polyhedrons():
    a = Point(0, 0, 0)
    b = Point(1, 0, 0)
    c = Point(1, 1, 0)
    d = Point(0, 1, 0)
    e = Point(0, 0, 1)
    f = Point(0, 1, 1)
    g = Point(1, 0, 1)
    h = Point(1, 1, 1)
    cp_1 = ConvexPolygon((a, b, c, d))  # base inf
    cp_3 = ConvexPolygon((a, b, e))
    cp_4 = ConvexPolygon((a, d, f, e))
    cp_5 = ConvexPolygon((b, c, f, e))
    cp_6 = ConvexPolygon((c, f, d))
    generated_polhedrons = []
    for factor in scale_factors:
        generated_polhedrons.append(Parallelepiped(origin(), x_unit_vector()*factor, y_unit_vector()*factor, z_unit_vector()*factor))
        generated_polhedrons.append(ConvexPolyhedron((
            ConvexPolygon((a.scale(factor), b.scale(factor), c.scale(factor), d.scale(factor))),
            ConvexPolygon((a.scale(factor), b.scale(factor), e.scale(factor))),
            ConvexPolygon((a.scale(factor), d.scale(factor), f.scale(factor), e.scale(factor))),
            ConvexPolygon((b.scale(factor), c.scale(factor), f.scale(factor), e.scale(factor))),
            ConvexPolygon((c.scale(factor), f.scale(factor), d.scale(factor)))
        )))

        generated_polhedrons.append(ConvexPolyhedron((
            ConvexPolygon((a.scale(factor), b.scale(factor), c.scale(factor), d.scale(factor))),
            ConvexPolygon((a.scale(factor), b.scale(factor), g.scale(factor))),
            ConvexPolygon((a.scale(factor), d.scale(factor), h.scale(factor), g.scale(factor))),
            ConvexPolygon((b.scale(factor), c.scale(factor), h.scale(factor), g.scale(factor))),
            ConvexPolygon((c.scale(factor), h.scale(factor), d.scale(factor)))
        )))
    total_pol = []
    for pol in generated_polhedrons:
        for i in range(0, space_dimension+1):
            for j in range(0, space_dimension+1):
                for k in range(0, space_dimension+1):
                    p = copy.deepcopy(pol)
                    total_pol.append(p.move(Vector(i, j, k)))
    return total_pol


if __name__ == "__main__":
    r = Renderer()
    pols = generate_polyhedrons()
    print(len(pols))
    for s in pols:
        r.add((s, 'r', 1), normal_length=0)
    r.show()


#
# cph = Parallelepiped(origin(), x_unit_vector()*2, y_unit_vector(), z_unit_vector())
#
# a = origin()
# b = Point(1, 0, 0)
# c = Point(1, 1, 0)
# d = Point(0, 1, 0)
# e = Point(0, 0, 1)
# f = Point(0, 1, 1)
# cp_1 = ConvexPolygon((a, b, c, d))  # base inf
# cp_3 = ConvexPolygon((a, b, e))
# cp_4 = ConvexPolygon((a, d, f, e))
# cp_5 = ConvexPolygon((b, c, f, e))
# cp_6 = ConvexPolygon((c, f, d))
# cp_blue = ConvexPolyhedron((cp_1, cp_3, cp_4, cp_5, cp_6))
#
#
# r = Renderer()
# # r.add((cph, 'r', 1), normal_length=0)
# r.add((cp_blue, 'r', 1), normal_length=0)
# r.add((cp_blue.__interior__(), 'black', 1), normal_length=0)
# r.show()
