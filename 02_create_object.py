import bpy
 
sep_len = 20 
print("-" * sep_len + "Creo Cubo" + "-" * sep_len) ### ignore this, just for formatting prints

# Aggiunta di un cubo

cubemesh = bpy.ops.mesh.primitive_cube_add(size=2, location=(0, 0, 0))

# bpy.ops.mesh.primitive_uv_sphere_add(location = (5,5,5))
# bpy.ops.mesh.primitive_plane_add()
# bpy.ops.mesh.primitive_monkey_add()


# Retrieve the newly created cube --> oggetto creato è per forza attivo a meno di altri script che tolgano il focus
cubemesh = bpy.context.active_object

# Optionally, rename the cube
cubemesh.name = "MyCube"

print(cubemesh.name)