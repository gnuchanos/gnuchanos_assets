bl_info = {
    "name": "GnuChanOS Addons for GnuChanGE",
    "author": "archkubi",
    "version": (0, 1),
    "blender": (3, 3, 11),
    "location": "View3d > Tool",
    "warning": "I learn blender scripting if you find bugs, please let me know",
    "wiki_url": "",
    "category": "GnuChanGE addons",
}



import bpy
import os

# Checkbox to export selected objects or the entire scene
bpy.types.Scene.export_selected_objects = bpy.props.BoolProperty(
    name="Export Selected Objects",
    description="Export selected objects instead of the entire scene",
    default=False  # Default to exporting the entire scene
)

class panel(bpy.types.Panel):
    bl_label = "Obj Keyframes Export"
    bl_idname = "PT_panel"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "GnuChanOS Addons"

    def draw(self, context):
        layout = self.layout

        row = layout.row()
        row.label(text="Export obj Animation for Ursina", icon="CUBE")

        # Add text boxes for frame name and output folder
        layout.prop(context.scene, "obj_frame_name")
        layout.prop(context.scene, "obj_output_folder")

        # Checkbox to choose export mode
        layout.prop(context.scene, "export_selected_objects", text="Export Selected Objects")

        # Add a property for the number of frames to export
        layout.prop(context.scene, "num_frames_to_export")

        row = layout.row()
        row.operator(ExportFramesAsOBJOperator.bl_idname)

class ExportFramesAsOBJOperator(bpy.types.Operator):
    bl_idname = "object.export_frames_as_obj"
    bl_label = "Export Frames as OBJ"

    def execute(self, context):
        scene = bpy.context.scene

        # Get frame name, output folder, and export selection checkbox
        obj_frame_name = bpy.context.scene.obj_frame_name
        obj_output_folder = bpy.context.scene.obj_output_folder
        export_selected = bpy.context.scene.export_selected_objects
        num_frames_to_export = bpy.context.scene.num_frames_to_export

        if export_selected:
            objects_to_export = bpy.context.selected_objects
        else:
            objects_to_export = bpy.context.scene.objects

        frame_range = range(scene.frame_start, scene.frame_start + num_frames_to_export)

        for frame in frame_range:
            bpy.context.scene.frame_set(frame)
            obj_filename = f"{obj_frame_name}_{frame:04d}.obj"
            obj_filepath = os.path.join(obj_output_folder, obj_filename)

            bpy.ops.export_scene.obj(
                filepath=obj_filepath,
                use_selection=export_selected,
                use_animation=False,
                use_mesh_modifiers=True,
                use_normals=True,
                use_materials=True,  # Set this to True to export .mtl files
                use_edges=False,
                use_smooth_groups=False
            )

        return {'FINISHED'}

def register():
    bpy.utils.register_class(panel)
    bpy.utils.register_class(ExportFramesAsOBJOperator)
    bpy.types.Scene.obj_frame_name = bpy.props.StringProperty(
        name="Frame Name",
        description="Name to be used for each exported frame",
        default="frame"
    )
    bpy.types.Scene.obj_output_folder = bpy.props.StringProperty(
        name="Output Folder",
        description="Folder where OBJ and MTL files will be saved",
        default="/home/archkubi/animation"  # Default output folder path, change as needed
    )
    bpy.types.Scene.num_frames_to_export = bpy.props.IntProperty(
        name="Number of Frames",
        description="Number of frames to export",
        default=10  # Default to exporting 10 frames
    )

def unregister():
    bpy.utils.unregister_class(panel)
    bpy.utils.unregister_class(ExportFramesAsOBJOperator)
    del bpy.types.Scene.obj_frame_name
    del bpy.types.Scene.obj_output_folder
    del bpy.types.Scene.export_selected_objects
    del bpy.types.Scene.num_frames_to_export

if __name__ == "__main__":
    register()
