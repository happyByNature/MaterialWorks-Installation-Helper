import sys
import os
import shutil
import zipfile
from datetime import datetime

# Version
v = "0.3.0"

# --- Header ---
print(f"\n*** MaterialWorks Installation Helper, Version: {v} ***")
print(f"Date/Time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")

if len(sys.argv) < 2:
    print("Error: No source folder provided.")
    print("Usage: python mwInstallationHelper.py <source_dir>")
    sys.exit(1)

source_dir = os.path.abspath(sys.argv[1])
print(f"Source folder: {source_dir}\n")

# --- Validate source folder ---
if not os.path.isdir(source_dir):
    print(f"Error: Source folder '{source_dir}' does not exist.")
    sys.exit(1)

# --- Validate zip files exist ---
zip_files = [f for f in os.listdir(source_dir) if f.lower().endswith(".zip")]
if not zip_files:
    print(f"Error: No zip files found in '{source_dir}'.")
    sys.exit(1)

# --- Create target folder ---
parent_dir = os.path.dirname(source_dir)
source_name = os.path.basename(source_dir)
target_dir = os.path.join(parent_dir, f"{source_name}_Ready")

if os.path.isdir(target_dir):
    print(f"Target folder already exists. Clearing: {target_dir}")
    for item in os.listdir(target_dir):
        item_path = os.path.join(target_dir, item)
        if os.path.isfile(item_path) or os.path.islink(item_path):
            os.remove(item_path)
        elif os.path.isdir(item_path):
            shutil.rmtree(item_path)
else:
    os.makedirs(target_dir)
    print(f"Created target folder: {target_dir}")

# --- Create subfolders ---
mats_1k_dir = os.path.join(target_dir, "BB Mats 1K")
mats_4k_dir = os.path.join(target_dir, "BB Mats 4K")
edgewear_dir = os.path.join(target_dir, "Edgewear")
os.makedirs(mats_1k_dir, exist_ok=True)
os.makedirs(mats_4k_dir, exist_ok=True)
os.makedirs(edgewear_dir, exist_ok=True)

# --- Extract BB_Mats_1K.zip ---
zip_1k = os.path.join(source_dir, "BB_Mats_1K.zip")
if os.path.isfile(zip_1k):
    print(f"Extracting BB_Mats_1K.zip -> BB Mats 1K/")
    with zipfile.ZipFile(zip_1k, "r") as z:
        z.extractall(mats_1k_dir)
else:
    print("Warning: BB_Mats_1K.zip not found, skipping.")

# --- Extract BB_Mats_4K*.zip files ---
zip_4k_files = sorted(f for f in zip_files if f.startswith("BB_Mats_4k"))
if zip_4k_files:
    for fname in zip_4k_files:
        print(f"Extracting {fname} -> BB Mats 4K/")
        with zipfile.ZipFile(os.path.join(source_dir, fname), "r") as z:
            z.extractall(mats_4k_dir)
else:
    print("Warning: No BB_Mats_4K*.zip files found, skipping.")

# --- Extract Edgewear zip files ---
edgewear_prefixes = ("Dents", "Dust", "Edgewear_and_Particles", "Rust", "Scratches", "Smudge_and_Stains")
edgewear_files = sorted(f for f in zip_files if any(f.startswith(p) for p in edgewear_prefixes))
if edgewear_files:
    for fname in edgewear_files:
        print(f"Extracting {fname} -> Edgewear/")
        with zipfile.ZipFile(os.path.join(source_dir, fname), "r") as z:
            z.extractall(edgewear_dir)
else:
    print("Warning: No Edgewear zip files found, skipping.")

print("\nDone!")
