import pytz
import unittest
from datetime import datetime
from emojizones import convert
from emojizones.lookup import EMOJI_TO_TIMEZONE

class ConvertTest(unittest.TestCase):

    def test_convert_datetime(self):
        self.assertEqual(
            convert(datetime(2020, 3, 7, 0, 0, 0), "🗻", "🗽"),
            pytz.timezone('America/New_York').localize(datetime(2020, 3, 6, 10, 0, 0)),
        )
        self.assertEqual(
            convert(datetime(2020, 3, 7, 0, 0), "🗻", "🗽", as_string=True),
            "2020-03-06 10:00:00",
        )

    def test_convert_string(self):
        self.assertEqual(
            convert("2020-03-07 00:00:00", "🗻", "🗽"),
            pytz.timezone('America/New_York').localize(datetime(2020, 3, 6, 10, 0, 0)),
        )
        self.assertEqual(
            convert("2020-03-07 00:00:00", "🗻", "🗽", as_string=True),
            "2020-03-06 10:00:00",
        )

    def test_valid_timezones(self):
        for timezone in EMOJI_TO_TIMEZONE.values():
            self.assertIn(timezone, pytz.all_timezones)


if __name__ == "__main__":
    unittest.main()
