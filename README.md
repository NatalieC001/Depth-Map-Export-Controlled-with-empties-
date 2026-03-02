# Depth Map Production and Displacement Workflow

This guide covers the complete two-part process: generating normalized 16-bit depth maps in Blender and applying them to 3D objects in Unity.

---

## Part 1: Depthmap Export (Blender)

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
| **Output** | `png or open exr` |

<img width="716" height="514" alt="Screenshot 2026-03-02 185552" src="https://github.com/user-attachments/assets/0274437c-670a-4733-b780-65775aaea1aa" />

---
---


## Part 2: Depthmap Stamper (Displacement & Baking)

The sister script for applying depth stamps to objects to create high-resolution assets within Blender.

### Overview
This script automates the application of 16-bit depth maps onto 3D geometry. It manages Multiresolution or Displacement modifiers to turn grayscale stamps into physical surface detail, preparing the mesh for final texture baking.

### Key Features
* **Stamp Application**: Quickly applies 16-bit PNG stamps to mesh surfaces.
* **Modifier Automation**: Automatically sets up the Displacement stack with correct texture settings.
* **Multi-Resolution Support**: Configures levels of detail for high-fidelity sculpting and baking.
* **Precision Mapping**: Uses the exported height data to drive exact vertex deformation.

### Installation
1. Download the `depthmap_stamper.py` file.
2. In Blender, go to **Edit > Preferences > Add-ons**.
3. Click **Install**, select the file, and enable **Object: Depthmap Stamper**.

<img width="327" height="270" alt="Placeholder interface How the plug in looks in the scene when ready to run" src="https://github.com/user-attachments/assets/c03333fc-fd2b-421e-950f-c1bff7a823ed" />
> **Image 2**: How the plugin looks in the scene when ready to run.

### Usage
1. Select the object intended for displacement.
2. Unwrap it
3. Open the **Depthmap Stamper** panel in the **Sidebar (N-panel)** or **Properties** editor.
4. Import the 16-bit depth texture into the texture field.
5. Adjust the strength and midlevel settings to match the original export range.
6. Click **Apply Displacement** to generate the modifier stack.

<img width="405" height="403" alt="unwaped uvs stacked" src="https://github.com/user-attachments/assets/e25b3fde-dff3-4892-a300-e498a5d77b02" />


<img width="443" height="673" alt="image" src="https://github.com/user-attachments/assets/228c6dde-47b6-4ba7-885a-ad9fa1a281d0" />

> **Image 3**: The settings and modifiers visible when running the script, the modifires get added automatically, just delete them to re-apply.

### Technical Specifications
| Feature | Specification |
| --- | --- |
| **Compatibility** | Blender 4.0+ |
| **Input Format** | 16-bit PNG / EXR |
| **Workflow** | Modifier-based Displacement / Multires |


<img width="539" height="499" alt="image" src="https://github.com/user-attachments/assets/f618b0bc-8637-45e6-a1e8-647271902046" />

<img width="596" height="687" alt="image" src="https://github.com/user-attachments/assets/465bf7c0-ea2d-4f01-a71f-4fb104a62ee8" />



> **Image 1**: The in-scene view of an object with the map applied.

<img width="443" height="473" alt="image" src="https://github.com/user-attachments/assets/c4e28872-7aed-47a1-9daf-b7e4724ab9cc" />

> **Image 4**: The 16-bit texture needed for import to drive displacement. (the same textures we created earlier)


<img width="518" height="481" alt="image" src="https://github.com/user-attachments/assets/e3472d06-50d3-4f02-912c-997837237dc7" />


---
