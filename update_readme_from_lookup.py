import re
import textwrap
from collections import defaultdict

EMOJI_LINE = re.compile(r'"([^"]+)": +"([^"]+)", +# (.+)', flags=re.UNICODE)
HEADING_LINE = re.compile(r'([A-Z_]+)\s+=\s+{', flags=re.UNICODE)

def main():
    blocks = defaultdict(list)
    current_heading = ""
    with open("emojizones/lookup.py", "r") as f:
        for line in f.readlines():
            line = line.strip()
            if not EMOJI_LINE.match(line):
                if HEADING_LINE.match(line):
                    varible = HEADING_LINE.match(line).group(1)
                    current_heading = varible.replace("_", " ").title()

                continue

            emoji, timezone, comment = EMOJI_LINE.match(line).groups()

            blocks[current_heading].append(
                f"| {emoji} | {timezone} | {comment} |"
            )

    TABLE_HEADING = textwrap.dedent("""
        | Emoji | Timezone | Comment |
        |---|---|---|
    """)
    TABLE = "\n".join(
        "### " + heading + "\n" + TABLE_HEADING + "\n".join(lines) + "\n"
        for heading, lines in blocks.items()
    )

    old_readme = []
    found_heading = False
    with open("README.md", "r") as f:
        for line in f.readlines():
            line = line.rstrip()

            old_readme.append(line)
            if line == "## Supported emojis":
                old_readme.append("\n")
                found_heading = True
                break

    if not found_heading:
        print("Did not find '## Supported emojis' heading, aborting...")
        return

    with open("README.md", "w") as f:
        f.write("\n".join(old_readme) + TABLE + "\n")


if __name__ == '__main__':
    main()
