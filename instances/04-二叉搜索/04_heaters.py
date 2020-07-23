# -*- coding: utf-8 -*-
"""
@Author         :  LEITENG
@Version        :  
------------------------------------
@File           :  04——heaters.py
@Description    :  
@CreateTime     :  2020/7/19 23:13
------------------------------------
@ModifyTime     :  
"""
from bisect import bisect


def find_radius(houses: list, heaters: list):
    heaters.sort()
    redius = 0
    for house in houses:
        heater_idx = bisect(heaters, house)
        left = heaters[heater_idx - 1] if heater_idx - 1 >= 0 else float('-inf')
        right = heaters[heater_idx] if heater_idx < len(heaters) else float('inf')
        redius = max(redius, min(house - left, right - house))
    return redius


def main():
    houses = [1, 2, 3, 4]
    heaters = [1, 4]
    print(find_radius(houses, heaters))

    houses = [1, 12, 23, 34]
    heaters = [12, 24]
    print(find_radius(houses, heaters))


if __name__ == '__main__':
    main()