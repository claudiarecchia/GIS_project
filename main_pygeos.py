
import numpy
from pygeos import *
from matplotlib import pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from mpl_toolkits.mplot3d.art3d import Poly3DCollection

# point_1 = Geometry("POINT (5.2 52.1 6.1)")
# print(point_1)
# print(get_coordinate_dimension(point_1))
#
# # prova visualizzazione
# fig = plt.figure()
# ax = Axes3D(fig, proj_type='ortho', auto_add_to_figure=False)
# fig.add_axes(ax)
# ax.scatter3D(get_x(point_1), get_y(point_1), get_z(point_1))
# plt.show()
#
# point_2 = Geometry("POINT (6.2 50.1 6.1)")
# print(point_2)
# print(get_coordinate_dimension(point_2))
#
# print(intersection(point_1, point_2))  # non c'è intersezione
#
# point_3 = Geometry("POINT (6.2 50.1 6.1)")
# print(point_3)
# print(get_coordinate_dimension(point_3))
#
# print(intersection(point_3, point_2))  # OK -- l'intersezione è il punto stesso
#
# ###############################################################
#
# # POLIGONI
# polygon_1 = box(0, 0, 1, 1)
# print(polygon_1)
# # print(get_x(polygon_1))
# print(get_coordinate_dimension(polygon_1))

# pol_2 = Geometry("POLYGON((0 0 0, 0 10 1, 10 10 1, 10 0 1, 1 1 1, 0 0 0))")
# pol_2 = Geometry("POLYGON((0 0 0, 1 0 1, 1 1 0, 0 1 1))")
# print(pol_2)
# print(get_coordinate_dimension(pol_2))
# # print(get_x(pol_2))
# print(area(pol_2))

# x = [0,1,1,0]
# y = [0,0,1,1]
# z = [0,1,0,1]

# pol_3 = Geometry("POLYGON((0 0 0, 0 2 0, 2 2 0, 2 0 0, 0 0 2, 0 2 2, 2 2 2, 2 0 2, 0 0 0))")
# pol_3 = Geometry("POLYGON((0 0 0, 2 0 0, 2 2 0, 0 2 0, 0 0 0, 0 0 2, 2 0 2, 2 2 2, 0 2 2, 0 0 2, 0 0 0))")
# print(pol_3)
# print(get_coordinate_dimension(pol_3))
# # print(get_x(pol_2))
# print(area(pol_3))
#
# print("intersects:", intersection(pol_2, pol_3))
# print("touches:", touches(pol_2, pol_3))
# print("overlaps:", overlaps(pol_2, pol_3))
# print("overlaps:", overlaps(pol_3, pol_2))


from shapely.geometry import Polygon
pol_points = [(0, 0, 0), (0, 1, 0), (1, 1, 0), (1, 0, 0), (0, 0, 1)]  # , (0, 0, 1), (0, 1, 1), (1, 1, 1), (1, 0, 1)
# pyramid = [(0, 0, 0),  (1, 1, 0), (0, 1, 0),(1, 0, 0), (0.5, 0.5, 1)]
# pol_points = [(1, 0, 1), (1, 1, 0), (0, 1, 1)]
pol = from_shapely(Polygon(pol_points))
# pol = from_shapely(Polygon())
print(pol)
print(get_coordinate_dimension(pol))
print(area(pol))
#
fig = plt.figure()
ax = Axes3D(fig, proj_type='ortho', auto_add_to_figure=False)
fig.add_axes(ax)

x_g_triangle, y_g_triangle, z_g_triangle = [], [], []
for element in pol_points:
    x_g_triangle.append(element[0])
    y_g_triangle.append(element[1])
    z_g_triangle.append(element[2])
verts_2 = [list(zip(x_g_triangle, y_g_triangle, z_g_triangle))]
ax.add_collection3d(Poly3DCollection(verts_2, facecolors="green"))
plt.show()

#
# pol_2_points = [(1, 0, 1), (1, 1, 0), (0, 1, 1)]
# pol_2 = from_shapely(Polygon(pol_points))
# # pol = from_shapely(Polygon())
# print(pol_2)
# print(get_coordinate_dimension(pol_2))
# print(area(pol_2))
# #
# fig = plt.figure()
# ax = Axes3D(fig, proj_type='ortho', auto_add_to_figure=False)
# fig.add_axes(ax)
#
# x_g_triangle, y_g_triangle, z_g_triangle = [], [], []
# for element in pol_2_points:
#     x_g_triangle.append(element[0])
#     y_g_triangle.append(element[1])
#     z_g_triangle.append(element[2])
# verts_2 = [list(zip(x_g_triangle, y_g_triangle, z_g_triangle))]
# ax.add_collection3d(Poly3DCollection(verts_2, facecolors="blue"))
# plt.show()
#
# print("intersects:", intersection(pol_2, pol))
# print("intersects:", intersection(pol, pol_2))
# print("touches:", touches(pol_2, pol))
# print("overlaps:", overlaps(pol_2, pol))
# print("overlaps:", overlaps(pol, pol_2))
#
# inter = intersection(pol_2, pol)
#
# print("point:", get_point(inter, 0))
#
# # fig = plt.figure()
# # ax = Axes3D(fig, proj_type='ortho', auto_add_to_figure=False)
# # fig.add_axes(ax)
# #
# # x_g_triangle, y_g_triangle, z_g_triangle = [], [], []
# # for element in inter:
# #     x_g_triangle.append(element[0])
# #     y_g_triangle.append(element[1])
# #     z_g_triangle.append(element[2])
# # verts_2 = [list(zip(x_g_triangle, y_g_triangle, z_g_triangle))]
# # ax.add_collection3d(Poly3DCollection(verts_2, facecolors="red"))
# # plt.show()
#
#
# pol_3 = Geometry("POLYGON ((1 0 1, 1 1 0, 0 1 1, 1 0 1))")
# print(pol_3)
# print(get_coordinate_dimension(pol_3))
# print(area(pol_3))
#
# # shapely_1 = to_wkt(Geometry(("POLYGON ((1 0 1, 1 1 0, 0 1 1, 1 0 1))")))
# # print("to WKT:", shapely_1)
#
# import shapely.wkt
# # P = shapely.wkt.loads("POLYGON ((1 0 1, 1 1 0, 0 1 1, 1 0 1))")
# P = shapely.wkt.loads(to_wkt(inter))
# print(P)
# print(P.geometryType())
# coords = []
# for element in P.exterior.coords:
#     coords.append(element)
#
# fig = plt.figure()
# ax = Axes3D(fig, proj_type='ortho', auto_add_to_figure=False)
# fig.add_axes(ax)
# x_g_triangle, y_g_triangle, z_g_triangle = [], [], []
# for element in coords:
#     x_g_triangle.append(element[0])
#     y_g_triangle.append(element[1])
#     z_g_triangle.append(element[2])
# verts_2 = [list(zip(x_g_triangle, y_g_triangle, z_g_triangle))]
# ax.add_collection3d(Poly3DCollection(verts_2, facecolors="red"))
# plt.show()
#
# pol_4 = Geometry("POLYGON ((0.4 0.2 1, 1 1 0, 0 1 1, 0.4 0.2 1))")
# print(pol_4)
# print(get_coordinate_dimension(pol_4))
# print(area(pol_4))
# #
# print("intersects:", intersection(pol_4, pol_3))
# print("touches:", touches(pol_4, pol_3))
# print("overlaps:", overlaps(pol_4, pol_3))
