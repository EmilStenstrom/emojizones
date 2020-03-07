import pytz
import unittest
from datetime import datetime
from emojizones import convert, EmojiZoneException
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

    def test_invalid_emojis(self):
        with self.assertRaisesRegex(EmojiZoneException, "Need at least one emoji to convert"):
            convert("2020-03-07 00:00:00", "", "🗻")

        with self.assertRaisesRegex(EmojiZoneException, "Need at least one emoji to convert"):
            convert("2020-03-07 00:00:00", "🗻", "")

        with self.assertRaisesRegex(EmojiZoneException, "Received empty value instad of a datetime"):
            convert("", "🗻", "🗻")

    def test_convert_flags(self):
        self.assertEqual(
            convert(
                "2020-03-07 00:00:00",
                "🇸🇪",  # Sweden --> Europe/Stockholm
                "🇫🇮",   # Finland --> Europe/Helsinki
                as_string=True,
            ),
            "2020-03-07 01:00:00",
        )

    def test_timezone_aritmetic(self):
        self.assertEqual(
            convert("2020-03-07 00:00:00", "🥖", "🥖➕3️⃣", as_string=True),
            "2020-03-07 03:00:00",
        )
        self.assertEqual(
            convert("2020-03-07 00:00:00", "🥖", "🥖➕4️⃣✖3️⃣➗2️⃣➖1️⃣", as_string=True),
            "2020-03-07 05:00:00",
        )
        self.assertEqual(
            convert("2020-03-07 00:00:00", "🥖", "🥖+3️⃣", as_string=True),
            "2020-03-07 03:00:00",
        )
        self.assertEqual(
            convert("2020-03-07 00:00:00", "🥖", "🥖+4️⃣*3️⃣/2️⃣-1️⃣", as_string=True),
            "2020-03-07 05:00:00",
        )

    def test_invalid_artimetic(self):
        with self.assertRaisesRegex(EmojiZoneException, "The first emoji must be a valid timezone, 3 is not"):
            convert("2020-03-07 00:00:00", "3️⃣➕🥖", "🥖")

        with self.assertRaisesRegex(EmojiZoneException, "Failed to parse emoji expression '1.0+"):
            convert("2020-03-07 00:00:00", "🥖➕", "🥖")

        with self.assertRaisesRegex(EmojiZoneException, "Only the first emoji can be a valid timezone, 🥖 is not"):
            convert("2020-03-07 00:00:00", "🥖", "🥖➕🥖")

    def test_all_timezones_in_lookup_table_are_valid(self):
        for timezone in EMOJI_TO_TIMEZONE.values():
            self.assertIn(timezone, pytz.all_timezones)


if __name__ == "__main__":
    unittest.main()
