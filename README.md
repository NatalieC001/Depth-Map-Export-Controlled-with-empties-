# Depth Map Production and Displacement Workflow

This guide covers the complete two-part process: generating normalized 16-bit depth maps in Blender and applying them to 3D objects. This project provides a streamlined two-part solution for 3D artists to capture surface details and reapply them to new geometry. By using these scripts, you can convert complex 3D models into reusable "stamps" (depth maps) and apply them to other surfaces instantly, bypassing hours of manual sculpting or modeling.

### The Concept: Why Use Depth Maps?
In traditional 3D modeling, creating intricate surface details—like bolts, panels, or organic textures—is time-consuming. A Depth Map acts as a 3D "Stamp" of an object. It is a grayscale image where white represents the highest points and black represents the lowest.

### The Benefits
**Speed:** Create a library of custom shapes (stamps) to "press" into any mesh.

**Optimization:** High-detail geometry is converted into a 2D texture, which can be baked onto low-poly models for game engines like Unity or Unreal Engine.

**Consistency:** Repeat complex patterns across different objects with uniform scale and depth.

### Blender project files (not included)
Scalloped_Teal_Bellflower_Master_Stamp.blend
Bellflower Quartet _stamp_how to apply texture.blend

---

## Part 1: Depthmap Export (Blender)
A high-precision, one-click solution for exporting normalized 16-bit depth maps.

### Overview
This Blender add-on streamlines the technical workflow of generating depth data. It automates compositor node configuration, ensures data normalization, and exports high-bit-depth PNG files compatible with external 3D, VFX, and AI applications.

### Key Features
16-bit Precision: Exports high-bit-depth PNG files to prevent banding.
Automated Workflow: Configures compositor nodes automatically during export.
Data Normalization: Scales Z-depth data for immediate use in external software.
Non-Destructive: Restores original render settings and node setups after export.

### Installation
1. Download the `depthmap_export.py` file.
2. Open **Blender**.
3. Navigate to **Edit > Preferences > Add-ons**.
4. Click **Install** and select the downloaded file.
5. Enable **Render: Depthmap Export**.

<p align="center">
  <img width="390" src="https://github.com/user-attachments/assets/463a39ee-a57b-4034-8cff-48b9d452e6bf" alt="Add-on Installation" />
</p>

### Usage
Set up your Blender scene and create 2 empties: "Near" represents the topmost height, and "Far" the bottommost.

<p align="center">
  <img width="1024" height="741" alt="image" src="https://github.com/user-attachments/assets/8491b7cd-89d4-42dd-93aa-18290cb5228c" />

  <br><em>Figure 1: The scene inside of Blender showing the empties far and near plus the 3D model that I've created. That would later be the Ceramic Bowl.</em>
</p>

1. Open the **Properties** editor.
2. Select the **Render** tab.
3. Locate the **Depth Export** panel.
4. Click **Export Depthmap (.png)**.
5. Add the empties to the fields.
6. Choose your destination folder and filename.

### Technical Specifications
| Feature | Specification |
| --- | --- |
| **Engine** | EEVEE NEXT (Blender 4.2+) |
| **Bit Depth** | 16-bit PNG |
| **Output** | `png or open exr` |

<p align="center">
  <img width="539" height="539" alt="image" src="https://github.com/user-attachments/assets/c51add01-9135-4b8f-a2aa-0dbcc281371f" />

  <br><em>Figure 6: The depth map itself and how it looks when it's rendered.</em>
</p>

---

## Part 2: Depthmap Stamper (Displacement & Baking)
The sister script for applying depth stamps to objects to create high-resolution assets within Blender.

### Overview
This script automates the application of 16-bit depth maps onto 3D geometry. It manages Multiresolution or Displacement modifiers to turn grayscale stamps into physical surface detail, preparing the mesh for final texture baking.

### Key Features
Stamp Application: Quickly applies 16-bit PNG stamps to mesh surfaces.
Modifier Automation: Automatically sets up the Displacement stack with correct texture settings.
Multi-Resolution Support: Configures levels of detail for high-fidelity sculpting and baking.
Precision Mapping: Uses the exported height data to drive exact vertex deformation.

### Installation
1. Download the `depthmap_stamper.py` file.
2. In Blender, go to **Edit > Preferences > Add-ons**.
3. Click **Install**, select the file, and enable **Object: Depthmap Stamper**.

### Usage
1. Select the object intended for displacement.
2. Unwrap it.
3. Open the **Depthmap Stamper** panel in the **Sidebar (N-panel)** or **Properties** editor.
4. Import the 16-bit depth texture into the texture field.
5. Adjust strength and midlevel settings.
6. Click **Apply Displacement** to generate the modifier stack.

<p align="center">
  <img width="327" src="https://github.com/user-attachments/assets/c03333fc-fd2b-421e-950f-c1bff7a823ed" alt="Stamper UI" />
  <br><em>Figure 3: The depth map placer plugin view that shows which texture, the displacement strength, and the button to generate the relief.</em>
</p>


<br>
<p align="center">
  <img width="443" height="673" alt="image" src="https://github.com/user-attachments/assets/b8e4e262-7570-4c5a-b74c-3478b9d94e29" />

  <br><em>Figure 2: The settings that automatically get applied depending on if we are having it as a repeated image or a single image.</em>
</p>



<p align="center">
  <img width="1024" height="1008" alt="image" src="https://github.com/user-attachments/assets/d6737981-e0de-4503-a632-62b1d5d8b42c" />

  <br><em>Figure 4: The UV unwrap of how it looks with the faces being overlapped. Obviously, you can't do this for game characters because it would mess up the normals and shading, but it's OK for 3D printing.</em>
</p>

<p align="center">
  <img width="539" src="https://github.com/user-attachments/assets/228c6dde-47b6-4ba7-885a-ad9fa1a281d0" alt="Modifier Settings" />
  <br><em>Figure 5: An image showing the modifiers that are created and how it looks in the scene.</em>
</p>

### Technical Specifications
| Feature | Specification |
| --- | --- |
| **Compatibility** | Blender 4.0+ |
| **Input Format** | 16-bit PNG / EXR |
| **Workflow** | Modifier-based Displacement / Multires |

---

## Project Results



<p align="center">
  <img width="701" height="452" alt="image" src="https://github.com/user-attachments/assets/9e792fa2-718a-42ad-a8d3-d6d45716a9e0" />
  <br><em>Figure 7: Project results showing a scene with two objects that have displacement maps added; one is an orb with a repeated pattern and the other is a flat single pattern with the stamp.</em>
</p>

<p align="center">
<img width="539" height="1024" alt="image" src="https://github.com/user-attachments/assets/eeb1da07-b3a3-489a-9417-58e579cc0ce3" />
  <br><em>Figure 8: A mock up visualization of the cutter stamp finished so we can imagine what it looks like to print out the stamp used to cut ceramics.</em>
</p>

<p align="center">
  <img width="539" src="https://github.com/user-attachments/assets/e3472d06-50d3-4f02-912c-997837237dc7" alt="Final Result" />
  <br><em>Figure 9: The ceramic plate that is produced in its final form with the glazes on it.</em>
</p>
