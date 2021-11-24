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



