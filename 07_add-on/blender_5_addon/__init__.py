import random

import bpy
from bpy.props import IntProperty, PointerProperty


bl_info = {
    "name": "Blender 5 Tutorial Add-on",
    "author": "Blender Python Tutorial",
    "version": (1, 0, 0),
    "blender": (5, 0, 0),
    "location": "View3D > Sidebar > Dev",
    "description": "Tutorial panels updated for Blender 5.0",
    "category": "3D View",
}


class BLENDER5ADDON_PG_TemplateProperties(bpy.types.PropertyGroup):
    my_int: IntProperty(
        name="My Integer",
        description="An example integer property",
        default=10,
        min=0,
        max=100,
    )


class BLENDER5ADDON_PT_TemplatePanel(bpy.types.Panel):
    bl_label = "My Add-on Panel"
    bl_idname = "BLENDER5ADDON_PT_template_panel"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = 'Dev'

    def draw(self, context):
        layout = self.layout
        layout.label(text="Hello, Blender!")

        props = context.scene.blender5addon_tool
        layout.prop(props, "my_int")


class BLENDER5ADDON_PT_CubePanel(bpy.types.Panel):
    bl_label = "COBJ"
    bl_idname = "BLENDER5ADDON_PT_cube_panel"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = 'Dev'

    def draw(self, context):
        layout = self.layout
        layout.label(text="Spawn a Cube")
        layout.operator("object.blender5addon_cube_spawner")
        layout.prop(context.scene, "blender5addon_num_cubes")


class BLENDER5ADDON_OT_CubeSpawner(bpy.types.Operator):
    bl_idname = "object.blender5addon_cube_spawner"
    bl_label = "Cube Spawner"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        for _ in range(context.scene.blender5addon_num_cubes):
            x, y, z = random.sample(range(-10, 10), 3)
            bpy.ops.mesh.primitive_cube_add(size=2, location=(x, y, z))

        self.report({'INFO'}, "Cubes created")
        return {'FINISHED'}


classes = (
    BLENDER5ADDON_PG_TemplateProperties,
    BLENDER5ADDON_PT_TemplatePanel,
    BLENDER5ADDON_PT_CubePanel,
    BLENDER5ADDON_OT_CubeSpawner,
)


def register():
    for cls in classes:
        bpy.utils.register_class(cls)

    bpy.types.Scene.blender5addon_tool = PointerProperty(
        type=BLENDER5ADDON_PG_TemplateProperties
    )
    bpy.types.Scene.blender5addon_num_cubes = IntProperty(
        name="Number of Cubes to Spawn",
        description="Select number of cubes",
        default=10,
        min=0,
        max=100,
    )


def unregister():
    if hasattr(bpy.types.Scene, "blender5addon_num_cubes"):
        del bpy.types.Scene.blender5addon_num_cubes
    if hasattr(bpy.types.Scene, "blender5addon_tool"):
        del bpy.types.Scene.blender5addon_tool

    for cls in reversed(classes):
        bpy.utils.unregister_class(cls)


if __name__ == "__main__":
    try:
        unregister()
    except RuntimeError:
        pass

    register()
