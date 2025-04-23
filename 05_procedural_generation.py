import os
import bpy
import time
import numpy as np 
import random

## TODO: se crasha, eseguire dentro blender e funziona

def spawn_cube(name, location_x=0,location_y=0,location_z = 0, size = 3):
    cubemesh = bpy.ops.mesh.primitive_cube_add(size=size, scale = (1,1,1), enter_editmode = False, align = "WORLD", location=(location_x, location_y, location_z))
    cubemesh = bpy.context.active_object
    cubemesh.name = name
    ## assign random texture
    # Decide randomly whether to assign red or black material
    if random.random() < 0.5:
        color = (1, 0, 0, 1)  # Red
        mat_name = "RedMaterial"
    else:
        color = (0, 0, 0, 1)  # Black
        mat_name = "BlackMaterial"

    # Check if the material already exists
    if mat_name in bpy.data.materials:
        mat = bpy.data.materials[mat_name]
    else:
        # Create a new material
        mat = bpy.data.materials.new(name=mat_name)
        mat.use_nodes = True
        bsdf = mat.node_tree.nodes.get("Principled BSDF")
        if bsdf:
            bsdf.inputs['Base Color'].default_value = color

    # Assign the material to the cube
    if cubemesh.data.materials:
        cubemesh.data.materials[0] = mat
    else:
        cubemesh.data.materials.append(mat)


sep_len = 20 
print("-" * sep_len + "Creazione piano di cubi" + "-" * sep_len) ### ignore this, just for formatting prints

# Aggiunta di un cubo

n_cubes = 200
width,height = 600, 1200

area = width*height
area_cube = area//n_cubes
side = np.sqrt(area_cube)

## generate coordinates
offset_x, offset_y = side, side
cube_size = min(offset_x, offset_x)

actual_x, actual_y = 0,0

idx = 0

while (actual_x < width) and (actual_y < height):
    while actual_x < width:
        actual_x += offset_x
        print(actual_x,actual_y)
        ## SPAWN CUBE WITH THESE LOCATIONS
        name = f"Cube_{idx}"
        spawn_cube(name = name, location_x = actual_x, location_y = actual_y, size = cube_size)
        # time.sleep(2)
        idx +=1
        # break
    # if idx > 2:
    #     break
    actual_y += offset_y
    actual_x = 0
    # break