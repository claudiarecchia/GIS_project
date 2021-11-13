"""
    Generatore di poligoni in geometry3d
    Elementi con 3, 4 e 5 vertici
    Tre punti sono sempre complanari
    Per elementi con 4 e 5 vertici si utilizza una funzione capace di
    comprendere se 4 punti appartengono allo stesso piano
    https://www.geeksforgeeks.org/program-to-check-whether-4-points-in-a-3-d-plane-are-coplanar/
"""
from pygeos_and_shapely.csv_utilities import *
from pygeos_and_shapely.linestring_generator import *
from pygeos_and_shapely import global_variables


def get_values(folder, filename):
    arr = read_nodes_file(folder, filename)
    points = get_int_values(arr)
    return points


def get_coplanar_polygons(folder, filename):
    arr = read_nodes_file(folder, filename)
    polygons_points = get_int_values(arr)
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
    if a * x + b * y + c * z + d == 0:
        coplanar = True
    else:
        coplanar = False
    return coplanar


def generate_polygons_3_points():
    triangles = get_values(global_variables.linestrings_folder, global_variables.three_nodes_file)
    write_nodes_to_file(global_variables.coplanar_polygons_folder, triangles, global_variables.three_nodes_file)
    return triangles


def generate_collinear_polygons_4_points():
    values = get_values(global_variables.linestrings_folder, global_variables.four_nodes_file)
    squares = []
    for line in values:
        if are_coplanar(line):
            squares.append(line)
    write_nodes_to_file(global_variables.coplanar_polygons_folder, squares, global_variables.four_nodes_file)
    return squares


def generate_collinear_polygons_5_points():
    values = get_values(global_variables.linestrings_folder, global_variables.five_nodes_file)
    pentagons = []
    for line in values:
        if are_coplanar([line[0], line[1], line[2], line[3]]) and are_coplanar([line[1], line[2], line[3], line[4]]):
            pentagons.append(line)
    write_nodes_to_file(global_variables.coplanar_polygons_folder, pentagons, global_variables.five_nodes_file)
    return pentagons


