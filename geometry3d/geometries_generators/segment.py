from geometry3d.Geometry3D import *
from geometry3d.global_variables import *
import copy


def generate_segments():
    generated_segments = []
    for factor in scale_factors:
        generated_segments.append(Segment(origin(), x_unit_vector()*factor))
        generated_segments.append(Segment(origin(), y_unit_vector()*factor))
        generated_segments.append(Segment(origin(), z_unit_vector()*factor))
    total_segments = []
    for segment in generated_segments:
        for i in range(0, space_dimension+1):
            for j in range(0, space_dimension+1):
                for k in range(0, space_dimension+1):
                    s = copy.deepcopy(segment)
                    total_segments.append(s.move(Vector(i, j, k)))
    return total_segments


if __name__ == "__main__":
    r = Renderer()
    segments = generate_segments()
    print(len(segments))
    for s in segments:
        r.add((s, 'r', 1), normal_length=0)
    r.show()
