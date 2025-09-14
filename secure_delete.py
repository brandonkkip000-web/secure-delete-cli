import os
import argparse
import secrets

def overwrite_file(filepath, passes=3):
    """Overwrite the file with random data multiple times."""
    if not os.path.isfile(filepath):
        print(f"[!] File not found: {filepath}")
        return False

    size = os.path.getsize(filepath)
    with open(filepath, "ba+") as f:  # Open in binary append mode
        for i in range(passes):
            f.seek(0)
            f.write(secrets.token_bytes(size))
            f.flush()
            os.fsync(f.fileno())
            print(f"[+] Pass {i+1}/{passes} complete")

    return True

def secure_delete(filepath, passes=3):
    if overwrite_file(filepath, passes):
        os.remove(filepath)
        print(f"[✔] Securely deleted: {filepath}")

def main():
    parser = argparse.ArgumentParser(
        description="Securely delete files by overwriting them with random data before removal."
    )
    parser.add_argument("file", help="File to securely delete")
    parser.add_argument("--passes", type=int, default=3, help="Number of overwrite passes (default: 3)")
    args = parser.parse_args()

    secure_delete(args.file, args.passes)

if __name__ == "__main__":
    main()
