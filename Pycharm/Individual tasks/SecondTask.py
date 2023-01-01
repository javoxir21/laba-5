#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import math

print("Введите координаты точки и радиус круга")
x = float(input("x = "))
y = float(input("y = "))
r = float(input("R = "))

r_xy = math.sqrt(x ** 2 + y ** 2)

if r_xy <= r:
    print("Точка принадлежит кругу")
else:
    print("Точка не принадлежит кругу")
    