from pathlib import Path

print("Welcome to File Organizer Dry Run!")

target_folder = Path(input("Enter a folder path or press Enter for current folder: ").strip() or Path.cwd())
target_folder = target_folder.resolve()

print(f"Scanning: {target_folder}")

for item in target_folder.iterdir():
    if item.is_file():
        extension = item.suffix.lower() or ".no_extension"
        print(f"Would move {item.name} to folder {extension[1:]}")
