import bpy
 
sep_len = 20 
print("-"*sep_len + "Loop Objects Example" + "-"*sep_len)
 ### ignore this, just for formatting prints


# Loop over all objects in the scene
for obj in bpy.data.objects:
    print(f"Object Name: {obj.name}, Type: {obj.type}")


## FILTER OBJECT BY NAME
# Loop over all mesh objects and filter by Type!
print("-"*sep_len + "Filter Example" + "-"*sep_len)


for obj in bpy.data.objects:
    # print(obj.__dir__())
    if obj.type == 'MESH':
        print(f"Mesh Object: {obj.name}")
        print(f"Object Coordinates: {obj.matrix_world}") # 4x4 coordinate omogenee
    
## MATERIALS
print("-"*sep_len + "Get Materials" + "-"*sep_len)

# Elenco nomi dei materiali
for mat in bpy.data.materials:
    print(mat.name)
