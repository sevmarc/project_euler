"""
Three distinct points are plotted at random on a Cartesian plane, for which -1000 ≤ x, y ≤ 1000, such that a triangle is formed.

Consider the following two triangles:

A(-340,495), B(-153,-910), C(835,-947)
X(-175,41), Y(-421,-714), Z(574,-645)

It can be verified that triangle ABC contains the origin, whereas triangle XYZ does not.

Using triangles.txt (right click and 'Save Link/Target As...'), a 27K text file containing the co-ordinates 
of one thousand "random" triangles, find the number of triangles for which the interior contains the origin.

NOTE: The first two examples in the file represent the triangles in the example given above.
"""

from function_collection.main import timer_wrapper
from math import pi, sqrt, acos, degrees

"""

    ^
    |      B              Y
    |     @@@@           @@@
    |    @@@0@@         @@@@@
    |   A@@@@@@@C      X@@@@@@Z
    |____________>

When is (0,0) inside the triangle?
1. Angles:
AOB, BOC, COA angles = 360
XOY, YOZ, ZOX angles < 360

"""

def load_triangles(triangle_file):
    triangles = []
    with open(triangle_file) as tri:
        tris = tri.readlines()
        for t in tris:
            coords = t.split(',')
            triangles.append([[int(coords[0].strip('\n')), int(coords[1].strip('\n'))] ,
                              [int(coords[2].strip('\n')), int(coords[3].strip('\n'))] ,
                              [int(coords[4].strip('\n')), int(coords[5].strip('\n'))]])
    return triangles

def points_dist(point1, point2):
    X1, Y1 = point1
    X2, Y2 = point2
    return sqrt(( X1 - X2 )**2 + (Y1 - Y2)**2)

def angle_by_law_of_cosines(point1, vertex, point2):
    X1, Y1 = point1
    XV, YV = vertex
    X2, Y2 = point2
    return acos(( points_dist(vertex, point1)**2 + 
                  points_dist(vertex, point2)**2 -
                  points_dist(point1, point2)**2 ) / 
                  (2 * points_dist(vertex, point1) * points_dist(vertex, point2)) )


def zero_out_or_in(triangle):
    """ Using law of cosines """
    origo = [0, 0]
    X,Y,Z = triangle
    # XOY, YOZ, ZOX angles
    XOY = angle_by_law_of_cosines(X, origo, Y)
    YOZ = angle_by_law_of_cosines(Y, origo, Z)
    ZOX = angle_by_law_of_cosines(Z, origo, X)
    anglesum_in_rad = (XOY + YOZ + ZOX)
    deg = degrees(anglesum_in_rad)
    return  abs(deg - 360) < 0.00001


def calc102(triangles):
    count = 0
    for t in triangles:
        if zero_out_or_in(t):
            count += 1
    return count

triangle_file = "inputfiles/102_triangles.txt"
triangles = load_triangles(triangle_file)

print(timer_wrapper(calc102, triangles))

"""tests
print(zero_out_or_in(triangles[0]))
print(zero_out_or_in(triangles[1]))
"""