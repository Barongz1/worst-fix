"""Worst Fix Ever: Funniest Commit Message — entry for make.fun.

Writes one line to /output/entry.txt. The line is one commit message for a bug fix that made everything worse, at most 100 characters.
"""
import os

LINE = "fix: replaced the bug with a bigger bug that has its own bug tracker"

def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE + "\n")

if __name__ == "__main__":
    main()
