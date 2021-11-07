
from shapely.geometry import *
from pygeos import *
from matplotlib import pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from mpl_toolkits.mplot3d.art3d import *
from csv_utilities import *
import global_variables


def get_figure_pints(pol_points):
    x, y, z = [], [], []
    for element in pol_points:
        x.append(element[0])
        y.append(element[1])
        z.append(element[2])
    points = [list(zip(x, y, z))]
    return points


points_strings = read_nodes_file(global_variables.trials_folder, "points")
int_points = get_int_values(points_strings)

for point in int_points:
    point = from_shapely(Point(point))
    print(point)
    fig = plt.figure()
    ax = Axes3D(fig, proj_type='ortho', auto_add_to_figure=False)
    fig.add_axes(ax)
    ax.set_xlim3d(right=2)
    ax.set_ylim3d(ymax=2)
    ax.set_zlim3d(top=2)
    ax.scatter3D(get_x(point), get_y(point), get_z(point))
    plt.show()


linestrings_strings = read_nodes_file(global_variables.trials_folder, "linestrings_3")
int_points = get_int_values(linestrings_strings)

for points_line in int_points:
    line = from_shapely(LineString(points_line))
    print(line)
    vertices = get_figure_pints(points_line)
    print(vertices)
    fig = plt.figure()
    ax = Axes3D(fig, proj_type='ortho', auto_add_to_figure=False)
    fig.add_axes(ax)
    ax.set_xlim3d(right=2)
    ax.set_ylim3d(ymax=2)
    ax.set_zlim3d(top=2)
    ax.add_collection3d(Line3DCollection(vertices))
    plt.show()


linestrings_strings = read_nodes_file(global_variables.trials_folder, "linestrings_5")
int_points = get_int_values(linestrings_strings)

for points_line in int_points:
    line = from_shapely(LineString(points_line))
    print(line)
    vertices = get_figure_pints(points_line)
    print(vertices)
    fig = plt.figure()
    ax = Axes3D(fig, proj_type='ortho', auto_add_to_figure=False)
    fig.add_axes(ax)
    ax.set_xlim3d(right=2)
    ax.set_ylim3d(ymax=2)
    ax.set_zlim3d(top=2)
    ax.add_collection3d(Line3DCollection(vertices))
    plt.show()


polys_strings = read_nodes_file(global_variables.trials_folder, "polygons_3")
int_points = get_int_values(polys_strings)

for points_line in int_points:
    line = from_shapely(Polygon(points_line))
    print(line)
    vertices = get_figure_pints(points_line)
    print(vertices)
    fig = plt.figure()
    ax = Axes3D(fig, proj_type='ortho', auto_add_to_figure=False)
    fig.add_axes(ax)
    ax.set_xlim3d(right=2)
    ax.set_ylim3d(ymax=2)
    ax.set_zlim3d(top=2)
    ax.add_collection3d(Poly3DCollection(vertices))
    plt.show()

polys_strings = read_nodes_file(global_variables.trials_folder, "polygons_4")
int_points = get_int_values(polys_strings)

for points_line in int_points:
    line = from_shapely(Polygon(points_line))
    print(line)
    vertices = get_figure_pints(points_line)
    print(vertices)
    fig = plt.figure()
    ax = Axes3D(fig, proj_type='ortho', auto_add_to_figure=False)
    fig.add_axes(ax)
    ax.set_xlim3d(right=2)
    ax.set_ylim3d(ymax=2)
    ax.set_zlim3d(top=2)
    ax.add_collection3d(Poly3DCollection(vertices))
    plt.show()
    print(is_simple(line))


polys_strings = read_nodes_file(global_variables.trials_folder, "polygons_5")
int_points = get_int_values(polys_strings)

for points_line in int_points:
    line = from_shapely(Polygon(points_line))
    print(line)
    vertices = get_figure_pints(points_line)
    print(vertices)
    fig = plt.figure()
    ax = Axes3D(fig, proj_type='ortho', auto_add_to_figure=False)
    fig.add_axes(ax)
    ax.set_xlim3d(right=2)
    ax.set_ylim3d(ymax=2)
    ax.set_zlim3d(top=2)
    ax.add_collection3d(Poly3DCollection(vertices))
    plt.show()
    print(is_simple(line))

