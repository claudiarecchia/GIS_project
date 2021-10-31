"""
    Generatore di poligoni in 3D
    Triangoli, quadrati, pentagoni
    Tre punti sono sempre coplanari
    Per quadrati e pentagoni si utilizzerà una funzione capace di
    comprendere se 4 punti appartengono allo stesso piano
    https://www.geeksforgeeks.org/program-to-check-whether-4-points-in-a-3-d-plane-are-coplanar/
"""
from csv_utilities import *
from linestring_generator import *


def are_coplanar(vertices):
    x1 = vertices[0][0]
    y1 = vertices[0][1]
    z1 = vertices[0][2]

    x2 = vertices[1][0]
    y2 = vertices[1][1]
    z2 = vertices[1][2]

    x3 = vertices[2][0]
    y3 = vertices[2][1]
    z3 = vertices[2][2]

    x = vertices[3][0]
    y = vertices[3][1]
    z = vertices[3][2]

    a1 = x2 - x1
    b1 = y2 - y1
    c1 = z2 - z1
    a2 = x3 - x1
    b2 = y3 - y1
    c2 = z3 - z1
    a = b1 * c2 - b2 * c1
    b = a2 * c1 - a1 * c2
    c = a1 * b2 - b1 * a2
    d = (- a * x1 - b * y1 - c * z1)

    # equation of plane is: a*x + b*y + c*z = 0 #
    # checking if the 4th point satisfies
    # the above equation
    if (a * x + b * y + c * z + d == 0):
        # print("Coplanar")
        coplanar = True
    else:
        # print("Not Coplanar")
        coplanar = False
    return coplanar


# polygon = [[0, 0, 0], [1, 0, 1], [1, 1, 0], [0, 1, 1]]  # aereo
# polygon_2 = [[0, 0, 0], [1, 0, 0], [1, 1, 0], [0, 1, 0]]
# equation_plane(polygon_2)

lines = generate_linestring_dim_4()
print(lines[0])

squares = []

for line in lines:
    if are_coplanar(line):
        squares.append(line)

print(len(squares))

#############################################





#############################################

# lines_2 = generate_linestring_dim_5()
# pentagons = []
#
# for line in lines_2:
#     line = line.pop(0)  # elimino primo elemento
#     line_2 = line.pop()  # elimino ultimo elemento
#     print(line)
#     print(line_2)
#     if are_coplanar(line) and are_coplanar(line_2):
#         pentagons.append(line)
#
# print(len(pentagons))
