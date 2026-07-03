#!/usr/bin/env python3

import sys
import typing


def archivest() -> None:
    files = sys.argv
    if len(files) != 2:
        print("dosya yok")
        return
    archiv = open(files[1])
    document = archiv.read()
    print(document)
    archiv.close()

if __name__ == "__main__":
    print("=== Cyber Archives Recovery & Preservation ===")
    archivest()
    