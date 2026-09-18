"""Network service tests."""

import unittest

from services.network.health import health_payload, readiness_payload
from services.network.mesh_ping import ping_all, NODES


class TestNetwork(unittest.TestCase):
    def test_health(self):
        h = health_payload()
        self.assertEqual(h["status"], "ok")
        self.assertEqual(h["constants"]["schumann_hz"], 7.83)

    def test_mesh_quorum(self):
        r = ping_all()
        self.assertTrue(r["quorum"])
        self.assertEqual(len(r["nodes"]), len(NODES))

    def test_readiness(self):
        r = readiness_payload(sovereign_ready=True)
        self.assertTrue(r["ready"])


if __name__ == "__main__":
    unittest.main()
