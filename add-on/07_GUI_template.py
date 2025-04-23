import bpy


class MYADDON_PT_MainPanel(bpy.types.Panel):
    bl_label = "My Add-on Panel"
    bl_idname = "MYADDON_PT_main_panel"
    bl_space_type = 'VIEW_3D'      # Area where the panel will appear
    bl_region_type = 'UI'          # Region within the area
    bl_category = 'My Tools'       # Tab name in the sidebar

    def draw(self, context):
        layout = self.layout
        layout.label(text="Hello, Blender!")
        layout.operator("object.simple_operator")
        layout.prop(context.scene, "my_int")


class OBJECT_OT_SimpleOperator(bpy.types.Operator):
    bl_idname = "object.simple_operator"
    bl_label = "Simple Operator"

    def execute(self, context):
        self.report({'INFO'}, "Operator executed")
        return {'FINISHED'}


classes = [MYADDON_PT_MainPanel, OBJECT_OT_SimpleOperator]

def register():
    bpy.types.Scene.my_int = bpy.props.IntProperty(
        name="My Integer",
        description="An example integer property",
        default=10,
        min=0,
        max=100
    )
    for cls in classes:
        bpy.utils.register_class(cls)

def unregister():
    del bpy.types.Scene.my_int
    for cls in reversed(classes):
        bpy.utils.unregister_class(cls)


if __name__ == "__main__":
    register()
