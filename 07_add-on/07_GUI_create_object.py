import bpy
import random
from bpy.props import IntProperty


bl_info = {
    "name": "Cube Object Prefab",
    "author": "Blender Python Tutorial",
    "version": (1, 0, 0),
    "blender": (5, 0, 0),
    "location": "View3D > Sidebar > Dev",
    "description": "Spawn multiple cube objects from a View3D sidebar panel",
    "category": "Object",
}


class COBJ_PT_MainPanel(bpy.types.Panel):
    bl_label = "COBJ"
    bl_idname = "COBJ_PT_main_panel"
    bl_space_type = 'VIEW_3D'      # Area where the panel will appear
    bl_region_type = 'UI'          # Region within the area
    bl_category = 'Dev'            # Tab name in the sidebar

    def draw(self, context):
        layout = self.layout
        layout.label(text="Spawn a Cube")
        layout.operator("object.creator_simple_operator")
        layout.prop(context.scene, "num_cubes")


class OBJECT_OT_SimpleOperator(bpy.types.Operator):
    bl_idname = "object.creator_simple_operator"
    bl_label = "Cube Spawner"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        self.report({'INFO'}, "Operator executed")
        for i in range(context.scene.num_cubes):
            x, y, z = random.sample(range(-10, 10), 3)
            bpy.ops.mesh.primitive_cube_add(size=2, location=(x, y, z))
        return {'FINISHED'}


classes = [COBJ_PT_MainPanel, OBJECT_OT_SimpleOperator]


def register():
    for cls in classes:
        bpy.utils.register_class(cls)
    bpy.types.Scene.num_cubes = IntProperty(
        name="Number of Cubes to Spawn",
        description="Select number of cubes",
        default=10,
        min=0,
        max=100
    )


def unregister():
    if hasattr(bpy.types.Scene, "num_cubes"):
        del bpy.types.Scene.num_cubes

    for cls in reversed(classes):
        bpy.utils.unregister_class(cls)


if __name__ == "__main__":
    try:
        unregister()
    except RuntimeError:
        pass

    register()
