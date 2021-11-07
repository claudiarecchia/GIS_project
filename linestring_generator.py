"""
    Generatore di spezzate con 3 o 4 segmenti
    Le spezzate non hanno necessità di essere coplanari
"""
from points_generator import get_points
from csv_utilities import write_nodes_to_file
import os.path
import global_variables


def check_uniqueness(lst):
    unique = True
    for i in range(len(lst)):
        for j in range(len(lst)):
            if i != j and lst[i] == lst[j]:
                unique = False
                return unique
    return unique


def generate_linestring_dim_3():
    points = get_points(global_variables.points_folder, global_variables.points_file)
    lines = []
    for i in range(0, len(points)):
        for j in range(0, len(points)):
            for k in range(0, len(points)):
                if check_uniqueness([points[i], points[j], points[k]]):
                    lines.append([points[i], points[j % len(points)], points[k % len(points)]])
    write_nodes_to_file(global_variables.linestrings_folder, lines, global_variables.three_nodes_file)
    return lines


def generate_linestring_dim_4():
    points = get_points(global_variables.points_folder, global_variables.points_file)
    lines = []
    for i in range(0, len(points)):
        for j in range(0, len(points)):
            for k in range(0, len(points)):
                for m in range(0, len(points)):
                    if check_uniqueness([points[i], points[j], points[k], points[m]]):
                        lines.append(
                            [points[i], points[j % len(points)], points[k % len(points)], points[m % len(points)]])
    write_nodes_to_file(global_variables.linestrings_folder, lines, global_variables.four_nodes_file)
    return lines


def generate_linestring_dim_5():
    points = get_points(global_variables.points_folder, global_variables.points_file)
    lines = []
    for i in range(0, len(points)):
        for j in range(0, len(points)):
            for k in range(0, len(points)):
                for m in range(0, len(points)):
                    for n in range(0, len(points)):
                        if check_uniqueness([points[i], points[j], points[k], points[m], points[n]]):
                            lines.append([points[i], points[j % len(points)], points[k % len(points)],
                                          points[m % len(points)], points[n % len(points)]])
    write_nodes_to_file(global_variables.linestrings_folder, lines, global_variables.five_nodes_file)
    return lines
