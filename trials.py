"""
    Creazione poligoni: Point, LineString, Polygon
"""

from shapely.geometry import *
from pygeos import *
from matplotlib import pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from mpl_toolkits.mplot3d.art3d import *


def get_figure_pints(pol_points):
    x, y, z = [], [], []
    for element in pol_points:
        x.append(element[0])
        y.append(element[1])
        z.append(element[2])
    points = [list(zip(x, y, z))]
    return points


points = [1, 0, 1]
point = from_shapely(Point(points))
print(point)
fig = plt.figure()
ax = Axes3D(fig, proj_type='ortho', auto_add_to_figure=False)
fig.add_axes(ax)
ax.scatter3D(get_x(point), get_y(point), get_z(point))
plt.show()

points_line = [(0, 0, 0), (1, 0, 1), (0, 1, 1)]
line = from_shapely(LineString(points_line))
print(line)
vertices = get_figure_pints(points_line)
print(vertices)

fig = plt.figure()
ax = Axes3D(fig, proj_type='ortho', auto_add_to_figure=False)
fig.add_axes(ax)
# ax.set_xlim3d(right=2)
# ax.set_ylim3d(ymax=2)
# ax.set_zlim3d(top=2)
ax.add_collection3d(Line3DCollection(vertices))


# print("intersects:", intersection(line, point))
# print("intersect:", intersects(line, point))

print("cross:", crosses(line, point))
print("contains:", contains(line, point))
print("disjoint:", disjoint(line, point))
print("overlaps:", overlaps(line, point))
print("touches:", touches(line, point))
print("within: ", within(line, point))
print("equal: ", equals(line, point))


points_line = [(0, 0, 0), (1, 0, 1), (0, 1, 1)]
poly = from_shapely(Polygon(points_line))
print(line)
vertices = get_figure_pints(points_line)
print(vertices)

fig = plt.figure()
ax = Axes3D(fig, proj_type='ortho', auto_add_to_figure=False)
fig.add_axes(ax)
# ax.set_xlim3d(right=2)
# ax.set_ylim3d(ymax=2)
# ax.set_zlim3d(top=2)
ax.add_collection3d(Poly3DCollection(vertices))

print("crosses:", crosses(line, poly))
print("contains:", contains(line, poly))
print("disjoint:", disjoint(line, poly))
print("overlaps:", overlaps(line, poly))
print("touches:", touches(line, poly))
print("within: ", within(line, poly))
print("equals: ", equals(line, poly))


plt.show()
