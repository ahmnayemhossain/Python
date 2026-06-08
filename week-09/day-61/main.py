from pathlib import Path
import shutil

print("Welcome to File Download Organizer!")

target_folder = Path(input("Enter download folder path or press Enter for current folder: ").strip() or Path.cwd())
target_folder = target_folder.resolve()

print(f"Scanning: {target_folder}")

for file_path in target_folder.iterdir():
    if file_path.is_file():
        extension_name = file_path.suffix.lower().lstrip(".") or "no_extension"
        destination_folder = target_folder / extension_name
        destination_folder.mkdir(exist_ok=True)
        destination_path = destination_folder / file_path.name
        if destination_path.exists():
            print(f"Skipped {file_path.name} because target already exists.")
        else:
            shutil.move(str(file_path), str(destination_path))
            print(f"Moved {file_path.name} to {destination_folder.name}/")
