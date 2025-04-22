import bpy
 
# Loop over all objects in the scene
for obj in bpy.data.objects:
    print(f"Object Name: {obj.name}, Type: {obj.type}")



