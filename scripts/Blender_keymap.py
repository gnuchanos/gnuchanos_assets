keyconfig_version = (3, 6, 13)
keyconfig_data = \
[("Transform Modal Map",
  {"space_type": 'EMPTY', "region_type": 'WINDOW', "modal": True},
  {"items":
   [("CONFIRM", {"type": 'LEFTMOUSE', "value": 'PRESS', "any": True}, None),
    ("CONFIRM", {"type": 'RET', "value": 'PRESS', "any": True}, None),
    ("CONFIRM", {"type": 'NUMPAD_ENTER', "value": 'PRESS', "any": True}, None),
    ("CONFIRM", {"type": 'SPACE', "value": 'PRESS', "any": True}, None),
    ("CANCEL", {"type": 'RIGHTMOUSE', "value": 'PRESS', "any": True}, None),
    ("CANCEL", {"type": 'ESC', "value": 'PRESS', "any": True}, None),
    ("AXIS_X", {"type": 'X', "value": 'PRESS'}, None),
    ("AXIS_Y", {"type": 'Z', "value": 'PRESS'}, None),
    ("AXIS_Z", {"type": 'Y', "value": 'PRESS'}, None),
    ("PLANE_X", {"type": 'X', "value": 'PRESS', "shift": True}, None),
    ("PLANE_Y", {"type": 'Z', "value": 'PRESS', "shift": True}, None),
    ("PLANE_Z", {"type": 'Y', "value": 'PRESS', "shift": True}, None),
    ("CONS_OFF", {"type": 'C', "value": 'PRESS'}, None),
    ("TRANSLATE", {"type": 'G', "value": 'PRESS'}, None),
    ("VERT_EDGE_SLIDE", {"type": 'G', "value": 'PRESS'}, None),
    ("ROTATE", {"type": 'R', "value": 'PRESS'}, None),
    ("TRACKBALL", {"type": 'R', "value": 'PRESS'}, None),
    ("RESIZE", {"type": 'S', "value": 'PRESS'}, None),
    ("ROTATE_NORMALS", {"type": 'N', "value": 'PRESS'}, None),
    ("SNAP_TOGGLE", {"type": 'TAB', "value": 'PRESS', "shift": True}, None),
    ("SNAP_INV_ON", {"type": 'LEFT_CTRL', "value": 'PRESS', "any": True}, None),
    ("SNAP_INV_OFF", {"type": 'LEFT_CTRL', "value": 'RELEASE', "any": True}, None),
    ("SNAP_INV_ON", {"type": 'RIGHT_CTRL', "value": 'PRESS', "any": True}, None),
    ("SNAP_INV_OFF", {"type": 'RIGHT_CTRL', "value": 'RELEASE', "any": True}, None),
    ("ADD_SNAP", {"type": 'A', "value": 'PRESS'}, None),
    ("ADD_SNAP", {"type": 'A', "value": 'PRESS', "ctrl": True}, None),
    ("REMOVE_SNAP", {"type": 'A', "value": 'PRESS', "alt": True}, None),
    ("PROPORTIONAL_SIZE_UP", {"type": 'PAGE_UP', "value": 'PRESS', "repeat": True}, None),
    ("PROPORTIONAL_SIZE_DOWN", {"type": 'PAGE_DOWN', "value": 'PRESS', "repeat": True}, None),
    ("PROPORTIONAL_SIZE_UP", {"type": 'PAGE_UP', "value": 'PRESS', "shift": True, "repeat": True}, None),
    ("PROPORTIONAL_SIZE_DOWN", {"type": 'PAGE_DOWN', "value": 'PRESS', "shift": True, "repeat": True}, None),
    ("PROPORTIONAL_SIZE_UP", {"type": 'WHEELDOWNMOUSE', "value": 'PRESS'}, None),
    ("PROPORTIONAL_SIZE_DOWN", {"type": 'WHEELUPMOUSE', "value": 'PRESS'}, None),
    ("PROPORTIONAL_SIZE_UP", {"type": 'WHEELDOWNMOUSE', "value": 'PRESS', "shift": True}, None),
    ("PROPORTIONAL_SIZE_DOWN", {"type": 'WHEELUPMOUSE', "value": 'PRESS', "shift": True}, None),
    ("PROPORTIONAL_SIZE", {"type": 'TRACKPADPAN', "value": 'ANY'}, None),
    ("AUTOIK_CHAIN_LEN_UP", {"type": 'PAGE_UP', "value": 'PRESS', "repeat": True}, None),
    ("AUTOIK_CHAIN_LEN_DOWN", {"type": 'PAGE_DOWN', "value": 'PRESS', "repeat": True}, None),
    ("AUTOIK_CHAIN_LEN_UP", {"type": 'PAGE_UP', "value": 'PRESS', "shift": True, "repeat": True}, None),
    ("AUTOIK_CHAIN_LEN_DOWN", {"type": 'PAGE_DOWN', "value": 'PRESS', "shift": True, "repeat": True}, None),
    ("AUTOIK_CHAIN_LEN_UP", {"type": 'WHEELDOWNMOUSE', "value": 'PRESS'}, None),
    ("AUTOIK_CHAIN_LEN_DOWN", {"type": 'WHEELUPMOUSE', "value": 'PRESS'}, None),
    ("AUTOIK_CHAIN_LEN_UP", {"type": 'WHEELDOWNMOUSE', "value": 'PRESS', "shift": True}, None),
    ("AUTOIK_CHAIN_LEN_DOWN", {"type": 'WHEELUPMOUSE', "value": 'PRESS', "shift": True}, None),
    ("INSERTOFS_TOGGLE_DIR", {"type": 'T', "value": 'PRESS'}, None),
    ("NODE_ATTACH_ON", {"type": 'LEFT_ALT', "value": 'RELEASE', "any": True}, None),
    ("NODE_ATTACH_OFF", {"type": 'LEFT_ALT', "value": 'PRESS', "any": True}, None),
    ("AUTOCONSTRAIN", {"type": 'MIDDLEMOUSE', "value": 'ANY'}, None),
    ("AUTOCONSTRAINPLANE", {"type": 'MIDDLEMOUSE', "value": 'ANY', "shift": True}, None),
    ("PRECISION", {"type": 'LEFT_SHIFT', "value": 'ANY', "any": True}, None),
    ("PRECISION", {"type": 'RIGHT_SHIFT', "value": 'ANY', "any": True}, None),
    ],
   },
  ),
 ]


if __name__ == "__main__":
    # Only add keywords that are supported.
    from bpy.app import version as blender_version
    keywords = {}
    if blender_version >= (2, 92, 0):
        keywords["keyconfig_version"] = keyconfig_version
    import os
    from bl_keymap_utils.io import keyconfig_import_from_data
    keyconfig_import_from_data(
        os.path.splitext(os.path.basename(__file__))[0],
        keyconfig_data,
        **keywords,
    )
