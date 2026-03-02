Depthmap Export
Description
A Blender add-on providing a one-click solution for exporting normalized 16-bit depth maps and diffuse images.

Features

Exports high-bit-depth PNG files.
Automatically configures compositor nodes.
Normalizes Z-depth data for immediate use in external software.
Restores original render settings after export.

Installation
Download the Python file.

Open Blender.
Navigate to Edit > Preferences > Add-ons.

Click Install and select the file.
Enable Render: Depthmap Export.

Usage
Open the Properties editor.

Go to the Render tab.
Locate the True Depth Export panel.
Click Export Depthmap (.png).
Select a destination and filename.

Technical Details
Resolution: Hardcoded to 1024x1024.
Engine: Uses EEVEE NEXT (Blender 4.2+).
Outputs: Generates two files: [filename]_depthmap_Depth.png and [filename]_depthmap_Diffuse.png.

<img width="610" height="609" alt="Screenshot 2026-03-02 185446" src="https://github.com/user-attachments/assets/b9c37b49-2759-4c75-a97d-fd5e2895fd59" />

<img width="716" height="514" alt="Screenshot 2026-03-02 185552" src="https://github.com/user-attachments/assets/0274437c-670a-4733-b780-65775aaea1aa" />


