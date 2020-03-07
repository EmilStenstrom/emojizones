# Emojizones
**Emojizones** helps you convert one datetime in one time zone to another, using the emojiis you are used to from your iPhone. Never have time zone conversion been this easy!

## Installation

```bash
pip install emojizones
```

## Example usage

```python
from emojizones import convert
from datetime import datetime

# Here we have a naive datetime without a time zone
from_time = datetime(2020, 3, 7, 0, 0, 0)

# Now we use the emojizones.convert-method
to_time = convert(
    from_time,
    "🗻",  # Mount Fuji, Japan --> Asia/Tokyo
    "🗽"   # Statue of Libery, New York --> America/New_York
)
print(to_time)
# 2020-03-06 10:00:00
```
