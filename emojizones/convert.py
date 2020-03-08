from emojizones.lookup import EMOJI_TO_TIMEZONE
from datetime import datetime, timedelta
import pytz
import grapheme

DATETIME_FORMAT = "%Y-%m-%d %H:%M:%S"

OPERATORS = {
    "✖": "*",
    "➕": "+",
    "➖": "-",
    "➗": "/",
    "*": "*",
    "+": "+",
    "-": "-",
    "/": "/",
}
NUMBERS = {
    "0️⃣": "0",
    "1️⃣": "1",
    "2️⃣": "2",
    "3️⃣": "3",
    "4️⃣": "4",
    "5️⃣": "5",
    "6️⃣": "6",
    "7️⃣": "7",
    "8️⃣": "8",
    "9️⃣": "9",
    "🔟": "10",
}

class EmojiZoneException(Exception):
    pass

def convert(from_dt, from_emoji, to_emoji, as_string=False):
    if not from_dt:
        raise EmojiZoneException("Received empty value instad of a datetime")

    if isinstance(from_dt, str):
        try:
            from_dt = datetime.strptime(from_dt, DATETIME_FORMAT)
        except ValueError:
            raise EmojiZoneException(f"Supplied string is not a valid datetime in the '{DATETIME_FORMAT}' format")

    from_timezone = pytz.timezone(emoji_lookup(from_emoji, from_dt=from_dt))
    to_timezone = pytz.timezone(emoji_lookup(to_emoji, from_dt=from_dt))

    from_dt = from_timezone.localize(from_dt.replace(tzinfo=None))
    to_dt = from_dt.astimezone(to_timezone)

    if as_string:
        return to_dt.strftime(DATETIME_FORMAT)

    return to_dt

def possible_timezones(tz_offset):
    # convert the float hours offset to a timedelta
    offset_days, offset_seconds = 0, int(tz_offset * 3600)
    if offset_seconds < 0:
        offset_days = -1
        offset_seconds += 24 * 3600
    desired_delta = timedelta(offset_days, offset_seconds)

    # Loop through the timezones and find any with matching offsets
    null_delta = timedelta(0, 0)
    results = []
    for tz_name in pytz.common_timezones:
        tz = pytz.timezone(tz_name)
        non_dst_offset = getattr(tz, '_transition_info', [[null_delta]])[-1]
        if desired_delta == non_dst_offset[0]:
            results.append(tz_name)

    return results

def emoji_lookup(emoji_string, from_dt=None):
    if from_dt and isinstance(from_dt, str):
        try:
            from_dt = datetime.strptime(from_dt, DATETIME_FORMAT)
        except ValueError:
            raise EmojiZoneException(f"Supplied string is not a valid datetime in the '{DATETIME_FORMAT}' format")

    emoji_list = list(grapheme.graphemes(emoji_string))

    if len(emoji_list) == 0:
        raise EmojiZoneException(f"Need at least one emoji to convert")

    emoji_expression = []
    for emoji in emoji_list:
        if emoji in EMOJI_TO_TIMEZONE:
            emoji_expression.append(EMOJI_TO_TIMEZONE[emoji])
        elif emoji in NUMBERS:
            emoji_expression.append(NUMBERS[emoji])
        elif emoji in OPERATORS:
            emoji_expression.append(OPERATORS[emoji])
        else:
            raise EmojiZoneException(f"Did not find timezone for {emoji}, consider adding it in a PR!")

    initial_timezone = emoji_expression[0]
    if len(emoji_expression) == 1:
        return initial_timezone

    if emoji_expression[0] not in pytz.common_timezones:
        raise EmojiZoneException(f"The first emoji must be a valid timezone, {emoji_expression[0]} is not")

    for i, element in enumerate(emoji_expression[1:]):
        if element in pytz.common_timezones:
            raise EmojiZoneException(f"Only the first emoji can be a valid timezone, {emoji_list[i + 1]} is not")

    if from_dt is None:
        raise EmojiZoneException(f"Emoji aritmetics requires from_dt from where to do lookups")

    expression = []
    for element in emoji_expression:
        if element in pytz.common_timezones:
            utc_offset = pytz.timezone(element).utcoffset(from_dt.replace(tzinfo=None))
            hours = utc_offset.total_seconds() / (60 * 60)
            expression.append(str(hours))
        else:
            expression.append(element)

    try:
        evaluated_offset = eval("".join(expression), {}, {})
    except Exception:
        raise EmojiZoneException(f"Failed to parse emoji expression '{''.join(expression)}'")

    matching_timezones = possible_timezones(evaluated_offset)

    prefix = initial_timezone[:initial_timezone.index("/")]
    for timezone in matching_timezones:
        if timezone.startswith(prefix):
            return timezone

    return matching_timezones[0]
