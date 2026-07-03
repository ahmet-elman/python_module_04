#!/usr/bin/env python3

import sys


def ft_data_archivist() -> None:
    archive = sys.argv
    if len(archive) != 2:
        print("Usage: ft_ancient_text.py <file>")
        return

    try:
        print("=== Cyber Archives Recovery ===")
        print(f"Accessing file '{archive[1]}'\n")
        file_line: str = archive[1]
        file = open(file_line, 'r')
        content = file.read()
        print(content)
    except FileNotFoundError as e:
        print(f"Error opening file '{archive[1]}':", e)
    except PermissionError as e:
        print(f"Error opening file '{archive[1]}':", e)
    else:
        print("\n---")
        file.close()
        print(f"File '{archive[1]}' closed.")


if __name__ == "__main__":
    ft_data_archivist()