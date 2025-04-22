import bpy
import math 
import copy 
from mathutils import Vector, Euler

sep_len = 20 
print("-" * sep_len + "Render Image" + "-" * sep_len) ### ignore this, just for formatting prints

## SAVE IMAGE RENDER
home_path = "C:/Users/Chiqu/Desktop/BLENDER SCRIPTING/Blender-Python-Tutorial/"
bpy.context.scene.render.filepath = home_path + "screenshot.png"
bpy.ops.render.render(write_still=True)




## RENDER CHANGING CAMERA POSE

# Sostituisci 'Camera' con il nome della tua camera
camera = bpy.data.objects.get("Camera")

## get initial matrix pose

matrix_pose = copy.deepcopy(camera.matrix_world)

if camera:
    bpy.context.scene.camera = camera
    
    offset = Vector((1.0, 0.0, 1.0))

    # Muoviamo la camera a sinistra e in basso (stiamo togliendo)   
    camera.location = camera.location - offset
    ## per settare in maniera assoluta basta assegnare!
    
else:
    print("Camera non trovata.")

bpy.context.scene.render.filepath = home_path + "screenshot_camera_render_changepose.png"
bpy.ops.render.render(write_still=True)
print(matrix_pose)

# reset camera to initial
camera.matrix_world = matrix_pose



### CAMERA ROTATION

## get initial matrix pose

matrix_pose = copy.deepcopy(camera.matrix_world)

if camera:
    camera.rotation_mode = 'XYZ'

    offset_radians_y = 10 ## dipende da posizionamento camera!

    # Ruotiamo la camera lungo l'asse Z 
    camera.rotation_euler.y -= math.radians(offset_radians_y)
    ## per settare in maniera assoluta basta assegnare!
    
else:
    print("Camera non trovata.")

bpy.context.scene.render.filepath = home_path + "screenshot_camera_rotation.png"
bpy.ops.render.render(write_still=True)
print(matrix_pose)

# reset camera to initial
camera.matrix_world = matrix_pose