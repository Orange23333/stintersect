# -*- coding: UTF-8 -*-

import cv2
import numpy
import os
# import sympy
# import pvtrack vtk boost.geogmetry open3d opengl
from shapely.geometry import Polygon


def get_fitting_curve(origin_polygon: Polygon, threshold=10, denominator=10, max_iou=1, min_iou=0.8):
    """

    refs:
        * python-OpenCV-多边形拟合: https://blog.csdn.net/weixin_52182640/article/details/116198310 。
        * https://docs.opencv.org/4.5.5/d3/dc0/group__imgproc__shape.html#ga0012a5fdaea70b8a9970165d98722b4c 。
        * https://shapely.readthedocs.io/en/latest/manual.html?highlight=Polygon#polygons 。

    :param origin_polygon: 原始的多边形曲线。
    :param threshold:
    :param denominator:
    :param max_iou:
    :param min_iou:
    :return:
    """

    temp = list(origin_polygon.boundary.coords)
    print(temp[0].__class__)
    temparr=array[len(temp)][2]
    foreach
        heRE

    origin_curve = numpy.ndarray(temp)
    print(origin_curve)

    if len(origin_curve) <= threshold:
        return Polygon(origin_curve)  # Clone.

    # epsilon = len(origin_curve) / denominator
    epsilon = cv2.arcLength(origin_curve, True)/denominator
    iou = 0

    fitting_curve = cv2.approxPolyDP(origin_curve, epsilon, True)
    # 因为fitting
    print(origin_curve.area)
    print(fitting_curve.area)
    return 0

    iou = origin_curve.area / fitting_curve.area

    while iou > max_iou:
        epsilon += 1
    while iou < min_iou:
        epsilion -= 1


def get_iou(poly1: Polygon, poly2: Polygon):
    """
    获取两个多边形的交并比。

    refs:
        * python——计算两个多边形的IOU: https://blog.csdn.net/qq_40081208/article/details/105309319 。
        * 一种实用性较强的求IOU的算法（任意多边形之间的IOU）: https://sky-x.blog.csdn.net/article/details/122159051 。
        * ! 计算多边形之间的IOU， polygon iou: https://blog.csdn.net/heroacool/article/details/112668056 。

    :param poly1: 多边形1.
    :param poly2: 多边形2.
    :return: 多边形1和多边形2的交并比。
    """

    intersection_area = poly1.intersection(poly2).area
    union_area = poly1.union(poly2).area
    return intersection_area / union_area
