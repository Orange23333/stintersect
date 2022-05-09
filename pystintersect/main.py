# -*- coding: UTF-8 -*-

# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

from shapely.geometry import Polygon
from shapely.geometry import LineString

from fitting import get_fitting_curve

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

    pl1 = Polygon([[2, 2], [3, 4], [5, 6], [0, 0]])
    print(len(list(pl1.boundary.coords)))
    get_fitting_curve(pl1, 0, 4, 1, 0.5)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
