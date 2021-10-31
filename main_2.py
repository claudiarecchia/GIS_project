from matplotlib import pyplot as plt
from shapely.geometry import Polygon, LineString
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
from mpl_toolkits.mplot3d import Axes3D

red_triangle = Polygon([(0, 0), (1, 1), (1, 0)])
poly_area = red_triangle.area
print("Area triangolo rosso:", poly_area)
# per la visualizzazione grafica
x, y = red_triangle.exterior.xy

pol2 = [(0, 0), (0, 2), (2, 2), (2, 0), (0, 0)]
yellow_rectangle = Polygon(pol2)
w, z = yellow_rectangle.exterior.xy

green_triangle = Polygon([(2, 0), (1, 1), (1.25, 1.25)])

m, n = green_triangle.exterior.xy
plt.plot(w, z, c="black")
plt.fill(w, z, c="yellow")
plt.plot(x, y, c="black")
plt.fill(x, y, c="red")
plt.plot(m, n, c="black")
plt.fill(m, n, c="green")

print("red_triangle TOUCHES yellow_rectangle: ", red_triangle.touches(yellow_rectangle))
print("red_triangle TOUCHES yellow_triangle: ", red_triangle.touches(green_triangle))
print("red_triangle INTERSECTION yellow_rectangle: ", red_triangle.intersection(yellow_rectangle))

plt.show()
# # costruzione poligono
# green_triangle_2 = Polygon([(2, 0, 0), (1, 1, 0), (1.25, 1.25, 1)])
# fig2 = plt.figure()
# ax2 = fig2.add_subplot(111, projection='3d')
# ax2.add_collection3d(green_triangle_2)
# plt.show()

fig = plt.figure()
ax = Axes3D(fig, proj_type='ortho', auto_add_to_figure=False)
fig.add_axes(ax)
# x = [0, 1, 1, 0]
# y = [0, 0, 1, 1]
# z = [0, 1, 0, 1]

b_triangle = [[0.4, 0.4, 0.0], [1.0, 1.0, 0.0], [0.25, 0.25, 1.0]]
x_b_triangle, y_b_triangle, z_b_triangle = [], [], []
for element in b_triangle:
    x_b_triangle.append(element[0])
    y_b_triangle.append(element[1])
    z_b_triangle.append(element[2])

verts_1 = [list(zip(x_b_triangle, y_b_triangle, z_b_triangle))]
ax.add_collection3d(Poly3DCollection(verts_1))

g_triangle = [[0.1, 0.1, 0.0], [0.4, 0.4, 0.0], [0.2, 0.2, 1.0]]
x_g_triangle, y_g_triangle, z_g_triangle = [], [], []
for element in g_triangle:
    x_g_triangle.append(element[0])
    y_g_triangle.append(element[1])
    z_g_triangle.append(element[2])
verts_2 = [list(zip(x_g_triangle, y_g_triangle, z_g_triangle))]
ax.add_collection3d(Poly3DCollection(verts_2, facecolors="green"))
plt.show()


################################################
fig = plt.figure()
ax = Axes3D(fig, proj_type='ortho', auto_add_to_figure=False)
fig.add_axes(ax)
# prototype_polygon = [(0, 0, 0), (1, 0, 0), (1, 1, 0), (0, 1, 0), (0, 1, 1), (0, 0, 1), (1, 1, 1)]
# # , (0, 0, 1), (1, 0, 1), (1, 1, 1), (0, 1, 1)
# x_cube, y_cube, z_cube = [], [], []
# for element in prototype_polygon:
#     x_cube.append(element[0])
#     y_cube.append(element[1])
#     z_cube.append(element[2])
x = [0,1,1,0]
y = [0,0,1,1]
z = [0,1,0,1]
verts_1 = [list(zip(x, y, z))]
ax.add_collection3d(Poly3DCollection(verts_1))

x = [0.4, 1, 1, 0]
y = [0.2, 0, 1, 1]
z = [0, 1, 0, 1]
verts_1 = [list(zip(x, y, z))]
ax.add_collection3d(Poly3DCollection(verts_1, facecolors="green"))
plt.show()
# it can be used to change the axes view
ax.view_init(100, 0)
plt.show()
################################################
# import numpy as np
#
# # Create axis
# axes = [5, 5, 5]
#
# # Create Data
# data = np.ones(axes, dtype=np.bool)
# print(data)

# Polygons
# green = Polygon(g_triangle)
# blue = Polygon(b_triangle)
# green.buffer(0)
# blue.buffer(0)
# print("green_triangle TOUCHES blue_triangle: ", green.touches(blue))
# print("green_triangle INTERSECTION blue_triangle: ", blue.intersection(green))


# fig_2 = plt.figure()
# ax_2 = Axes3D(fig_2, proj_type='persp', auto_add_to_figure=False)
# fig_2.add_axes(ax_2)
# g_triangle = [(0.0, 0.0, 0.0), (1.0, 1.0, 0.0), (0.2, 0.2, 1.0)]
# x_g_triangle, y_g_triangle, z_g_triangle = [], [], []
# for element in g_triangle:
#     x_g_triangle.append(element[0])
#     y_g_triangle.append(element[1])
#     z_g_triangle.append(element[2])
# verts_2 = [list(zip(x_g_triangle, y_g_triangle, z_g_triangle))]
# ax_2.add_collection3d(Poly3DCollection(verts_2, facecolors="green"))

