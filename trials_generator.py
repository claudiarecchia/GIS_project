from linestring_generator import *
import random
from polygon_generator import *
from pygeos import *
from shapely.geometry import *


def create_points():
    global _, index
    points = get_or_create_points("points")
    selected_points = []
    for _ in range(0, 10):
        index = random.randint(0, len(points))
        selected_points.append(points[index])
    write_nodes_to_file("trials_1", selected_points, "points")


def create_linestrings_3():
    global _, index
    values_3 = get_or_create_values("three_nodes")
    selected_linestrings_3 = []
    for _ in range(0, 3):
        index = random.randint(0, len(values_3))
        selected_linestrings_3.append(values_3[index])
    write_nodes_to_file("trials_1", selected_linestrings_3, "linestrings_3")


def create_linestrings_4():
    global _, index
    values_4 = get_or_create_values("four_nodes")
    selected_linestrings_4 = []
    for _ in range(0, 3):
        index = random.randint(0, len(values_4))
        selected_linestrings_4.append(values_4[index])
    write_nodes_to_file("trials_1", selected_linestrings_4, "linestrings_4")


def create_linestrings_5():
    global _, index
    values_5 = get_or_create_values("five_nodes")
    selected_linestrings_5 = []
    for _ in range(0, 3):
        index = random.randint(0, len(values_5))
        selected_linestrings_5.append(values_5[index])
    write_nodes_to_file("trials_1", selected_linestrings_5, "linestrings_5")


def create_polygons_3():
    global _, index
    values_poly_3 = get_or_create_coplanar_polygons("three_nodes")
    selected_poly_3 = []
    for _ in range(0, 3):
        index = random.randint(0, len(values_poly_3))
        selected_poly_3.append(values_poly_3[index])

    write_nodes_to_file("trials_1", selected_poly_3, "polygons_3")


def create_polygons_4():
    global _, index
    values_poly_4 = get_or_create_coplanar_polygons("four_nodes")
    selected_poly_4 = []
    counter = 0
    while counter < 3:
        index = random.randint(0, len(values_poly_4))
        if is_simple(from_shapely(Polygon(values_poly_4[index]))):
            selected_poly_4.append(values_poly_4[index])
            counter += 1

    write_nodes_to_file("trials_1", selected_poly_4, "polygons_4")


def create_polygons_5():
    global _, index
    values_poly_5 = get_or_create_coplanar_polygons("five_nodes")
    selected_poly_5 = []
    counter = 0
    while counter < 3:
        index = random.randint(0, len(values_poly_5))
        if is_simple(from_shapely(Polygon(values_poly_5[index]))):
            selected_poly_5.append(values_poly_5[index])
            counter += 1

    write_nodes_to_file("trials_1", selected_poly_5, "polygons_5")


create_polygons_5()