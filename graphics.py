import random
from typing import List
from shapely.geometry import Point

import matplotlib.pyplot as plt

COLORS = ['red', 'green', 'blue']


def _draw_3D_points(ax: plt.figure, points_to_draw: List[Point], color='black'):
    if len(points_to_draw) == 0:
        return None

    xdata = [pt.x for pt in points_to_draw] + [points_to_draw[0].x]
    ydata = [pt.y for pt in points_to_draw] + [points_to_draw[0].y]
    zdata = [pt.z for pt in points_to_draw] + [points_to_draw[0].z]
    ax.plot3D(xdata, ydata, zdata, c=color, linestyle='', marker='x')


def draw_3D_points_list(three_D_points_list: List[List[Point]]):
    fig = plt.figure()
    ax = plt.axes(projection='3d')

    for i, a_list_of_points in enumerate(three_D_points_list):
        _draw_3D_points(ax, a_list_of_points, color=COLORS[i % len(COLORS)])

    plt.show()
