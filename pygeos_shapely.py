from pygeos import *
from matplotlib import pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
import shapely.wkt
from shapely.geometry import Polygon


def new_figure(text):
    global fig, ax
    fig = plt.figure()
    fig.suptitle(text, fontsize=16)
    ax = Axes3D(fig, proj_type='ortho', auto_add_to_figure=False)
    fig.add_axes(ax)


def get_figure_pints(pol_points):
    x, y, z = [], [], []
    for element in pol_points:
        x.append(element[0])
        y.append(element[1])
        z.append(element[2])
    points = [list(zip(x, y, z))]
    return points


trials = [[
    [(0, 0, 0), (1, 0, 0), (1, 1, 0.5), (0, 1, 1)],
    [(1, 0, 1), (1, 1, 0), (0, 1, 1)]
    ]
    # [
    #     [(0, 0, 0), (1, 0, 1), (0, 1, 1)],
    #     [(1, 0, 1), (1, 1, 0), (0.6, 1, 0.6)]
    # ],
    # [
    #     [(0, 0, 0), (1, 0, 1), (0, 1, 1)],
    #     [(1, 0.2, 1), (1, 1, 0), (0.6, 1, 0.6)]
    # ]
]


for trial in trials:
    pol_1 = trial[0]
    pol_2 = trial[1]

    pol_points = pol_1
    pol = from_shapely(Polygon(pol_points))
    print("POLIGONO 1:", pol)
    print("DIMENSIONE COORDINATE:", get_coordinate_dimension(pol))
    print("AREA:", area(pol))

    new_figure("Poligono 1")
    vertices = get_figure_pints(pol_points)
    ax.add_collection3d(Poly3DCollection(vertices, facecolors="green"))
    plt.show()

    pol_2_points = pol_2
    pol_2 = from_shapely(Polygon(pol_2_points))
    print("POLIGONO 2:", pol_2)
    print("DIMENSIONE COORDINATE:", get_coordinate_dimension(pol_2))
    print("AREA:", area(pol_2))

    new_figure("Poligono 2")
    vertices = get_figure_pints(pol_2_points)
    ax.add_collection3d(Poly3DCollection(vertices, facecolors="blue"))
    plt.show()

    print("intersects:", intersection(pol, pol_2))
    print("touches:", touches(pol, pol_2))
    print("overlaps:", overlaps(pol, pol_2))
    print("contains:", contains(pol, pol_2))

    inter = intersection(pol, pol_2)
    print("AREA:", area(inter))
    P = shapely.wkt.loads(to_wkt(inter))
    # print(P.geometryType())
    coords = []
    if P.is_empty:
        print("L'intersezione è vuota. Il poligono dato dall'intersezione è vuoto.")

    elif P.geometryType() == "Point":
        for element in P.coords:
            coords.append(element)

        new_figure("Intersezione")
        ax.set_xlim3d(right=1)
        ax.set_ylim3d(ymax=1)
        ax.set_zlim3d(top=1)
        ax.scatter3D(coords[0][0], coords[0][1], coords[0][2], edgecolor="red")
        plt.show()
    else:
        for element in P.exterior.coords:
            coords.append(element)

        new_figure("Intersezione")
        if P.geometryType() != "Point":
            vertices = get_figure_pints(coords)
            ax.add_collection3d(Poly3DCollection(vertices, facecolors="red"))
        else:
            ax.set_xlim3d(right=1)
            ax.set_ylim3d(ymax=1)
            ax.set_zlim3d(top=1)
            ax.scatter3D(coords[0][0], coords[0][1], coords[0][2], edgecolor="red")
        plt.show()
    print("\n")
