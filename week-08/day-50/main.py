from pathlib import Path

base_folder = Path(__file__).parent

required_files = [
    "main.py",
    "README.md",
    "requirements.txt",
    ".gitignore",
    ".env.example",
]

print("Welcome to Clean Project Starter Template!")

for file_name in required_files:
    exists = (base_folder / file_name).exists()
    print(f"{file_name}: {'ready' if exists else 'missing'}")
