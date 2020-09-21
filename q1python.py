#!/usr/bin/env python3


def period_generator(list1, list2):
    class Period:

        def __init__(self, start, end, points):
            self.start = start
            self.end = end
            self.points = points

        def point_count(self):
            return len(self.points)

    periods = []
    for i in range(len(list1) - 1):
        [start, end] = [list1[i], list1[i+1]]
        points = []
        for i in range(start, end):
            amount = list2.count(i)
            points = points + amount * [i]
        periods.append(Period(start, end, points))
    return periods


# if __name__ == "__main__":
#     list1 = [1, 5, 6, 10, 11, 20, 21, 25, 26, 40, 41, 50]
#     list2 = [14, 9, 24, 2, 44, 8, 41, 4, 46, 26,
#              11, 31, 18, 24, 21, 4, 22, 50, 6, 36]
#     periods = period_generator(list1, list2)
#     for p in periods:
#         print(p.start, p.end,
#               p.points, p.point_count())
