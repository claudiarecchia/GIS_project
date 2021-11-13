from Geometry3D import *


def convex_polyhedron_contains(cp_1, cp_2):
    """
    **Input:**

    - cp_1: a ConvexPolyhedron
    - cp_2: a ConvexPolyhedron

    **Output:**
    - Whether the polyhedron cp_1 contains the polyhedron cp_2 and
        cp_1!=cp_2 (contains - equals)
    """
    result = True
    polygons = cp_2.convex_polygons
    for pol in polygons:
        if not cp_1.__contains__(pol):
            result = False
    if cp_1.__eq__(cp_2):  # cp_1!=cp_2 (contains - equals)
        result = False
    return result
