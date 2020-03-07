# Stupidzones
**Stupidzones** helps you convert one datetime in one time zone to another, using the emojiis you are used to from your iPhone. Never have time zone conversion been this easy!

## Installation

```bash
pip install stupidzones
```

## Example usage

```python
>>> from stupidzones import convert
>>> from datetime import datetime
>>>
>>> convert(datetime(2020, 3, 7, 0, 0, 0), "🗾", "🗻")
"2020-03-07 13:14:15"

```
