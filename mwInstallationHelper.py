import sys
import os
import shutil
import zipfile
import time
from datetime import datetime

# Version
v = "0.5.0"

# --- Header ---
start_time = time.time()
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
hdri_dir = os.path.join(target_dir, "HDRi")
os.makedirs(mats_1k_dir, exist_ok=True)
os.makedirs(mats_4k_dir, exist_ok=True)
os.makedirs(edgewear_dir, exist_ok=True)
os.makedirs(hdri_dir, exist_ok=True)

def extract_zips(files, dest, label):
    if not files:
        print(f"Warning: No {label} zip files found, skipping.")
        return
    t = time.time()
    for fname in sorted(files):
        print(f"Extracting {fname} -> {label}/")
        with zipfile.ZipFile(os.path.join(source_dir, fname), "r") as z:
            z.extractall(dest)
    print(f"  [{label} done in {time.time() - t:.1f}s]")

# --- Extract ---
extract_zips(
    [f for f in zip_files if f == "BB_Mats_1K.zip"],
    mats_1k_dir, "BB Mats 1K"
)

extract_zips(
    [f for f in zip_files if f.startswith("BB_Mats_4k")],
    mats_4k_dir, "BB Mats 4K"
)

edgewear_prefixes = ("Dents", "Dust", "Edgewear_and_Particles", "Rust", "Scratches", "Smudge_and_Stains")
extract_zips(
    [f for f in zip_files if any(f.startswith(p) for p in edgewear_prefixes)],
    edgewear_dir, "Edgewear"
)

extract_zips(
    [f for f in zip_files if f == "HDRi.zip"],
    hdri_dir, "HDRi"
)

print(f"\nDone! Total time: {time.time() - start_time:.1f}s")
