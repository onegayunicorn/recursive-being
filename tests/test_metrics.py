"""Schumann + SO(5) metric tests."""

import unittest

from src.metrics.schumann import SchumannMetrics, SCHUMANN_MODES
from src.metrics.so5 import SO5Algebra, dim_so_n, is_skew


class TestSchumann(unittest.TestCase):
    def test_fundamental(self):
        m = SchumannMetrics()
        self.assertAlmostEqual(m.f1, 7.83, places=2)
        modes = m.modes()
        self.assertIn("fundamental", modes)
        self.assertGreater(modes["h5"], modes["h2"])

    def test_oscillator_bounds(self):
        m = SchumannMetrics()
        v = m.oscillator(0.0)
        self.assertTrue(0.9 <= v <= 1.1)


class TestSO5(unittest.TestCase):
    def test_dimension(self):
        self.assertEqual(dim_so_n(5), 10)
        alg = SO5Algebra()
        self.assertEqual(len(alg.basis), 10)
        self.assertTrue(alg.verify_basis()["all_skew"])

    def test_generators_skew(self):
        alg = SO5Algebra()
        for G in alg.basis:
            self.assertTrue(is_skew(G))


if __name__ == "__main__":
    unittest.main()
