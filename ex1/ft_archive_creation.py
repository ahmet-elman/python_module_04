#!/usr/bin/env python3

import sys


def ft_data_archivist() -> None:
    archive = sys.argv
    if len(archive) != 2:
        print("Usage: ft_ancient_text.py <file>")
        return
    file = None
    try:
        print("=== Cyber Archives Recovery ===")
        print(f"Accessing file '{archive[1]}'\n")
        file_line: str = archive[1]
        file = open(file_line, 'r')
        content = file.read()
        print("---\n")
        print(content, end="")
        print("\n---")
    except FileNotFoundError as e:
        print(f"Error opening file '{archive[1]}':", e)
    except PermissionError as e:
        print(f"Error opening file '{archive[1]}':", e)
    except Exception as e:
        print(f"An unexpected error occurred with '{archive[1]}':", e)
    finally:
        if file is not None:
            file.close()
            print(f"File '{archive[1]}' closed.")
    print()
    try:
        print("Transform data")
        
    except Exception as e:
        print(e)

    


if __name__ == "__main__":
    ft_data_archivist()
