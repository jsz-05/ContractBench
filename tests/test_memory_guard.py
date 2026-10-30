import sys
from pathlib import Path
import unittest
from unittest.mock import patch

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
from run_local import ensure_memory


class MemoryGuardTests(unittest.TestCase):
    def test_yellow_pressure_is_allowed(self):
        with patch("run_local.memory", return_value={"normal": False, "pressure_level": 2, "free_percent": 30}):
            self.assertEqual(ensure_memory()["pressure_level"], 2)

    def test_critical_pressure_stops(self):
        with patch("run_local.memory", return_value={"normal": False, "pressure_level": 4, "free_percent": 30}):
            with self.assertRaises(RuntimeError):
                ensure_memory()

    def test_dangerously_low_headroom_stops(self):
        with patch("run_local.memory", return_value={"normal": True, "pressure_level": 1, "free_percent": 5}):
            with self.assertRaises(RuntimeError):
                ensure_memory()
