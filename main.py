"""Write the entry image for make.fun's news-image-20261124 bounty.

Copies the image this repository holds (news.png) to entry.png in the
output directory. Deterministic: the same input bytes always produce the
same output bytes. Standard library only; no network.

Outside the grader's container, MAKEFUN_OUTPUT_DIR stands in for /output:
    mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
"""

import os
import shutil

HERE = os.path.dirname(os.path.abspath(__file__))
SOURCE = os.path.join(HERE, "news.png")
OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
DESTINATION = os.path.join(OUTPUT_DIR, "entry.png")
PNG_SIGNATURE = b"\x89PNG\r\n\x1a\n"
MAX_BYTES = 1048576


def main():
    with open(SOURCE, "rb") as f:
        data = f.read()
    if not data.startswith(PNG_SIGNATURE):
        raise ValueError("news.png is not a PNG image")
    if len(data) > MAX_BYTES:
        raise ValueError("news.png is over the 1 MiB limit")
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    with open(DESTINATION, "wb") as f:
        f.write(data)
    print("wrote %s (%d bytes)" % (DESTINATION, len(data)))


if __name__ == "__main__":
    main()
