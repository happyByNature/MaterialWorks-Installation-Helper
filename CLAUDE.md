# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

A Python CLI utility that automates installation of the MaterialWorks addon for Blender (by BlenderBros). It takes a source folder of downloaded MW files and prepares a ready-to-use target folder.

## Running the Script

```bash
python helper.py <source_dir>
```

No external dependencies — uses Python standard library only.

## Expected Behavior

The script:

1. Print current date/time, script version, and source folder path
2. Validate that `<source_dir>` exists (exit with error if not)
3. Validate that at least one `.zip` file exists in `<source_dir>` (exit with error if none)
4. Create a target folder at `<parent_of_source_dir>/<source_dir_name>_Ready` — if it already exists, **delete all files in it**
5. Extracts zip files into the following structure:
   ```
   <source_dir>_Ready/
   ├── Mats/
   │   ├── BB Mats 1K/     ← BB_Mats_1K.zip
   │   ├── BB Mats 4K/     ← BB_Mats_4k*.zip
   │   ├── Edgewear/       ← Dents, Dust, Edgewear_and_Particles, Rust, Scratches, Smudge_and_Stains zips (prefix-matched)
   │   └── HDRi/           ← HDRi.zip
   └── Details/            ← Details.zip
       ├── Trims/          ← Trims*.zip (Trims/ created by Details.zip extraction)
       └── Decals/         ← Decals*.zip (Decals/ created by Details.zip extraction)
   ```

## Input File Layout

The user places all MW download files in a single source folder (e.g. `Downloads/MW_23032026_1-2e`), **except** for the main addon zip (`MaterialWorks-1.2e.zip`), which goes in a separate folder.
