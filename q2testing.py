import unittest
from q1python import period_generator

# CRITERIA:
# All periods and data points must be whole numbers
# There can only ever be a maximum of 10 periods
# Each point represents one second - a period may be no longer than 10 seconds
# Each period must contain between one and 10 data points
# Points must be stored in time order, with the earliest listed first

list1 = [1, 5, 6, 10, 11, 20, 21, 25, 26, 40, 41, 50]

list2 = [14, 9, 24, 2, 44, 8, 41, 4, 46, 26,
         11, 31, 18, 24, 21, 4, 22, 50, 6, 36]


class TestPeriodGenerator(unittest.TestCase):

    # the result of this test depends solely on the values of list1 and list2
    def test_all_periods_and_data_points_whole_numbers(self):
        periods = period_generator(list1, list2)

        # all periods integers
        self.assertTrue(all(isinstance(period.start, int) and isinstance(
            period.end, int) for period in periods))

        # all points integers
        self.assertTrue(all(all(isinstance(point, int)
                                for point in period.points) for period in periods))

    # similarly, the result of this test depends solely on the amount of values in list1
    def test_max_of_ten_periods(self):
        periods = period_generator(list1, list2)

        self.assertTrue(len(periods) <= 10)

    # similarly, the result of this test depends solely on the values of list1
    def test_period_no_longer_than_ten_secs(self):
        periods = period_generator(list1, list2)

        for period in periods:
            print((period.end - period.start))

        self.assertTrue(all((period.end - period.start) <=
                            10 for period in periods))

    def test_each_period_contains_between_one_and_ten_data_points(self):
        periods = period_generator(list1, list2)

        self.assertTrue(all(1 <= len(period.points)
                            <= 10 for period in periods))

    def test_points_ordered_by_ascending(self):
        periods = period_generator(list1, list2)

        def list_is_ascending(list):
            output = True
            for i in range(len(list) - 1):
                if list[i+1] < list[i]:
                    output = False
            return output

        self.assertTrue(all(list_is_ascending(period.points)
                            for period in periods))

# the program will NOT pass with the data set provided, due to the 3rd criteria (that a period can be no longer than 10 seconds),
# as the penultimate period has a gap of 14 seconds (between 26 and 40)
