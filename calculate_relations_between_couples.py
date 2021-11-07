"""
    Avendo ottenuto i diversi oggetti trials
    Si procede con il confronto tra di essi, due a due
    per determinare infine la tabella di composizione
"""

import global_variables
from csv_utilities import *
from shapely.geometry import *
from pygeos import *
import numpy as np
import sys


def pretty_print(mat):
    template = "{0:10}{1:10}{2:10}{3:10}{4:10}{5:10}{6:10}{7:10}{8:10}{9:10}"
    print(template.format(" ", "B_C1", "B_C2", "B_C3", "B_C4", "B_C5", "B_C6", "B_C7", "B_C8", "B_C9"))  # header
    for rec in mat:
        print(template.format(*rec))


def check_JEPD_relations(element1, element2):
    JEPD = True
    cross = crosses(element1, element2)
    contain = contains(element1, element2)
    disj = disjoint(element1, element2)
    overlap = overlaps(element1, element2)
    touch = touches(element1, element2)
    wit = within(element1, element2)
    equal = equals(element1, element2)

    if sum([cross, contain, disj, overlap, touch, wit, equal]) > 1:
        JEPD = False
    return JEPD


def get_relations_results(element1, element2):
    name_true_relation = ""

    if crosses(element1, element2):
        name_true_relation = "crosses"
    elif contains(element1, element2):
        name_true_relation = "contains"
    elif disjoint(element1, element2):
        name_true_relation = "disjoint"
    elif overlaps(element1, element2):
        name_true_relation = "overlaps"
    elif touches(element1, element2):
        name_true_relation = "touches"
    elif within(element1, element2):
        name_true_relation = "within"
    elif equals(element1, element2):
        name_true_relation = "equals"

    # print("crosses:", crosses(element1, element2))
    # print("contains:", contains(element1, element2))
    # print("disjoint:", disjoint(element1, element2))
    # print("overlaps:", overlaps(element1, element2))
    # print("touches:", touches(element1, element2))
    # print("within: ", within(element1, element2))
    # print("equals: ", equals(element1, element2))

    return name_true_relation


def exit_if_not_JEPD(points, linestrings, polygons):
    results = []
    for point in points:
        point = from_shapely(Point(point))
        for linestring in linestrings:
            linestring = from_shapely(LineString(linestring))
            results.append(check_JEPD_relations(point, linestring))  # AB
            for poly in polygons:
                poly = from_shapely(Polygon(poly))
                results.append(get_relations_results(linestring, poly))  # BC
                results.append(get_relations_results(point, poly))  # AC
    if False in results:
        sys.exit("Le relazioni identificate non risultano essere JEPD.")
    else:
        print("Le relazioni sono JEPD. Si procede con il calcolo delle tabelle di composizione.")


def calculate_composition_tables(points, linestrings, polygons):
    # per ogni terna A,B,C (con C = x, cioè variabile) devo creare una nuova tabella
    n_entries_rows = 2
    n_entries_cols = len(polygons) + 1
    matrices = []
    col = 0
    index = 0
    mat = np.empty((n_entries_rows, n_entries_cols), dtype=np.chararray)
    mat[0][0] = "A_B"
    for point in points:
        point = from_shapely(Point(point))
        for linestring in linestrings:
            col = 0
            index = 0
            mat = np.empty((n_entries_rows, n_entries_cols), dtype=np.chararray)
            mat[0][0] = "A_B"
            linestring = from_shapely(LineString(linestring))  # AB
            mat[1][0] = get_relations_results(point, linestring)
            for poly in polygons:
                col += 1
                poly = from_shapely(Polygon(poly))
                mat[0][col] = get_relations_results(linestring, poly)  # BC
                mat[1][col] = get_relations_results(point, poly)  # AC
            matrices.append(mat)
            pretty_print(mat)
            print(
                "-------------------------------------------------------------------------------------------------------")
        print("Numero tabelle di composizione generate:", len(matrices))


# if __name__ == "__main__":
#     polygons, linestrings, points = [], [], []
#     points_strings = read_nodes_file(global_variables.trials_folder, "points")
#     points = get_int_values(points_strings)
#
#     for file in global_variables.linestrings:
#         points_strings = read_nodes_file(global_variables.trials_folder, file)
#         linestrings.extend(get_int_values(points_strings))
#
#     for file in global_variables.polygons:
#         points_strings = read_nodes_file(global_variables.trials_folder, file)
#         polygons.extend(get_int_values(points_strings))
#
#     exit_if_not_JEPD(points, linestrings, polygons)
#     calculate_composition_tables(points, linestrings, polygons)

