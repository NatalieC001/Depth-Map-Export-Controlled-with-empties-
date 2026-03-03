Tutorial: The Master Stamp Workflow basic outline of process

I. Introduction: The Universal Digital Die
Imagine creating a design once and applying it to any medium. This tutorial covers a unified workflow to create and capture16-bit depth maps in Blender and deploy them across three distinct industries. We are turning complex 3D geometry into a digital die—a "stamp" that works for digital assets and physical studio production.
<img width="1024" height="1008" alt="image" src="https://github.com/user-attachments/assets/a1cf9ee2-e2ef-420c-a873-e82df1481335" />

II. Why Use This Workflow?
<img width="1024" height="728" alt="image" src="https://github.com/user-attachments/assets/2843df4a-f32c-4e92-b433-894d8b8a1fb9" />

This process bridges the gap between digital precision and material craft. Think of this grayscale image as a digital rubbing. Just as you might press paper over a textured coin to see its surface, we use light and shadow to record height. In this view, white represents the highest points of your design while black represents the lowest base. Every shade of gray in between tells the computer exactly how far to push or pull a surface.
By capturing 16-bit height data, we eliminate the "banding" and jagged artifacts found in standard images. A regular photo only has 256 levels of gray, which creates harsh, stair-stepped edges in a physical object. This 16-bit workflow provides over 65,000 levels of depth, ensuring that every curve remains as smooth as if you had hand-burnished it.

For Game Developers, this means baking complex details into optimized 2D textures. For Analog Artists, it provides the exact depth needed for professional-grade embossing plates and a chance to preview a design before commiting time and materials.

The Workflow: Capture and Apply
<img width="390" height="173" alt="image" src="https://github.com/user-attachments/assets/07b46aa0-0b87-40af-a888-2e534ff7b85c" />
  <br><em>Visual: The Depthmap Export panel</em> 
<img width="327" height="270" alt="image" src="https://github.com/user-attachments/assets/c855190a-5cd2-4ace-b264-8d8d3c616d86" />
 <br><em>Visual: the Stamper panel.</em>    

We use two specialized Blender scripts to automate the technical setup. First, the Depthmap Export script. You define the height boundaries with "Near" and "Far" markers. One click automates the compositor to export a normalized 16-bit file. Second, the Depthmap Stamper script. This automates the displacement modifier stack and UV mapping. It allows you to "press" your captured design into any new mesh either by using the Sculpt Brush or the Displace Map, bypassing hours of manual modeling.

The Three Results: What You Will Achieve
Visual: Montage of the three specific end-points. By the end of this guide, you will have mastered three distinct outputs: One: A 3D stamp asset with high-fidelity surface detail ready for detailing your sculpts. Two: A physical master stamp for transferring patterns into clay or pliable mediums. One workflow. Three professional industries. 

<img width="1024" height="1008" alt="image" src="https://github.com/user-attachments/assets/02496ebb-c948-40ed-850a-3b2ea2aaede6" />

---


## The Digital-to-Physical Journey: From Screen to Surface


### Phase 1: Capturing the Digital Relief
The process starts in **Blender** with the **Depthmap Export** script. After a detailed relief is modeled, the scene is calibrated using two markers: **Near** and **Far**. The script automates the compositor and node setup to generate a 16-bit PNG or OpenEXR image.

<img width="390" height="173" alt="image" src="https://github.com/user-attachments/assets/3b91fe46-c8cb-4c8a-ad45-496d46b03a77" />

<img width="1024" height="741" alt="image" src="https://github.com/user-attachments/assets/54de334d-a985-4d89-875a-178adc971285" />


### Phase 2: Applying the Stamp and Creating the Master
Once the depth map is finalized, 
<img width="910" height="906" alt="image" src="https://github.com/user-attachments/assets/1b181a08-c96f-4ceb-84bd-6583a9f66021" />

the **Depthmap Stamper** script allows you to re-apply this relief to new 3D geometry with one click.
<img width="327" height="270" alt="image" src="https://github.com/user-attachments/assets/18174053-d563-445d-8b15-e02e9130e1d0" />

<img width="443" height="673" alt="image" src="https://github.com/user-attachments/assets/a111ea8c-42a8-43a4-9482-f3a969b21bbd" />


This script automates the modifier stack, and displacement settings to prepare a mesh for **3D printing**. This tool becomes the bridge between software and material, allowing for the consistent transfer of patterns that would be nearly impossible to achieve by hand.

### Phase 3: Stamping and Surface Formation in the real world
By pressing the master die into a pliable medium like paper clay, air-dry clay, or damp cardstock, the digital pattern is transferred with absolute fidelity. While the material is still soft, it can be shaped—such as placing a stamped clay slab into a concave mold to create a bowl, or embossing paper to create a textured artwork.

---

### Process Overview
| Phase | Environment | Key Mechanism | Final Output |
| :--- | :--- | :--- | :--- |
| **I. Capture** | Digital (Blender) | **Export Script** (1-Click) | 16-bit Normalized Heightmap |
| **II. Application** | Digital (Blender) | **Stamper Script** (1-Click) | Displacement-ready 3D Mesh |
| **III. Transfer** | Physical (3D Print) | Negative Die Production | Rigid Master Stamp |
| **IV. Impression** | Studio (Manual) | Pressing & Stamping | Relief Surface (Clay/Paper) |
| **V. Formation** | Studio (Manual) | Slump Molding/Folding | Final Shaped Object |

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

  <br><em>Figure 6: The depth map rendered either as open exr or png.</em>
</p>

---

## Part 2: Depthmap Stamper (Displacement & 3d printready geometry)
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
 <img width="1024" height="666" alt="image" src="https://github.com/user-attachments/assets/a99b1fcc-fbde-4983-a2cc-96a169b9be02" />
 <br><em>Figure 7: Project results showing a scene with two objects that have displacement maps added; one is an orb with a repeated pattern and the other is a flat single pattern with the stamp.</em>
</p>

<img width="1008" height="1024" alt="image" src="https://github.com/user-attachments/assets/d0f5400b-826b-475c-bbdf-fd0243e75b71" />

  <br><em>Figure 7: Printing the stamp ai mock.</em>
</p>

<img width="1024" height="666" alt="image" src="https://github.com/user-attachments/assets/7c112292-cc58-49ff-a253-f148848206d3" />

  <br><em>Figure 7: Cutting the clay.</em>
</p>

<p align="center">
 <img width="1024" height="666" alt="image" src="https://github.com/user-attachments/assets/e08cc76b-4052-45c4-ab74-32863adb70a8" />
  
  <br><em>Figure 9: The ceramic plate ai mock that is produced in its final form with the glazes on it.</em>

  <p align="center">
 <img width="1024" height="1008" alt="image" src="https://github.com/user-attachments/assets/26832cca-9f0e-4540-bf4c-59574d9e8aa1" />

  <br><em>Figure 9: Paper embossing ai mock.</em>

  <p align="center">
 <img width="1024" height="1008" alt="image" src="https://github.com/user-attachments/assets/7499c6a7-6e7d-4a3b-817c-295ffda8d6dd" />
  <br><em>Figure 9: Paper embossing notes.</em>
  
</p>
