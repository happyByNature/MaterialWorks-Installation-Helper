# MaterialWorks-Installation-Helper

This is a helper to install MaterialWorks addon of BlenderBros (www.blenderbros.com/materialworks)

## Prerequisites

**Assuming you know what GitHub and "git clone" are and how to run python scripts:**

1. Download all files from MW website and put them in the **same folder** (like Downloads/MW_23032026_1-2e).
2. Except for the main addon file like (MaterialWorks-1.2e.zip), put it in a separate folder.

***Notice, they have versions increment like a, b, c, etc., so download the farthest version from the beginning of the Alphabets (means "c" version is more recent than "a" version).***

## How to use

Run python script mwInstallationHelper.py and give source folder as input:
```bash
python mwInstallationHelper.py <source_dir>
```

Example, navigate to the folder where mwInstallationHelper.py is located and run the script:
```bash
cd E:\GitHub\MaterialWorks-Installation-Helper
py .\mwInstallationHelper.py "C:\Users\username\Downloads\MW_23032026_1-2e"
```
As a result, you will get a new folder named "MW_23032026_1-2e_Ready" in the same location as the source folder; this folder is "ready to use" in Blender. You can refence it in Blender or move to a desired location and point to it.

## What the script does

1. Validates that the source folder exists and contains at least one zip file.
2. Creates a `<source_folder>_Ready` target folder next to the source folder (clears it if it already exists).
3. Extracts zip files into the following structure:
   ```
   <source_folder>_Ready/
   ├── Mats/
   │   ├── BB Mats 1K/     ← BB_Mats_1K.zip
   │   ├── BB Mats 4K/     ← BB_Mats_4k*.zip
   │   ├── Edgewear/       ← Dents, Dust, Edgewear_and_Particles, Rust, Scratches, Smudge_and_Stains zips
   │   └── HDRi/           ← HDRi.zip
   └── Details/            ← Details.zip
       ├── Trims/          ← Trims*.zip
       └── Decals/         ← Decals*.zip
   ```
4. Warns about any zip files in the source folder that were not processed.
5. Prints per-category and total execution time.