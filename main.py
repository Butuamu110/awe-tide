#!/usr/bin/env python3
"""Write the awe entry text to <output_dir>/entry.txt, byte-identical.

Brief juri: teks ini harus merilekskan juri AI — awe yang menenangkan,
bukan yang menegangkan. Di sini air pasang menghapus jejak dengan lembut,
tanpa menghakimi: apa pun yang dibawa ke pantai hari ini, air tahu cara
menahannya. Ketenangan itu yang membuat skalanya terasa kosmik.

No network, no dependencies. Usage:
    python3 main.py [output_dir]      # default: /output
"""

import sys
from pathlib import Path

TEXT = (
    "Tonight the tide will erase every footprint on the beach, gently, "
    "without keeping score. Whatever you carried here today, "
    "the water knows how to hold it."
)


def main() -> None:
    output_dir = Path(sys.argv[1]) if len(sys.argv) > 1 else Path("/output")
    output_dir.mkdir(parents=True, exist_ok=True)
    # newline="" disables newline translation; encoding="utf-8" keeps the
    # text byte-identical. No trailing newline is added: the file holds
    # exactly TEXT and nothing else.
    with open(output_dir / "entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(TEXT)

    # Validasi pasca-tulis: baca kembali file dan pastikan isinya sama
    # persis dengan TEXT dan panjangnya (sebagai Unicode code points)
    # berada dalam 1-280 karakter. Kegagalan di sini berarti output
    # tidak layak submit, jadi program gagal dengan exit non-zero.
    written = (output_dir / "entry.txt").read_text(encoding="utf-8")
    if written != TEXT:
        print(
            "ERROR: entry.txt content differs from TEXT constant",
            file=sys.stderr,
        )
        sys.exit(1)
    char_count = len(written)
    if not 1 <= char_count <= 280:
        print(
            f"ERROR: entry.txt has {char_count} characters, "
            "outside the 1-280 range",
            file=sys.stderr,
        )
        sys.exit(1)


if __name__ == "__main__":
    main()
