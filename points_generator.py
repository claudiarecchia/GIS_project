from csv_utilities import write_nodes_to_file, read_nodes_file, get_int_values


def generate_points(plot_dimension, folder, filename):
    points = []
    for i in range(0, plot_dimension+1):
        for j in range(0, plot_dimension+1):
            for k in range(0, plot_dimension+1):
                points.append([i, j, k])
    write_nodes_to_file(folder, points, filename)
    return points


def get_points(folder, filename):
    arr = read_nodes_file(folder, filename)
    points = get_int_values(arr)
    return points