# The Master Stamp Workflow: From Digital Relief to Physical Surface
*Developed as part of the [Hummingbird in Paper](https://nataliec001.github.io/Hummingbird-in-Paper/) project.*

## I. Introduction – The Universal Digital Die

Create a design **once** in Blender and apply it across digital and physical mediums using a **unified 16-bit depth map workflow**.

This process turns detailed 3D geometry into a portable "digital stamp" (height/displacement map) usable in:

- Game asset texturing & sculpting
- 3D-printable master dies
- Analog studio production (clay, paper, embossing)

![Universal Digital Die Overview](https://github.com/user-attachments/assets/a1cf9ee2-e2ef-420c-a873-e82df1481335)

## II. Why This Workflow Matters

A 16-bit depth map captures over **65,000** levels of height (vs. 256 in 8-bit), eliminating banding and stair-stepping artifacts.

White = highest points  
Black = lowest base  
Grayscale values = precise height data

This precision enables smooth curves in both rendered/digital and physically embossed/printed results.

![16-bit vs 8-bit comparison / banding explanation](https://github.com/user-attachments/assets/2843df4a-f32c-4e92-b433-894d8b8a1fb9)

## Core Tools

The complete scripts are  in the repository:  
- `DepthMapExportWithEmpties.py` — one-click normalized 16-bit height map capture using Near/Far empties  
- `3dStamperFromDepthMap.py` — one-click application of the map as displacement

You can download them directly or install as add-ons 

![Depthmap Export panel](https://github.com/user-attachments/assets/07b46aa0-0b87-40af-a888-2e534ff7b85c)  
*Depthmap Export panel*

![Depthmap Stamper panel](https://github.com/user-attachments/assets/c855190a-5cd2-4ace-b264-8d8d3c616d86)  
*Depthmap Stamper panel*

## Three Professional Outputs – One Workflow

By the end you will produce:

1. High-fidelity **3D stamp/sculpting asset** (in Blender)  
2. **3D-printable master die/stamp** for physical production  
3. **Final embossed/relief objects** in clay, paper, or other pliable media

![Montage of the three results](https://github.com/user-attachments/assets/02496ebb-c948-40ed-850a-3b2ea2aaede6)

## The Complete Process Overview

| Phase          | Environment     | Key Tool / Mechanism              | Output                              |
|----------------|-----------------|------------------------------------|-------------------------------------|
| 1. Capture     | Blender         | DepthMapExportWithEmpties.py       | 16-bit normalized heightmap (PNG/EXR) |
| 2. Application | Blender         | Depthmap Stamper script            | Displacement-ready 3D mesh          |
| 3. Preparation | Digital → Physical | 3D printing (negative)          | Rigid master stamp / die            |
| 4. Impression  | Studio          | Manual pressing / stamping         | Relief in soft medium               |
| 5. Formation   | Studio          | Slumping, molding, folding         | Final shaped object                 |

## Part 1: Depthmap Export (Capture Phase)

**Goal**: Generate a clean, normalized 16-bit height map from any relief model.

### Installation
1. Go to the repository
2. Download `3dStamperFromDepthMap and DepthMapExportWithEmpties.py`
3. In Blender: **Edit > Preferences > Add-ons** → **Install** → select the .py file → enable **Render: Depthmap Export** 

### Usage
1. Model your relief geometry.
2. Add two **Empty** objects named exactly:
   - `Near` → topmost (highest) point
   - `Far` → bottommost (lowest) point
3. Go to **Properties > Render** tab → **Depth Export** panel
4. Assign the Near/Far empties
5. Choose output folder and filename
6. Click **Export Depthmap (.png)** (or EXR)

The script auto-configures the compositor, normalizes Z-depth between Near/Far, and restores original settings afterward.

**Recommended settings**:
- Engine: **EEVEE NEXT** (Blender 4.2+)
- Output: 16-bit PNG or OpenEXR

![Scene setup with Near/Far empties](https://github.com/user-attachments/assets/8491b7cd-89d4-42dd-93aa-18290cb5228c)  
*Figure 1: Scene with Near/Far markers and example relief model*

![Exported depth map example](https://github.com/user-attachments/assets/c51add01-9135-4b8f-a2aa-0dbcc281371f)  
*Figure 6: Resulting 16-bit depth map*

## Part 2: Depthmap Stamper (Application Phase)

**Goal**: Apply the captured depth map to any mesh as precise surface displacement.

### Installation
1. From the same repo: download the stamper script (e.g. `DepthmapStamper.py`)
2. Blender → **Edit > Preferences > Add-ons** → **Install** → enable **Object: Depthmap Stamper**

### Usage
1. Select target mesh
2. **UV unwrap** it (simple/overlapping UVs are fine for 3D printing)
3. Open **Depthmap Stamper** panel (N-panel or Properties)
4. Load your 16-bit depth map texture
5. Adjust **Strength** and **Midlevel** if needed
6. Choose mode (single stamp or repeating/tiled)
7. Click **Apply Displacement**

The script auto-creates and configures the displacement modifier stack.

![Stamper UI](https://github.com/user-attachments/assets/c03333fc-fd2b-421e-950f-c1bff7a823ed)  
*Figure 3: Stamper interface*

![Modifier & texture settings](https://github.com/user-attachments/assets/b8e4e262-7570-4c5a-b74c-3478b9d94e29)  
*Figure 2: Auto-applied settings*

![UV layout example (overlapping OK for print)](https://github.com/user-attachments/assets/d6737981-e0de-4503-a632-62b1d5d8b42c)  
*Figure 4: Typical UV layout for printing*

![Resulting modifier stack](https://github.com/user-attachments/assets/228c6dde-47b6-4ba7-885a-ad9fa1a281d0)  
*Figure 5: Generated modifiers in action*

## Gallery – Project Results

![Displacement applied to orb (tiled) and flat plate (single)](https://github.com/user-attachments/assets/a99b1fcc-fbde-4983-a2cc-96a169b9be02)

![3D printed stamp mockup](https://github.com/user-attachments/assets/d0f5400b-826b-475c-bbdf-fd0243e75b71)

![Cutting stamped clay](https://github.com/user-attachments/assets/7c112292-cc58-49ff-a253-f148848206d3)

![Final glazed ceramic plate mockup](https://github.com/user-attachments/assets/e08cc76b-4052-45c4-ab74-32863adb70a8)

![Paper embossing example](https://github.com/user-attachments/assets/26832cca-9f0e-4540-bf4c-59574d9e8aa1)

![Paper embossing detail/notes](https://github.com/user-attachments/assets/7499c6a7-6e7d-4a3b-817c-295ffda8d6dd)

---

## Blender Depth Map to Silhouette Emboss

Export your Z-depth map from Blender as a 16-bit PNG and drop it into Silhouette Studio. Use the Emboss Panel to apply a fill pattern to the image, which translates the grayscale gradients into the specific tool paths required for the Power Embosser. Place your material on the embossing mat and hit Send to let the machine's downward force execute the relief based on those generated paths.

---

One design → one capture → infinite applications across digital sculpting, 3D printing, and traditional studio craft.

Happy stamping! 🎨🖨️🚀
