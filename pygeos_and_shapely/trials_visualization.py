"""
    Visualizzazione grafica degli elementi Point, LineString, Polygon
    identificati come campioni (trials)
"""

from shapely.geometry import *
from pygeos import *
from matplotlib import pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from mpl_toolkits.mplot3d.art3d import *
from pygeos_and_shapely.csv_utilities import *
from pygeos_and_shapely import global_variables

linestrings = [global_variables.lin_3, global_variables.lin_4, global_variables.lin_5]
polygons = [global_variables.pol_3, global_variables.pol_4, global_variables.pol_5]


def get_figure_points(pol_points):
    x, y, z = [], [], []
    for element in pol_points:
        x.append(element[0])
        y.append(element[1])
        z.append(element[2])
    points = [list(zip(x, y, z))]
    return points


def set_axes():
    fig = plt.figure()
    ax = Axes3D(fig, proj_type='ortho', auto_add_to_figure=False)
    fig.add_axes(ax)
    ax.set_xlim3d(right=2)
    ax.set_ylim3d(ymax=2)
    ax.set_zlim3d(top=2)
    return ax, fig


def plot_point(point):
    point = from_shapely(Point(point))
    print(point)
    ax, fig = set_axes()
    fig.suptitle(point, fontsize=10)
    ax.scatter3D(get_x(point), get_y(point), get_z(point))
    plt.show()


def plot_linestring(points_line):
    line = from_shapely(LineString(points_line))
    print(line)
    vertices = get_figure_points(points_line)
    ax, fig = set_axes()
    fig.suptitle(line, fontsize=10)
    ax.add_collection3d(Line3DCollection(vertices))
    plt.show()


def plot_polygon(points_line):
    line = from_shapely(Polygon(points_line))
    print(line)
    vertices = get_figure_points(points_line)
    ax, fig = set_axes()
    fig.suptitle(line, fontsize=10)
    ax.add_collection3d(Poly3DCollection(vertices))
    plt.show()


points_strings = read_nodes_file(global_variables.trials_folder, global_variables.points_file)
int_points = get_int_values(points_strings)
for point in int_points:
    plot_point(point)


for lin in linestrings:
    linestrings_strings = read_nodes_file(global_variables.trials_folder, lin)
    int_points = get_int_values(linestrings_strings)
    for points_line in int_points:

        plot_linestring(points_line)

for pol in polygons:
    polys_strings = read_nodes_file(global_variables.trials_folder, pol)
    int_points = get_int_values(polys_strings)
    for points_line in int_points:
        print(points_line)
        plot_polygon(points_line)


