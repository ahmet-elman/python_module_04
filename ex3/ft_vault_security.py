#!/usr/bin/env python3

def secure_archive(
        file_name: str,
        action: str = "read",
        content: str = "") -> tuple[bool, str]:

    try:
        if not action.strip():
            action = "read"
        action = action.strip()
        if action == "read" or action == "r":
            with open(file_name, "r") as file:
                return True, file.read()
        elif action == "write" or action == "w":
            with open(file_name, "w") as file:
                file.write(content)
                return True, "Content successfully written to file"
        else:
            return False, f"Unknown action: {action}"

    except Exception as e:
        return False, str(e)


if __name__ == "__main__":
    print("=== Cyber Archives Security ===")
    print()
    print("Using 'secure_archive' to read from a nonexistent file:")
    print(secure_archive("/not/existing/file", "read"))
    print()
    print("Using 'secure_archive' to read from an inaccessible file:")
    print(secure_archive("text.txt", "read"))
    print()
    print("Using 'secure_archive' to read from a regular file:")
    print(secure_archive("file", "read"))
    print()
    print("Using 'secure_archive' to write previous content to a new file:")
    result = secure_archive(
            "file",
            "write",
            "[FRAGMENT 001] Digital preservation protocols established 2087 \n"
            "[FRAGMENT 002] Knowledge must survive the entropy wars \n"
            "[FRAGMENT 003] Every byte saved is a victory against oblivion\n")
    print(result)
