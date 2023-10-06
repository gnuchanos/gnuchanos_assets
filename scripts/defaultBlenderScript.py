bl_info = {
    "name": "Set Origin for GnuChanGE",
    "author": "archkubi",
    "version": (0, 1),
    "blender": (3, 3, 11),
    "location": "View3d > Tool",
    "warning": "I learn blender scripting if you find bugs, please let me know",
    "wiki_url": "",
    "category": "GnuChanGE addons",
}

import bpy


class GnuChanOSSetOrigin(bpy.types.Panel):
    bl_label = "Set Origin for GnuChanGE"
    bl_idname = "PT_GnuChanOSSetORigin"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "GnuChanOS Addons"

    def draw(self, context):
        layout = self.layout
        obj = context.active_object

def register():
    bpy.utils.register_class(GnuChanOSSetOrigin)

def unregister():
    bpy.utils.unregister_class(GnuChanOSSetOrigin)

if __name__ == "__main__":
    register()