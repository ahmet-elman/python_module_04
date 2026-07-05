#!/usr/bin/env python3

import sys
import typing


def ft_data_archivist() -> None:
    archive = sys.argv
    if len(archive) != 2:
        print(f"Usage: {archive[0]} <file>")
        return
    file: typing.IO[str] | None = None
    error_status: int = 0
    try:
        print("=== Cyber Archives Recovery & Preservation ===")
        print(f"Accessing file '{archive[1]}'\n")
        file_line: str = archive[1]
        file = open(file_line, 'r')
        content: str = file.read()
        print("---\n")
        print(content)
        print("\n---")

    except Exception as e:
        sys.stderr.write(f"[STDERR] Error opening file '{file_line}': {e} \n")
        error_status = 1

    finally:
        if file is not None:
            file.close()
            print(f"File '{file_line}' closed.")

    if error_status == 1:
        return
    print()
    new_file: typing.IO[str] | None = None
    file_name: str = ""
    try:
        print("Transform data")
        print("---\n")
        new_lines: list[str] = [ln + '#' for ln in content.splitlines()]
        print(*new_lines, sep="\n")
        print("\n---")
        print("Enter new file name (or empty):", end=" ")
        sys.stdout.flush()
        file_name = sys.stdin.readline().strip()
        if not file_name.strip():
            print("Not saving data.")
            return
        else:
            print(f"Saving data to '{file_name}'")
        new_file = open(file_name, "w")
        for line in new_lines:
            new_file.write(line + "\n")
        print(f"Data saved in file '{file_name}'.")
    except Exception as e:
        sys.stderr.write(f"[STDERR] Error opening file '{file_name}': {e} \n")
        print("Data not saved.")
    except BaseException:
        return

    finally:
        if new_file is not None:
            new_file.close()


if __name__ == "__main__":
    ft_data_archivist()
