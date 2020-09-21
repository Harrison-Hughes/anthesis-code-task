import unittest
import period_generator as period_generator

# All periods and data points must be whole numbers
# There can only ever be a maximum of 10 periods
# Each point represents one second - a period may be no longer than 10 seconds
# Each period must contain between one and 10 data points
# Points must be stored in time order, with the earliest listed first

list1 = [1, 5, 6, 10, 11, 20, 21, 25, 26, 40, 41, 50]

list2 = [14, 9, 24, 2, 44, 8, 41, 4, 46, 26,
         11, 31, 18, 24, 21, 4, 22, 50, 6, 36]


class PeriodGenerator(unittest.TestCase):

    # the result of this test depends solely on the values of list1 and list2
    def all_periods_and_data_points_whole_numbers(self):
        periods = period_generator(list1, list2)

        # all periods integers
        self.assertTrue(all(isinstance(num, int) for num in list1)

        # all points integers
        self.assertTrue(all(isinstance(period.start, int) and isinstance(period.end, int) for period in periods)

    # similarly, the result of this test depends solely on the amount of values in list1
    def max_of_ten_periods(self):
        self.assertTrue

    def period_no_longer_than_ten_secs(self):

    def each_period_contains_between_one_and_ten_data_points(self):

    def points_ordered_by_ascending(self):
