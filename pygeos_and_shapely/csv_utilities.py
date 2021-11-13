"""
    Funzioni utili per tener traccia dei dataset generati
    e per poter rendere gli esperimenti riproducibili, mantenendone memoria
    in definiti files .csv, i cui nomi sono specificati all'interno del file
    global_variables.py
"""
import csv


def write_nodes_to_file(folder, nodes, file_name):
    with open(folder + '/' + file_name, mode='w') as nodes_file:
        if "three" in file_name or "3" in file_name:
            fieldnames = ['nodo_1', 'nodo_2', 'nodo_3']
        elif "four" in file_name or "4" in file_name:
            fieldnames = ['nodo_1', 'nodo_2', 'nodo_3', 'nodo_4']
        elif "five" in file_name or "5" in file_name:
            fieldnames = ['nodo_1', 'nodo_2', 'nodo_3', 'nodo_4', 'nodo_5']
        elif "points" in file_name:
            fieldnames = ['punto']

        writer = csv.DictWriter(nodes_file, fieldnames=fieldnames)
        writer.writeheader()
        lines = 0
        for node in nodes:
            if "three" in file_name or "3" in file_name:
                writer.writerow(
                    {'nodo_1': node[0], 'nodo_2': node[1], 'nodo_3': node[2]})
            elif "four" in file_name or "4" in file_name:
                writer.writerow(
                    {'nodo_1': node[0], 'nodo_2': node[1], 'nodo_3': node[2], 'nodo_4': node[3]})
            elif "five" in file_name or "5" in file_name:
                writer.writerow(
                    {'nodo_1': node[0], 'nodo_2': node[1], 'nodo_3': node[2], 'nodo_4': node[3], 'nodo_5': node[4]})
            elif "points" in file_name:
                writer.writerow({'punto': node})
            lines = lines + 1
        # print("Scritte su file", lines, "righe\n")


def read_nodes_file(folder, filename):
    nodes_1 = []
    nodes_2 = []
    nodes_3 = []
    nodes_4 = []
    nodes_5 = []
    with open(folder + '/' + filename, mode='r') as nodes_file:
        reader = csv.DictReader(nodes_file)
        for row in reader:
            if "points" not in filename:
                nodes_1.append(row["nodo_1"])
                nodes_2.append(row["nodo_2"])
                nodes_3.append(row["nodo_3"])
                if "four" in filename or "4" in filename:
                    nodes_4.append(row["nodo_4"])
                if "five" in filename or "5" in filename:
                    nodes_4.append(row["nodo_4"])
                    nodes_5.append(row["nodo_5"])
            else:
                nodes_1.append((row["punto"]))
    return [nodes_1, nodes_2, nodes_3, nodes_4, nodes_5]


def get_int_values(arr):
    nodes_1 = arr[0]
    nodes_2 = arr[1]
    nodes_3 = arr[2]
    nodes_4 = arr[3]
    nodes_5 = arr[4]
    nodes = []
    chars_1 = []
    chars_2 = []
    chars_3 = []
    chars_4 = []
    chars_5 = []
    for i in range(len(nodes_1)):
        for char in range(len(nodes_1[i])):
            if nodes_1[i][char] != " " and nodes_1[i][char] != "," and nodes_1[i][char] != "[" and nodes_1[i][char] != "]":

                chars_1.append(int(nodes_1[i][char]))
                if nodes_2:
                    chars_2.append(int(nodes_2[i][char]))
                if nodes_3:
                    chars_3.append(int(nodes_3[i][char]))
                if nodes_4:
                    chars_4.append(int(nodes_4[i][char]))
                if nodes_5:
                    chars_5.append(int(nodes_5[i][char]))
                if len(chars_1) == 3:
                    if nodes_5:
                        nodes.append([chars_1, chars_2, chars_3, chars_4, chars_5])
                    elif nodes_4:
                        nodes.append([chars_1, chars_2, chars_3, chars_4])
                    elif nodes_3:
                        nodes.append([chars_1, chars_2, chars_3])
                    elif nodes_2:
                        nodes.append([chars_1, chars_2])
                    else:
                        nodes.append(chars_1)
                    chars_1 = []
                    chars_2 = []
                    chars_3 = []
                    chars_4 = []
                    chars_5 = []
    return nodes


def get_int_values_points(arr):
    nodes_1 = arr[0]
    nodes_2 = arr[1]
    nodes_3 = arr[2]
    nodes_4 = arr[3]
    nodes_5 = arr[4]
    nodes = []
    chars_1 = []
    chars_2 = []
    chars_3 = []
    chars_4 = []
    chars_5 = []
    for i in range(len(nodes_1)):
        for char in range(len(nodes_1[i])):
            if nodes_1[i][char] != " " and nodes_1[i][char] != "," and nodes_1[i][char] != "[" and nodes_1[i][
                char] != "]":
                chars_1.append(int(nodes_1[i][char]))
                chars_2.append(int(nodes_2[i][char]))
                chars_3.append(int(nodes_3[i][char]))
                if nodes_4:
                    chars_4.append(int(nodes_4[i][char]))
                if nodes_5:
                    chars_5.append(int(nodes_5[i][char]))
                if len(chars_1) == 3:
                    nodes.append([chars_1, chars_2, chars_3])
                    chars_1 = []
                    chars_2 = []
                    chars_3 = []
                    chars_4 = []
                    chars_5 = []
    return nodes