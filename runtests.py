import unittest
from datetime import datetime

import pytz

from emojizones import EmojiZoneException, convert, emoji_lookup
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

    def test_aware_datetime(self):
        from_time = pytz.UTC.localize(datetime(2020, 3, 7, 0, 0, 0))
        self.assertEqual(
            convert(from_time, "🗻", "🗽"),
            pytz.timezone('America/New_York').localize(datetime(2020, 3, 6, 10, 0, 0)),
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

    def test_invalid_string_input(self):
        with self.assertRaisesRegex(
            EmojiZoneException,
            "Supplied string is not a valid datetime in the '%Y-%m-%d %H:%M:%S' format"
        ):
            convert("2020/01/01 00:00:00", "🗻", "🗻")

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
            convert("2020-03-07 00:00:00", "🥖", "🥖➖3️⃣", as_string=True),
            "2020-03-06 21:00:00",
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
        self.assertEqual(
            convert("2020-03-07 00:00:00", "🥖", "🥖+🔟🔟-1️⃣0️⃣1️⃣0️⃣+🔟", as_string=True),
            "2020-03-07 10:00:00",
        )
        self.assertEqual(
            convert("2020-03-07 00:00:00", "🥖", "🥖➕🥖", as_string=True),
            "2020-03-07 01:00:00",
        )

    def test_invalid_artimetic(self):
        with self.assertRaisesRegex(EmojiZoneException, "The first emoji must be a valid timezone, 3 is not"):
            convert("2020-03-07 00:00:00", "3️⃣➕🥖", "🥖")

        with self.assertRaisesRegex(EmojiZoneException, "Failed to parse emoji expression '1.0+"):
            convert("2020-03-07 00:00:00", "🥖➕", "🥖")

    def test_direct_emoji_lookup(self):
        self.assertEqual(
            emoji_lookup("🥖"),
            "Europe/Paris"
        )
        self.assertEqual(
            emoji_lookup("🥖➕2️⃣", from_dt="2020-03-07 00:00:00"),
            "Europe/Istanbul"
        )

        from_time = datetime(2000, 1, 1, 0, 0)
        timezone = emoji_lookup("👨‍🎤➕4️⃣✖3️⃣-👨‍🎤", from_time)
        difference = pytz.timezone(timezone).utcoffset(from_time.replace(tzinfo=None))
        hours = difference.total_seconds() / (60 * 60)
        self.assertEqual(hours, 12.0)

    def test_invalid_emoji_lookup(self):
        with self.assertRaisesRegex(EmojiZoneException, "Did not find timezone for 🛑, consider adding it in a PR!"):
            emoji_lookup("🛑")

        with self.assertRaisesRegex(EmojiZoneException, "Emoji aritmetics requires from_dt from where to do lookups"):
            emoji_lookup("🥖➕2️⃣")

        with self.assertRaisesRegex(
            EmojiZoneException,
            "Supplied string is not a valid datetime in the '%Y-%m-%d %H:%M:%S' format"
        ):
            emoji_lookup("🗻", from_dt="2020/01/01 00:00:00")

    def test_all_timezones_in_lookup_table_are_valid(self):
        for timezone in EMOJI_TO_TIMEZONE.values():
            self.assertIn(timezone, pytz.common_timezones)


if __name__ == "__main__":
    unittest.main()
