bl_info = {
    "name": "Depth Map Export (Controlled with empties)",
    "description": "Camera-based depth export using two empties as near/far bounds",
    "author": "Natalie Coulam",
    "version": (1, 1, 0),
    "blender": (4, 2, 0),
    "category": "Render",
}

import bpy
import os
from bpy_extras.io_utils import ExportHelper

# --------------------------------------------------------
# Utility,  
# --------------------------------------------------------

def distance_from_camera(obj, cam):
    return (obj.matrix_world.translation - cam.matrix_world.translation).length

# --------------------------------------------------------
# Operator
# --------------------------------------------------------

class EXPORT_OT_true_depth(bpy.types.Operator, ExportHelper):
    """Export Controlled Depth Map"""
    bl_idname = "export.controlled_depthmap"
    bl_label = "Export Depth Map"

    # The extension is handled dynamically in invoke
    filename_ext = ".exr"

    def execute(self, context):
        scene = context.scene
        cam = scene.camera
        near_empty = scene.true_depth_near
        far_empty = scene.true_depth_far

        if not cam:
            self.report({'ERROR'}, "No active camera.")
            return {'CANCELLED'}

        if not near_empty or not far_empty:
            self.report({'ERROR'}, "Assign both Near and Far empties.")
            return {'CANCELLED'}

        # Calculate camera-relative distances
        near_distance = distance_from_camera(near_empty, cam)
        far_distance = distance_from_camera(far_empty, cam)

        min_depth = min(near_distance, far_distance)
        max_depth = max(near_distance, far_distance)

        # Enable compositor
        scene.use_nodes = True
        tree = scene.node_tree
        tree.nodes.clear()
        scene.render.use_compositing = True
        context.view_layer.use_pass_z = True

        # Force EEVEE NEXT
        scene.render.engine = 'BLENDER_EEVEE_NEXT'

        # Nodes
        rl = tree.nodes.new('CompositorNodeRLayers')
        rl.location = (-600, 0)

        map_range = tree.nodes.new('CompositorNodeMapRange')
        map_range.location = (-200, 0)
        map_range.inputs['From Min'].default_value = min_depth
        map_range.inputs['From Max'].default_value = max_depth
        map_range.inputs['To Min'].default_value = 1.0
        map_range.inputs['To Max'].default_value = 0.0
        map_range.use_clamp = True

        file_output = tree.nodes.new('CompositorNodeOutputFile')
        file_output.location = (200, 0)
        file_output.base_path = os.path.dirname(self.filepath)
        
        # Configure format based on user selection
        if scene.true_depth_format == 'EXR':
            file_output.format.file_format = 'OPEN_EXR'
            file_output.format.color_depth = '32'
            file_output.format.color_mode = 'RGBA' # Fixed for compatibility
        else:
            file_output.format.file_format = 'PNG'
            file_output.format.color_depth = '16'
            file_output.format.color_mode = 'BW'

        file_output.file_slots[0].path = os.path.splitext(
            os.path.basename(self.filepath))[0]

        # Links
        tree.links.new(rl.outputs['Depth'], map_range.inputs['Value'])
        tree.links.new(map_range.outputs['Value'], file_output.inputs[0])

        bpy.ops.render.render(write_still=True)

        self.report({'INFO'}, f"Depth map exported as {scene.true_depth_format}")
        return {'FINISHED'}

    def invoke(self, context, event):
        # Set the extension based on the UI setting before opening the browser
        if context.scene.true_depth_format == 'EXR':
            self.filename_ext = ".exr"
        else:
            self.filename_ext = ".png"
        return super().invoke(context, event)

# --------------------------------------------------------
# Panel
# --------------------------------------------------------

class RENDER_PT_true_depth(bpy.types.Panel):
    bl_label = "Depth Export with Empties"
    bl_idname = "RENDER_PT_true_depth"
    bl_space_type = 'PROPERTIES'
    bl_region_type = 'WINDOW'
    bl_context = "render"

    def draw(self, context):
        layout = self.layout
        scene = context.scene

        col = layout.column(align=True)
        col.label(text="Depth Bounds (Camera Relative):")
        col.prop(scene, "true_depth_near")
        col.prop(scene, "true_depth_far")

        layout.separator()
        
        row = layout.row(align=True)
        row.label(text="Export Format:")
        row.prop(scene, "true_depth_format", expand=True)

        layout.separator()
        layout.operator("export.controlled_depthmap",
                        text="Export Depth Map",
                        icon='IMAGE_ZDEPTH')

# --------------------------------------------------------
# Registration
# --------------------------------------------------------

def register():
    bpy.types.Scene.true_depth_near = bpy.props.PointerProperty(
        name="Near (White)",
        type=bpy.types.Object,
        description="Empty representing near/white depth bound"
    )

    bpy.types.Scene.true_depth_far = bpy.props.PointerProperty(
        name="Far (Black)",
        type=bpy.types.Object,
        description="Empty representing far/black depth bound"
    )

    bpy.types.Scene.true_depth_format = bpy.props.EnumProperty(
        name="Format",
        items=[
            ('EXR', "OpenEXR (32-bit)", "High precision floating point"),
            ('PNG', "PNG (16-bit)", "Standard high-quality image")
        ],
        default='EXR'
    )

    bpy.utils.register_class(EXPORT_OT_true_depth)
    bpy.utils.register_class(RENDER_PT_true_depth)

def unregister():
    del bpy.types.Scene.true_depth_near
    del bpy.types.Scene.true_depth_far
    del bpy.types.Scene.true_depth_format

    bpy.utils.unregister_class(EXPORT_OT_true_depth)
    bpy.utils.unregister_class(RENDER_PT_true_depth)

if __name__ == "__main__":
    register()
