"""
    Generatore di spezzate con 3 o 4 segmenti
    Le spezzate non hanno necessità di essere coplanari
"""

from points_generator import generate_points
from csv_utilities import *
import os.path


def check_uniqueness(lst):
    unique = True
    for i in range(len(lst)):
        for j in range(len(lst)):
            if i != j and lst[i] == lst[j]:
                unique = False
                return unique
    return unique


def get_or_create_points(filename):
    if os.path.isfile("points/" + filename + ".csv"):
        print("OK")
        arr = read_nodes_file("points", filename)
        points = get_int_values(arr)
    else:
        points = generate_points(2)
    return points


def generate_linestring_dim_3():
    points = get_or_create_points("points")
    lines = []
    for i in range(0, len(points)):
        for j in range(0, len(points)):
            for k in range(0, len(points)):
                if check_uniqueness([points[i], points[j], points[k]]):
                    lines.append([points[i], points[j % len(points)], points[k % len(points)]])
    write_nodes_to_file("linestrings", lines, "three_nodes")
    return lines


def generate_linestring_dim_4():
    points = get_or_create_points("points")
    lines = []
    for i in range(0, len(points)):
        for j in range(0, len(points)):
            for k in range(0, len(points)):
                for m in range(0, len(points)):
                    if check_uniqueness([points[i], points[j], points[k], points[m]]):
                        lines.append(
                            [points[i], points[j % len(points)], points[k % len(points)], points[m % len(points)]])
    write_nodes_to_file("linestrings", lines, "four_nodes")
    return lines


def generate_linestring_dim_5():
    points = get_or_create_points("points")
    lines = []
    for i in range(0, len(points)):
        for j in range(0, len(points)):
            for k in range(0, len(points)):
                for m in range(0, len(points)):
                    for n in range(0, len(points)):
                        if check_uniqueness([points[i], points[j], points[k], points[m], points[n]]):
                            lines.append([points[i], points[j % len(points)], points[k % len(points)],
                                          points[m % len(points)], points[n % len(points)]])
    write_nodes_to_file("linestrings", lines, "five_nodes")
    return lines


if __name__ == "__main__":
    generate_linestring_dim_5()
    # nodes_arrays = read_nodes_file("linestrings", "three_nodes")
    # list = get_int_values(nodes_arrays)
    # for el in list:
    #     print(el)