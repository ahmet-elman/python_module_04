#!/usr/bin/env python3

import sys
import typing


def ft_data_archivist() -> None:
    archive = sys.argv
    if len(archive) != 2:
        print(f"Usage: {archive[0]} <file>")
        return
    file: typing.IO[str] | None = None
    try:
        print("=== Cyber Archives Recovery ===")
        print(f"Accessing file '{archive[1]}'\n")
        file_line: str = archive[1]
        file = open(file_line, 'r')
        content: str = file.read()
        print("---\n")
        print(content)
        print("\n---")
    except Exception as e:
        print(f"Error opening file '{file_line}':", e)
    finally:
        if file is not None:
            file.close()
            print(f"File '{file_line}' closed.")


if __name__ == "__main__":
    ft_data_archivist()
