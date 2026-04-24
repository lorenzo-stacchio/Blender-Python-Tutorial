import bpy
from bpy.props import IntProperty, PointerProperty


bl_info = {
    "name": "My Add-on Panel",
    "author": "Blender Python Tutorial",
    "version": (1, 0, 0),
    "blender": (5, 0, 0),
    "location": "View3D > Sidebar > Dev",
    "description": "Example View3D sidebar panel with a custom scene property group",
    "category": "3D View",
}


class MyProperties(bpy.types.PropertyGroup):
    my_int: IntProperty(default=10)


class MYADDON_PT_TemplatePanel(bpy.types.Panel):
    bl_label = "My Add-on Panel"
    bl_idname = "MYADDON_PT_template_panel"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = 'Dev'

    def draw(self, context):
        layout = self.layout
        layout.label(text="Hello, Blender!")

        props = context.scene.my_tool
        layout.prop(props, "my_int")


classes = [MyProperties, MYADDON_PT_TemplatePanel]


def register():
    for cls in classes:
        bpy.utils.register_class(cls)

    bpy.types.Scene.my_tool = PointerProperty(type=MyProperties)


def unregister():
    if hasattr(bpy.types.Scene, "my_tool"):
        del bpy.types.Scene.my_tool

    for cls in reversed(classes):
        bpy.utils.unregister_class(cls)


if __name__ == "__main__":
    try:
        unregister()
    except RuntimeError:
        pass

    register()
