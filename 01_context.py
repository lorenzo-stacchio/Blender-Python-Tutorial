import bpy
 
sep_len = 20 
print("-" * sep_len + "Context Active Object" + "-" * sep_len) ### ignore this, just for formatting prints

## Oggetto attivo
obj = bpy.context.active_object
print(obj.name)


print("-"*sep_len + "Actual Mode" + "-"*sep_len) ### ignore this, just for formatting prints

# Modalità corrente (es. 'EDIT_MESH', 'OBJECT')
mode = bpy.context.mode
print("Mode:", mode)


# Loop over all mesh objects and filter by Type!
print("-"*sep_len + "Get Object Active on ViewPort" + "-"*sep_len)

# Loop over selected objects
for obj in bpy.context.selected_objects:
    print(f"Selected Object: {obj.name}")
    