import sys
import os
import shutil
import zipfile
import time
from datetime import datetime

# Version
v = "0.7.0"

# --- Colors ---
RESET  = "\033[0m"
BOLD   = "\033[1m"
CYAN   = "\033[96m"
GREEN  = "\033[92m"
YELLOW = "\033[93m"
RED    = "\033[91m"
DIM    = "\033[2m"

# Enable ANSI on Windows
if sys.platform == "win32":
    os.system("")

# --- Header ---
start_time = time.time()
print(f"\n{BOLD}{CYAN}*** MaterialWorks Installation Helper, Version: {v} ***{RESET}")
print(f"{DIM}Date/Time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}{RESET}")

if len(sys.argv) < 2:
    print(f"{RED}Error: No source folder provided.{RESET}")
    print(f"Usage: python mwInstallationHelper.py <source_dir>")
    sys.exit(1)

source_dir = os.path.abspath(sys.argv[1])
print(f"Source folder: {CYAN}{source_dir}{RESET}\n")

# --- Validate source folder ---
if not os.path.isdir(source_dir):
    print(f"{RED}Error: Source folder '{source_dir}' does not exist.{RESET}")
    sys.exit(1)

# --- Validate zip files exist ---
zip_files = [f for f in os.listdir(source_dir) if f.lower().endswith(".zip")]
if not zip_files:
    print(f"{RED}Error: No zip files found in '{source_dir}'.{RESET}")
    sys.exit(1)

# --- Create target folder ---
parent_dir = os.path.dirname(source_dir)
source_name = os.path.basename(source_dir)
target_dir = os.path.join(parent_dir, f"{source_name}_Ready")

if os.path.isdir(target_dir):
    print(f"{YELLOW}Target folder already exists. Clearing: {target_dir}{RESET}")
    for item in os.listdir(target_dir):
        item_path = os.path.join(target_dir, item)
        if os.path.isfile(item_path) or os.path.islink(item_path):
            os.remove(item_path)
        elif os.path.isdir(item_path):
            shutil.rmtree(item_path)
else:
    os.makedirs(target_dir)
    print(f"{GREEN}Created target folder: {target_dir}{RESET}")

# --- Create subfolders ---
mats_dir    = os.path.join(target_dir, "Mats")
details_dir = os.path.join(target_dir, "Details")

mats_1k_dir  = os.path.join(mats_dir, "BB Mats 1K")
mats_4k_dir  = os.path.join(mats_dir, "BB Mats 4K")
edgewear_dir = os.path.join(mats_dir, "Edgewear")
hdri_dir     = os.path.join(mats_dir, "HDRi")
trims_dir    = os.path.join(details_dir, "Trims")
decals_dir   = os.path.join(details_dir, "Decals")

for d in [mats_1k_dir, mats_4k_dir, edgewear_dir, hdri_dir, details_dir]:
    os.makedirs(d, exist_ok=True)

processed_files = set()

def extract_zips(files, dest, label):
    if not files:
        print(f"{YELLOW}Warning: No {label} zip files found, skipping.{RESET}")
        return
    print(f"\n{BOLD}[ {label} ]{RESET}")
    t = time.time()
    for fname in sorted(files):
        print(f"  {DIM}Extracting{RESET} {fname} {DIM}->{RESET} {label}/")
        with zipfile.ZipFile(os.path.join(source_dir, fname), "r") as z:
            z.extractall(dest)
        processed_files.add(fname)
    print(f"  {GREEN}Done in {time.time() - t:.1f}s{RESET}")

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

extract_zips(
    [f for f in zip_files if f == "Details.zip"],
    details_dir, "Details"
)

extract_zips(
    [f for f in zip_files if f.startswith("Trims")],
    trims_dir, "Trims"
)

extract_zips(
    [f for f in zip_files if f.startswith("Decals")],
    decals_dir, "Decals"
)

unprocessed = sorted(set(zip_files) - processed_files)
if unprocessed:
    print(f"\n{YELLOW}{BOLD}Warning: The following zip files were not processed:{RESET}")
    for f in unprocessed:
        print(f"  {YELLOW}- {f}{RESET}")

print(f"\n{BOLD}{GREEN}Done! Total time: {time.time() - start_time:.1f}s{RESET}")
