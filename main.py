

from pathlib import Path
import global_variables
import os
from points_generator import generate_points
from linestring_generator import *
from polygon_generator import *
from trials_generator import *
from calculate_relations_between_couples import *


def create_folders():
    Path("./" + global_variables.points_folder).mkdir(parents=True, exist_ok=True)
    Path("./" + global_variables.linestrings_folder).mkdir(parents=True, exist_ok=True)
    Path("./" + global_variables.coplanar_polygons_folder).mkdir(parents=True, exist_ok=True)
    Path("./" + global_variables.trials_folder).mkdir(parents=True, exist_ok=True)


def create_trials_folder():
    Path("./" + global_variables.trials_folder).mkdir(parents=True, exist_ok=True)


def create_all_values():
    if not os.path.exists("./" + global_variables.points_folder + "/" + global_variables.points_file):
        generate_points(2, global_variables.points_folder, global_variables.points_file)
    if not os.path.exists("./" + global_variables.linestrings_folder + "/" + global_variables.three_nodes_file):
        generate_linestring_dim_3()
    if not os.path.exists("./" + global_variables.linestrings_folder + "/" + global_variables.four_nodes_file):
        generate_linestring_dim_4()
    if not os.path.exists("./" + global_variables.linestrings_folder + "/" + global_variables.five_nodes_file):
        generate_linestring_dim_5()
    if not os.path.exists("./" + global_variables.coplanar_polygons_folder + "/" + global_variables.three_nodes_file):
        generate_polygons_3_points()
    if not os.path.exists("./" + global_variables.coplanar_polygons_folder + "/" + global_variables.four_nodes_file):
        generate_collinear_polygons_4_points()
    if not os.path.exists("./" + global_variables.coplanar_polygons_folder + "/" + global_variables.five_nodes_file):
        generate_collinear_polygons_5_points()


def create_trials():
    if not os.path.exists("./" + global_variables.trials_folder + "/" + global_variables.points_file):
        create_points()
    if not os.path.exists("./" + global_variables.trials_folder + "/" + global_variables.lin_3):
        create_linestrings_3()
    if not os.path.exists("./" + global_variables.trials_folder + "/" + global_variables.lin_4):
        create_linestrings_4()
    if not os.path.exists("./" + global_variables.trials_folder + "/" + global_variables.lin_5):
        create_linestrings_5()
    if not os.path.exists("./" + global_variables.trials_folder + "/" + global_variables.pol_3):
        create_polygons_3()
    if not os.path.exists("./" + global_variables.trials_folder + "/" + global_variables.pol_4):
        create_polygons_4()
    if not os.path.exists("./" + global_variables.trials_folder + "/" + global_variables.pol_5):
        create_polygons_5()


if __name__ == "__main__":
    create_folders()
    create_all_values()
    create_trials_folder()
    create_trials()

    polygons, linestrings, points = [], [], []
    points_strings = read_nodes_file(global_variables.trials_folder, global_variables.points_file)
    points = get_int_values(points_strings)

    for file in global_variables.linestrings:
        points_strings = read_nodes_file(global_variables.trials_folder, file)
        linestrings.extend(get_int_values(points_strings))

    for file in global_variables.polygons:
        points_strings = read_nodes_file(global_variables.trials_folder, file)
        polygons.extend(get_int_values(points_strings))

    exit_if_not_JEPD(points, linestrings, polygons)
    calculate_composition_tables(points, linestrings, polygons)

