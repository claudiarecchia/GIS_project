"""
    Generatore di poligoni in 3D
    Triangoli, quadrati, pentagoni
    Tre punti sono sempre coplanari
    Per quadrati e pentagoni si utilizzerà una funzione capace di
    comprendere se 4 punti appartengono allo stesso piano
    https://www.geeksforgeeks.org/program-to-check-whether-4-points-in-a-3-d-plane-are-coplanar/
"""
from csv_utilities import *
from linestring_generator import *


def get_or_create_values(filename):
    if os.path.isfile("linestrings/" + filename + ".csv"):
        print("OK")
        arr = read_nodes_file("linestrings", filename)
        points = get_int_values(arr)
    else:
        print("QUI")
        if "three" in filename:
            generate_linestring_dim_3()
            nodes_arrays = read_nodes_file("linestrings", "three_nodes")
            points = get_int_values(nodes_arrays)
        elif "four" in filename:
            generate_linestring_dim_4()
            nodes_arrays = read_nodes_file("linestrings", "four_nodes")
            points = get_int_values(nodes_arrays)
        elif "five" in filename:
            generate_linestring_dim_5()
            nodes_arrays = read_nodes_file("linestrings", "four_nodes")
            points = get_int_values(nodes_arrays)
    return points


def get_or_create_coplanar_polygons(filename):
    if os.path.isfile("coplanar_polygons/" + filename + ".csv"):
        print("OK")
        arr = read_nodes_file("coplanar_polygons", filename)
        polygons_points = get_int_values(arr)
    else:
        print("DA CREARE")
        if "three" in filename or "3" in filename:
            polygons_points = get_polygons_3_points()
        elif "four" in filename or "4" in filename:
            polygons_points = get_collinear_polygons_4_points()
        elif "five" in filename or "5" in filename:
            polygons_points = get_collinear_polygons_5_points()
    return polygons_points


def are_coplanar(vertices):
    x1 = vertices[0][0]
    y1 = vertices[0][1]
    z1 = vertices[0][2]

    x2 = vertices[1][0]
    y2 = vertices[1][1]
    z2 = vertices[1][2]

    x3 = vertices[2][0]
    y3 = vertices[2][1]
    z3 = vertices[2][2]

    x = vertices[3][0]
    y = vertices[3][1]
    z = vertices[3][2]

    a1 = x2 - x1
    b1 = y2 - y1
    c1 = z2 - z1
    a2 = x3 - x1
    b2 = y3 - y1
    c2 = z3 - z1
    a = b1 * c2 - b2 * c1
    b = a2 * c1 - a1 * c2
    c = a1 * b2 - b1 * a2
    d = (- a * x1 - b * y1 - c * z1)

    # equation of plane is: a*x + b*y + c*z = 0 #
    # checking if the 4th point satisfies
    # the above equation
    if (a * x + b * y + c * z + d == 0):
        # print("Coplanar")
        coplanar = True
    else:
        # print("Not Coplanar")
        coplanar = False
    return coplanar


def get_polygons_3_points():
    triangles = get_or_create_values("three_nodes")
    write_nodes_to_file("coplanar_polygons", triangles, "three_nodes")
    return triangles


def get_collinear_polygons_4_points():
    values = get_or_create_values("four_nodes")
    squares = []
    for line in values:
        if are_coplanar(line):
            squares.append(line)
    write_nodes_to_file("coplanar_polygons", squares, "four_nodes")
    return squares


def get_collinear_polygons_5_points():
    values = get_or_create_values("five_nodes")
    pentagons = []
    for line in values:
        if are_coplanar([line[0], line[1], line[2], line[3]]) and are_coplanar([line[1], line[2], line[3], line[4]]):
            pentagons.append(line)
    write_nodes_to_file("coplanar_polygons", pentagons, "five_nodes")
    return pentagons


