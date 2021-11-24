from geometry3d.geometries_generators.segment import *
import random
from geometry3d.geometries_generators.polygon import *
from geometry3d.geometries_generators.polyhedron import *
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
    geoms.extend(generate_set_polyhedrons())
    return geoms


def get_relations_results(element1, element2):
    name_true_relation = ""
    trues = []
    if element1.__crosses__(element2):
        name_true_relation = "CR"
        e1, e2 = get_convex_polygons_if_convex_polyhedrons(element1, element2)
        trues.append([name_true_relation, e1, e2])
    if element1.__contains__(element2):
        name_true_relation = "CO"
        e1, e2 = get_convex_polygons_if_convex_polyhedrons(element1, element2)
        trues.append([name_true_relation, e1, e2])
    if element1.__disjoint__(element2):
        name_true_relation = "DI"
        e1, e2 = get_convex_polygons_if_convex_polyhedrons(element1, element2)
        trues.append([name_true_relation, e1, e2])
    if element1.__overlaps__(element2):
        name_true_relation = "OV"
        e1, e2 = get_convex_polygons_if_convex_polyhedrons(element1, element2)
        trues.append([name_true_relation, e1, e2])
    if element1.__touches__(element2):
        name_true_relation = "TO"
        e1, e2 = get_convex_polygons_if_convex_polyhedrons(element1, element2)
        trues.append([name_true_relation, e1, e2])
    if element1.__within__(element2):
        name_true_relation = "WI"
        e1, e2 = get_convex_polygons_if_convex_polyhedrons(element1, element2)
        trues.append([name_true_relation, e1, e2])
    if element1.__eq__(element2):
        name_true_relation = "EQ"
        e1, e2 = get_convex_polygons_if_convex_polyhedrons(element1, element2)
        trues.append([name_true_relation, e1, e2])

    check_JEPD(element1, element2, trues)
    return name_true_relation


def check_JEPD(element1, element2, trues):
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
        exit()


def print_geometries_first_loop(geoms, i, iter, j, k, relation_AB, relation_AC, relation_BC):
    if iter == 1:
        if geoms[i].get_dimension() == 3:
            print("Geometria A: ", geoms[i].convex_polygons)
        else:
            print("Geometria A: ", geoms[i])
        if geoms[j].get_dimension() == 3:
            print("Geometria B: ", geoms[j].convex_polygons)
        else:
            print("Geometria B: ", geoms[j])
        if geoms[k].get_dimension() == 3:
            print("Geometria C: ", geoms[k].convex_polygons)
        else:
            print("Geometria C: ", geoms[k])

        print("Relazione A_B: ", relation_AB)
        print("Relazione B_C: ", relation_BC)
        print("Relazione A_C: ", relation_AC)


def get_convex_polygons_if_convex_polyhedrons(element1, element2):
    if isinstance(element1, ConvexPolyhedron):
        e1 = (element1.convex_polygons)
    else:
        e1 = element1
    if isinstance(element2, ConvexPolyhedron):
        e2 = (element2.convex_polygons)
    else:
        e2 = element2
    return e1, e2


def calculate_matrix_values(geoms, df, file_name):
    iter = 0
    for i in range(len(geoms)):
        for j in range(len(geoms)):
            for k in range(len(geoms)):
                # if i != j and j != k and k != i:
                iter = iter + 1
                relation_AB = get_relations_results(geoms[i], geoms[j])
                relation_BC = get_relations_results(geoms[j], geoms[k])
                relation_AC = get_relations_results(geoms[i], geoms[k])

                print_geometries_first_loop(geoms, i, iter, j, k, relation_AB, relation_AC, relation_BC)

                if df[relation_AB][relation_BC]:
                    if relation_AC not in df[relation_AB][relation_BC]:
                        df[relation_AB][relation_BC] = df[relation_AB][relation_BC] + " " + relation_AC
                else:
                    df[relation_AB][relation_BC] = relation_AC

    df.to_csv('geometry3d/experiments/' + file_name + '.csv', index=True, header=True, sep=' ')

    for rn1 in relation_names:
        for rn2 in relation_names:
            if df[rn1][rn2] is None:
                return [False, df]

    return [True, df]


if __name__ == "__main__":
    matrices = []
    df = init_matrix()
    full_matrix = False
    file_name = input("Nome del file dove salvare la tabella di composizione: ")
    x = -1
    same_matrix = 0
    while same_matrix < convergence_value:
        x += 1
        geoms = init_and_select_geometries()
        full_matrix, matrix = calculate_matrix_values(geoms, df, file_name)
        matrices.append(matrix)
        same = True
        if len(matrices) > 1:
            for i in relation_names:
                for k in relation_names:
                    if not (matrices[x-1] == matrices[x])[i][k]:
                        same_matrix = 0
                        same = False
                        # print("not same matrix")
                        break
            if same:
                same_matrix += 1
                print("same matrix")
            # print(matrices[x-1] == matrices[x])




