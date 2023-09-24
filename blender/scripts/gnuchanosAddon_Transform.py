

bl_info = {
    "name": "GnuChanOS Transform for Ursina",
    "author": "archkubi",
    "version": (0, 1),
    "blender": (3, 3, 11),
    "location": "View3d > Tool",
    "warning": "I learn blender scripting if you find bugs, please let me know",
    "wiki_url": "",
    "category": "ursina addons",
}

import bpy

class GnuChanOSTransformPanel(bpy.types.Panel):
    bl_label = "Transform for Ursina"
    bl_idname = "PT_GnuChanOSTransformPanel"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "GnuChanOS Addons"

    def draw(self, context):
        layout = self.layout
        obj = context.active_object

        layout.prop(obj, "location", index=0, text="X Location")
        layout.prop(obj, "location", index=2, text="Y Location")
        layout.prop(obj, "location", index=1, text="Z Location")
        
        row = layout.row()
        row = layout.row()
        row = layout.row()
        
        layout.prop(obj, "rotation_euler", index=0, text="X Rotation")
        layout.prop(obj, "rotation_euler", index=2, text="Y Rotation")
        layout.prop(obj, "rotation_euler", index=1, text="Z Rotation")
        
        row = layout.row()
        row = layout.row()
        row = layout.row()
        
        layout.prop(obj, "scale", index=0, text="X Scale")
        layout.prop(obj, "scale", index=2, text="Y Scale")
        layout.prop(obj, "scale", index=1, text="Z Scale")

def register():
    bpy.utils.register_class(GnuChanOSTransformPanel)

def unregister():
    bpy.utils.unregister_class(GnuChanOSTransformPanel)

if __name__ == "__main__":
    register()



        