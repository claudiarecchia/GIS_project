from csv_utilities import *


def generate_points(plot_dimension):
    points = []
    for i in range(0, plot_dimension+1):
        for j in range(0, plot_dimension+1):
            for k in range(0, plot_dimension+1):
                points.append([i, j, k])
    write_nodes_to_file("points", points, "points")
    return points


# if __name__ == "__main__":
#     # generate_points(2)
#     arr = read_nodes_file("points", "points")
#     print(arr)
#
#     nodes = get_int_values(arr)
#     for el in nodes:
#         print(el)
