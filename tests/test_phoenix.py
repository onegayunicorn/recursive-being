"""Phoenix Seed unit tests."""

import unittest

from src.phoenix.seed import PhoenixSeed, COHERENCE_TARGET, FOLD_ENTRY_HASH


class TestPhoenixSeed(unittest.TestCase):
    def test_fold_hash_stable(self):
        a = PhoenixSeed()
        b = PhoenixSeed()
        self.assertEqual(a.genesis_hash, b.genesis_hash)
        self.assertEqual(a.genesis_hash, FOLD_ENTRY_HASH)

    def test_self_heal_restores(self):
        seed = PhoenixSeed()
        seed.perturb(0.5)
        self.assertLess(seed.coherence, COHERENCE_TARGET)
        ok, msg = seed.self_heal()
        self.assertTrue(ok)
        self.assertGreaterEqual(seed.coherence, COHERENCE_TARGET)
        self.assertEqual(seed.phase, "BLOOM")
        self.assertEqual(seed.cycle_count, 1)

    def test_stable_no_rebirth(self):
        seed = PhoenixSeed()
        ok, msg = seed.self_heal()
        self.assertTrue(ok)
        self.assertIn("Stable", msg)
        self.assertEqual(seed.cycle_count, 0)


if __name__ == "__main__":
    unittest.main()
