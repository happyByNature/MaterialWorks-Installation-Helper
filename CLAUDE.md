# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

A Python CLI utility that automates installation of the MaterialWorks addon for Blender (by BlenderBros). It takes a source folder of downloaded MW files and prepares a ready-to-use target folder.

## Running the Script

```bash
python mwInstallationHelper.py <source_dir>
```

No external dependencies — uses Python standard library only.

## Expected Behavior

The script (currently in early development) will:

1. Print current date/time, script version, and source folder path
2. Validate that `<source_dir>` exists (exit with error if not)
3. Validate that at least one `.zip` file exists in `<source_dir>` (exit with error if none)
4. Create a target folder at `<parent_of_source_dir>/<source_dir_name>_Ready` — if it already exists, **delete all files in it**
5. Create `BB Mats 1K`, `BB Mats 4K`, `Edgewear`, `HDRi` subfolders inside the target folder
6. Extract `BB_Mats_1K.zip` into `BB Mats 1K/`
7. Extract all `BB_Mats_4k*.zip` files into `BB Mats 4K/`
8. Extract Edgewear zips (`Dents`, `Dust`, `Edgewear_and_Particles`, `Rust`, `Scratches`, `Smudge_and_Stains`) into `Edgewear/` — matched by filename prefix to handle versioning suffixes
9. Extract `HDRi.zip` into `HDRi/`

## Input File Layout

The user places all MW download files in a single source folder (e.g. `Downloads/MW_23032026_1-2e`), **except** for the main addon zip (`MaterialWorks-1.2e.zip`), which goes in a separate folder.
