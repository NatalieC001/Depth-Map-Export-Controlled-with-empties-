# Depthmap Export for Blender

A high-precision, one-click solution for exporting normalized 16-bit depth maps.

---

## Overview

This Blender add-on streamlines the technical workflow of generating depth data. It automates compositor node configuration, ensures data normalization, and exports high-bit-depth PNG files compatible with external 3D, VFX, and AI applications.

## Key Features

* **16-bit Precision**: Exports high-bit-depth PNG files to prevent banding.
* **Automated Workflow**: Configures compositor nodes automatically during export.
* **Data Normalization**: Scales Z-depth data for immediate use in external software.
* **Non-Destructive**: Restores original render settings and node setups after export.

## Installation

1. Download the `depthmap_export.py` file.
2. Open **Blender**.
3. Navigate to **Edit > Preferences > Add-ons**.
4. Click **Install** and select the downloaded file.
5. Enable **Render: Depthmap Export**.

<img width="390" height="173" alt="Screenshot 2026-03-02 190318" src="https://github.com/user-attachments/assets/463a39ee-a57b-4034-8cff-48b9d452e6bf" />

## Usage
Set up your bender scene and create 2 empties "Near" represtnts the top most height, and "Far" the bottom most (see image)
1. Open the **Properties** editor.
2. Select the **Render** tab.
3. Locate the **Depth Export** panel.
4. Click **Export Depthmap (.png)**.
5. Add the empties to the feilds
6. Choose your destination folder and filename.

<img width="610" height="609" alt="Screenshot 2026-03-02 185446" src="https://github.com/user-attachments/assets/b9c37b49-2759-4c75-a97d-fd5e2895fd59" />

## Technical Specifications

| Feature | Specification |
| --- | --- |
| **Engine** | EEVEE NEXT (Blender 4.2+) |
| **Bit Depth** | 16-bit PNG |
| **Output 1** | `[filename]_depthmap_Depth.png` |

<img width="716" height="514" alt="Screenshot 2026-03-02 185552" src="https://github.com/user-attachments/assets/0274437c-670a-4733-b780-65775aaea1aa" />

---
