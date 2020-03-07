from emojizones.lookup import EMOJI_TO_TIMEZONE
from datetime import datetime
import pytz
import random

DATETIME_FORMAT = "%Y-%m-%d %H:%M:%S"

def convert(from_dt, from_emoji, to_emoji, as_string=False):
    if isinstance(from_dt, str):
        from_dt = datetime.strptime(from_dt, DATETIME_FORMAT)

    from_timezone = pytz.timezone(emoji_lookup(from_emoji))
    to_timezone = pytz.timezone(emoji_lookup(to_emoji))

    from_dt = from_timezone.localize(from_dt)
    to_dt = from_dt.astimezone(to_timezone)

    if as_string:
        return to_dt.strftime(DATETIME_FORMAT)

    return to_dt

def emoji_lookup(emoji):
    if emoji not in EMOJI_TO_TIMEZONE:
        emoji = random.choice(list(EMOJI_TO_TIMEZONE.keys()))

    return EMOJI_TO_TIMEZONE[emoji]
