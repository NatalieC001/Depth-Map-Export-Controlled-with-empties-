# Depthmap Export for Blender

A high-precision, one-click solution for exporting normalized 16-bit depth maps and diffuse textures.

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

<img width="390" alt="Add-on Installation" src="[https://github.com/user-attachments/assets/463a39ee-a57b-4034-8cff-48b9d452e6bf](https://github.com/user-attachments/assets/463a39ee-a57b-4034-8cff-48b9d452e6bf)" />

## Usage

1. Open the **Properties** editor.
2. Select the **Render** tab.
3. Locate the **True Depth Export** panel.
4. Click **Export Depthmap (.png)**.
5. Choose your destination folder and filename.

<img width="610" alt="Panel Location" src="[https://github.com/user-attachments/assets/b9c37b49-2759-4c75-a97d-fd5e2895fd59](https://github.com/user-attachments/assets/b9c37b49-2759-4c75-a97d-fd5e2895fd59)" />

## Technical Specifications

| Feature | Specification |
| --- | --- |
| **Resolution** | 1024 x 1024 px (Hardcoded) |
| **Engine** | EEVEE NEXT (Blender 4.2+) |
| **Bit Depth** | 16-bit PNG |
| **Output 1** | `[filename]_depthmap_Depth.png` |
| **Output 2** | `[filename]_depthmap_Diffuse.png` |

<img width="716" alt="Output Example" src="[https://github.com/user-attachments/assets/0274437c-185552-0274437c-670a-4733-b780-65775aaea1aa](https://www.google.com/search?q=https://github.com/user-attachments/assets/0274437c-185552-0274437c-670a-4733-b780-65775aaea1aa)" />

---
