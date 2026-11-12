"""Platform-safety tests for the optional Attention Guardian."""

import unittest

import guardian


class GuardianPlatformTests(unittest.TestCase):
    def test_non_windows_monitor_is_disabled_without_user32(self):
        original = guardian.user32
        try:
            guardian.user32 = None
            self.assertEqual(guardian.get_active_window_title(), "")
            self.assertIsNone(guardian.start_attention_guardian({}, lambda _: None))
        finally:
            guardian.user32 = original


if __name__ == "__main__":
    unittest.main()
