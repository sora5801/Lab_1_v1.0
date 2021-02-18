from collections import namedtuple
from collections import defaultdict
import re

class Temperature:
    def __init__(self, median, upper, lower):
        self.Temperature = namedtuple('Temperature',
                                        [ 'median', 'upper', 'lower'])
        self.T = self.Temperature(median,upper,lower)

    def __str__(self):
        return "Temperature(median='{}', upper='{:.3f}', lower='{}')".format(
            self.T.median,
            self.T.upper, self.T.lower)

    def __repr__(self):
        return "Temperature(median='{}', upper='{:.3f}', lower='{}')".format(
            self.T.median,
            self.T.upper, self.T.lower)

    def __eq__(self,other):
        self.T = other

    def __iter__(self):
        return self