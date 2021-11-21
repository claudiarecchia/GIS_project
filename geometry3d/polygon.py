from geometry3d.Geometry3D import *
from geometry3d.global_variables import *
import copy


def generate_polygons():
    generated_polygons = []
    for factor in scale_factors:
        generated_polygons.append(Parallelogram(origin(), x_unit_vector()*factor, y_unit_vector()*factor))
        generated_polygons.append(Parallelogram(origin(), x_unit_vector()*factor, z_unit_vector()*factor))
        generated_polygons.append(Parallelogram(origin(), y_unit_vector()*factor, z_unit_vector()*factor))
        generated_polygons.append(ConvexPolygon((origin(), Point(1, 0, 0).scale(factor), Point(0.5, 1, 0).scale(factor))))

    total_pol = []
    for pol in generated_polygons:
        for i in range(0, space_dimension+1):
            for j in range(0, space_dimension+1):
                for k in range(0, space_dimension+1):
                    p = copy.deepcopy(pol)
                    total_pol.append(p.move(Vector(i, j, k)))
    return total_pol


if __name__ == "__main__":
    r = Renderer()
    pols = generate_polygons()
    print(len(pols))
    for s in pols:
        r.add((s, 'r', 1), normal_length=0)
    r.show()


# p1 = origin()
#
# v1 = x_unit_vector()
# v2 = z_unit_vector()
# p = Plane(p1, v1, v2)
#
# p = Parallelogram(origin(), x_unit_vector()*2, y_unit_vector()*2)
# t = ConvexPolygon((origin(), Point(1, 0, 0).scale(2), Point(0.5, 1, 0).scale(2)))
#
# r = Renderer()
# r.add((p, 'r', 1), normal_length=0)
# r.add((t, 'b', 1), normal_length=0)
# r.add((t.__interior__(), 'r', 1), normal_length=0)
#
# print(t)
# print(t.__interior__())
# # r.add((p.__interior__(), 'black', 1), normal_length=0)
# print(p)
# print(p.__interior__())
# r.show()
