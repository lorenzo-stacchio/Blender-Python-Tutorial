import bpy
 
sep_len = 20 
print("-" * sep_len + "Creo Cubo" + "-" * sep_len) ### ignore this, just for formatting prints

# Aggiunta di un cubo

cubemesh = bpy.ops.mesh.primitive_cube_add(size=2, location=(0, 0, 0))

# Retrieve the newly created cube --> oggetto creato è per forza attivo a meno di altri script che tolgano il focus
cubemesh = bpy.context.active_object

# Optionally, rename the cube
cubemesh.name = "MyCube"

print(cubemesh.name)