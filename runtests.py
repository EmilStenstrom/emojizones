import pytz
import unittest
from emojizones import convert
from emojizones.lookup import EMOJI_TO_TIMEZONE

class ConvertTest(unittest.TestCase):

    def test_convert_basic(self):
        self.assertEqual(
            convert("2020-03-07 00:00:00", "🗻", "🗽", as_string=True),
            "2020-03-06 10:00:00",
        )

    def test_valid_timezones(self):
        for timezone in EMOJI_TO_TIMEZONE.values():
            self.assertIn(timezone, pytz.all_timezones)


if __name__ == "__main__":
    unittest.main()
