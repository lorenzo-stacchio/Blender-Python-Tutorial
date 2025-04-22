import bpy
 
sep_len = 20 
print("-" * sep_len + "Creo Cubo" + "-" * sep_len) ### ignore this, just for formatting prints

# Aggiunta di un cubo

bpy.ops.mesh.primitive_cube_add(size=2, location=(0, 0, 0))

# Rendering dell'immagine corrente

## SAVE IMAGE RENDER
home_path = "C:/Users/Chiqu/Desktop/BLENDER SCRIPTING/Blender-Python-Tutorial/"
bpy.context.scene.render.filepath = home_path + "screenshot.png"
bpy.ops.render.render(write_still=True)
