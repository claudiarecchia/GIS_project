"""
    File contenente funzioni che vengono eseguite alla prima esecuzione
    del programma su una macchina
    Crea le cartelle e i files necessari da utilizzare come dataset
    basandosi sui nomi presenti nel file global_variables.py
    Se si vuole creare un nuovo dataset, sarà necessario cambiare
    il valore della variabile trials_folder in global_variables.py
"""

from pathlib import Path
import os
from pygeos_and_shapely.points_generator import generate_points
from pygeos_and_shapely.trials_generator import *


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