from geometry3d.Geometry3D import *
from geometry3d.global_variables import *
import copy
from geometry3d.segment import *
import random
from geometry3d.polygon import *
from geometry3d.polyhedron import *
import numpy as np
import pandas as pd


def init_matrix():
    A = np.empty((len(relation_names), len(relation_names)), dtype=np.chararray).reshape(len(relation_names), len(relation_names))
    names = [_ for _ in relation_names]
    df = pd.DataFrame(A, index=names, columns=names)
    return df


def init_and_select_geometries():
    segments = generate_segments()
    polygons = generate_polygons()
    polyhedrons = generate_polyhedrons()
    all_generated_geometries = segments + polygons + polyhedrons
    geoms = []
    for i in range(0, geometries_to_consider):
        geoms.append(all_generated_geometries[random.randint(0, len(all_generated_geometries) - 1)])
    return geoms


def get_relations_results(element1, element2):
    name_true_relation = ""
    trues = []
    if element1.__crosses__(element2):
        name_true_relation = "CR"
        if isinstance(element1, ConvexPolyhedron):
            e1 = (element1.convex_polygons)
        else: e1 = element1
        if isinstance(element2, ConvexPolyhedron):
            e2 = (element2.convex_polygons)
        else: e2 = element2
        trues.append([name_true_relation, e1, e2])
    if element1.__contains__(element2):
        name_true_relation = "CO"
        if isinstance(element1, ConvexPolyhedron):
            e1 = (element1.convex_polygons)
        else:
            e1 = element1
        if isinstance(element2, ConvexPolyhedron):
            e2 = (element2.convex_polygons)
        else:
            e2 = element2
        trues.append([name_true_relation, e1, e2])
    if element1.__disjoint__(element2):
        name_true_relation = "DI"
        if isinstance(element1, ConvexPolyhedron):
            e1 = (element1.convex_polygons)
        else:
            e1 = element1
        if isinstance(element2, ConvexPolyhedron):
            e2 = (element2.convex_polygons)
        else:
            e2 = element2
        trues.append([name_true_relation, e1, e2])
    if element1.__overlaps__(element2):
        name_true_relation = "OV"
        if isinstance(element1, ConvexPolyhedron):
            e1 = (element1.convex_polygons)
        else:
            e1 = element1
        if isinstance(element2, ConvexPolyhedron):
            e2 = (element2.convex_polygons)
        else:
            e2 = element2
        trues.append([name_true_relation, e1, e2])
    if element1.__touches__(element2):
        name_true_relation = "TO"
        if isinstance(element1, ConvexPolyhedron):
            e1 = (element1.convex_polygons)
        else:
            e1 = element1
        if isinstance(element2, ConvexPolyhedron):
            e2 = (element2.convex_polygons)
        else:
            e2 = element2
        trues.append([name_true_relation, e1, e2])
    if element1.__within__(element2):
        name_true_relation = "WI"
        if isinstance(element1, ConvexPolyhedron):
            e1 = (element1.convex_polygons)
        else:
            e1 = element1
        if isinstance(element2, ConvexPolyhedron):
            e2 = (element2.convex_polygons)
        else:
            e2 = element2
        trues.append([name_true_relation, e1, e2])
    if element1.__eq__(element2):
        name_true_relation = "EQ"
        if isinstance(element1, ConvexPolyhedron):
            e1 = (element1.convex_polygons)
        else:
            e1 = element1
        if isinstance(element2, ConvexPolyhedron):
            e2 = (element2.convex_polygons)
        else:
            e2 = element2
        trues.append([name_true_relation, e1, e2])
    if len(trues) > 1:
        print(trues)
        exit()
    if len(trues) == 0:
        if isinstance(element1, ConvexPolyhedron):
            print(element1.convex_polygons)
        else:
            print(element1)

        if isinstance(element2, ConvexPolyhedron):
            print(element2.convex_polygons)
        else:
            print(element2)
    # else:
    #     print(element1, element2)
    #     if isinstance(element1, ConvexPolyhedron):
    #         print(element1.convex_polygons)
    #     if isinstance(element2, ConvexPolyhedron):
    #         print(element2.convex_polygons)
    #     exit()

    return name_true_relation


def calculate_matrix_values(geoms, df):
    iter = 0
    for i in range(len(geoms)):
        for j in range(len(geoms)):
            for k in range(len(geoms)):
                if i != j and j != k and k != i:
                    # print(geoms[i], geoms[j], geoms[k])
                    # print(geoms[i], geoms[j])
                    # print(geoms[j], geoms[k])
                    # print(geoms[i], geoms[k])
                    iter = iter + 1
                    relation_AB = get_relations_results(geoms[i], geoms[j])
                    relation_BC = get_relations_results(geoms[j], geoms[k])
                    relation_AC = get_relations_results(geoms[i], geoms[k])

                    if iter == 1:
                        if geoms[i].get_dimension() == 3:
                            print("Geometria A: ", geoms[i].convex_polygons)
                        else:
                            print("Geometria A: ", geoms[i])
                        if geoms[j].get_dimension() == 3:
                            print("Geometria B: ", geoms[j].convex_polygons)
                        else:
                            print("Geometria A: ", geoms[j])
                        if geoms[k].get_dimension() == 3:
                            print("Geometria C: ", geoms[k].convex_polygons)
                        else:
                            print("Geometria A: ", geoms[k])

                        print("Relazione A_B: ", relation_AB)
                        print("Relazione B_C: ", relation_BC)
                        print("Relazione A_C: ", relation_AC)


                    if df[relation_AB][relation_BC]:
                        if relation_AC not in df[relation_AB][relation_BC]:
                            df[relation_AB][relation_BC] = df[relation_AB][relation_BC] + " " + relation_AC
                    else:
                        df[relation_AB][relation_BC] = relation_AC
    df.to_csv('geometry3d/experiments/1/1.csv', index=True, header=True, sep=' ')


if __name__ == "__main__":
    df = init_matrix()
    geoms = init_and_select_geometries()
    calculate_matrix_values(geoms, df)
