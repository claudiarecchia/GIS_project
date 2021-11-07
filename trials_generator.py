from linestring_generator import *
import random
from polygon_generator import *
from pygeos import *
from shapely.geometry import *
import global_variables


def create_points():
    points = get_points(global_variables.points_folder, global_variables.points_file)
    selected_points = []
    for _ in range(0, global_variables.number_trials_points):
        index = random.randint(0, len(points))
        selected_points.append(points[index])
    write_nodes_to_file(global_variables.trials_folder, selected_points, global_variables.points_file)


def create_linestrings_3():
    values_3 = get_values(global_variables.linestrings_folder, global_variables.three_nodes_file)
    selected_linestrings_3 = []
    for _ in range(0, global_variables.number_trials_linestrings):
        index = random.randint(0, len(values_3))
        selected_linestrings_3.append(values_3[index])
    write_nodes_to_file(global_variables.trials_folder, selected_linestrings_3, global_variables.lin_3)


def create_linestrings_4():
    values_4 = get_values(global_variables.linestrings_folder, global_variables.four_nodes_file)
    selected_linestrings_4 = []
    for _ in range(0, global_variables.number_trials_linestrings):
        index = random.randint(0, len(values_4))
        selected_linestrings_4.append(values_4[index])
    write_nodes_to_file(global_variables.trials_folder, selected_linestrings_4, global_variables.lin_4)


def create_linestrings_5():
    values_5 = (global_variables.linestrings_folder, global_variables.five_nodes_file)
    selected_linestrings_5 = []
    for _ in range(0, global_variables.number_trials_linestrings):
        index = random.randint(0, len(values_5))
        selected_linestrings_5.append(values_5[index])
    write_nodes_to_file(global_variables.trials_folder, selected_linestrings_5, global_variables.lin_5)


def create_polygons_3():
    values_poly_3 = get_coplanar_polygons(global_variables.coplanar_polygons_folder, global_variables.three_nodes_file)
    selected_poly_3 = []
    for _ in range(0, global_variables.number_trials_polygons):
        index = random.randint(0, len(values_poly_3))
        selected_poly_3.append(values_poly_3[index])

    write_nodes_to_file(global_variables.trials_folder, selected_poly_3, global_variables.pol_3)


def create_polygons_4():
    values_poly_4 = get_coplanar_polygons(global_variables.coplanar_polygons_folder, global_variables.four_nodes_file)
    selected_poly_4 = []
    counter = 0
    while counter < global_variables.number_trials_polygons:
        index = random.randint(0, len(values_poly_4))
        if is_simple(from_shapely(Polygon(values_poly_4[index]))):
            selected_poly_4.append(values_poly_4[index])
            counter += 1

    write_nodes_to_file(global_variables.trials_folder, selected_poly_4, global_variables.pol_4)


def create_polygons_5():
    values_poly_5 = get_coplanar_polygons(global_variables.coplanar_polygons_folder, global_variables.five_nodes_file)
    selected_poly_5 = []
    counter = 0
    while counter < global_variables.number_trials_polygons:
        index = random.randint(0, len(values_poly_5))
        if is_simple(from_shapely(Polygon(values_poly_5[index]))):
            selected_poly_5.append(values_poly_5[index])
            counter += 1

    write_nodes_to_file(global_variables.trials_folder, selected_poly_5, global_variables.pol_5)
