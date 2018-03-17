"""Unit tests for the LinearRegression class."""

import itertools
import unittest

import numpy as np

from mltools.glm import LinearModel


class TestLinearModel(unittest.TestCase):
    def test_easy_1d(self):
        """Numbers from http://onlinestatbook.com/2/regression/intro.html"""
        x = [1, 2, 3, 4, 5]
        y = [1, 2, 1.3, 3.75, 2.25]
        model = LinearModel()
        model.fit(x, y)
        intercept, slope = model.coef
        self.assertAlmostEqual(intercept, 0.785)
        self.assertAlmostEqual(slope, 0.425)

    def test_easy_2d(self):
        """Adapted from Exercises 3a, #3 in
            George A. F. Seber and Alan J. Lee. Linear Regression Analysis,
            Second Edition. Wiley Series in Probability and Statistics.
            Wiley-Interscience, Hoboken, NJ, 2003, pp. xvi+557.
            DOI: https://doi.org/10.1002/9780471722199
        """
        x = [[1, 0], [2, -1], [1, 2]]
        ys = np.linspace(-5, 5, num=10)
        for y1, y2, y3 in itertools.product(ys, ys, ys):
            y = [y1, y2, y3]
            model = LinearModel(fit_intercept=False)
            model.fit(x, y)
            theta, phi = model.coef
            self.assertAlmostEqual(theta, (y1 + 2 * y2 + y3) / 6)
            self.assertAlmostEqual(phi, (2 * y3 - y2) / 5)


if __name__ == "__main__":
    unittest.main()