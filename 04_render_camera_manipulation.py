import bpy
import math 
import copy 
from mathutils import Vector, Euler

sep_len = 20 
print("-" * sep_len + "Render Image" + "-" * sep_len) ### ignore this, just for formatting prints

## SAVE IMAGE RENDER
curr_dir = "C:/Users/Chiqu/Desktop/BLENDER SCRIPTING/Blender-Python-Tutorial/"

bpy.context.scene.render.filepath = curr_dir + "screenshot.png"
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

bpy.context.scene.render.filepath = curr_dir + "screenshot_camera_render_changepose.png"
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

bpy.context.scene.render.filepath = curr_dir + "screenshot_camera_rotation.png"
bpy.ops.render.render(write_still=True)
print(matrix_pose)

# reset camera to initial
camera.matrix_world = matrix_pose



## ROTATION FACILE CON METODO ROTATE
## get initial matrix pose

matrix_pose = copy.deepcopy(camera.matrix_world)

if camera:
    camera.rotation_mode = 'XYZ'
    applied_rotation = Euler((0.0, -math.radians(10), 0.0), 'XYZ')
    # Ruotiamo la camera lungo l'asse Z 
    camera.rotation_euler.rotate(applied_rotation)
    ## per settare in maniera assoluta basta assegnare!
    
else:
    print("Camera non trovata.")

bpy.context.scene.render.filepath = curr_dir + "screenshot_camera_rotation_rotate.png"
bpy.ops.render.render(write_still=True)
print(matrix_pose)

# reset camera to initial
camera.matrix_world = matrix_pose



### METODO GENERALE


def setupCamera(scene, c):
    pi = math.pi

    scene.camera.rotation_euler[0] = c[0] * (pi / 180.0)
    scene.camera.rotation_euler[1] = c[1] * (pi / 180.0)
    scene.camera.rotation_euler[2] = c[2] * (pi / 180.0)

    scene.camera.location.x = c[3]
    scene.camera.location.y = c[4]
    scene.camera.location.z = c[5]

    return