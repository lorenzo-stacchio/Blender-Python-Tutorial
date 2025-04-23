import bpy
import requests

server_url = "http://127.0.0.1:5000/download-glb"
response = requests.get(server_url)
home_dir = "C:/Users/Chiqu/Desktop/BLENDER SCRIPTING/Blender-Python-Tutorial/server_integration/downloaded/"

# Check if the request was successful
if response.status_code == 200:
    # Save the content to a local file
    with open(f'{home_dir}/downloaded_model.glb', 'wb') as f:
        f.write(response.content)
    print("OBJ file downloaded successfully.")
else:
    print(f"Failed to download OBJ file. Status code: {response.status_code}")


# Import the OBJ file
# bpy.ops.wm.obj_import(filepath=f'{home_dir}/downloaded_model.obj')
bpy.ops.import_scene.gltf(filepath=f'{home_dir}/downloaded_model.glb')

# Get the imported object (assumes it's the last one added)
imported_obj = bpy.context.selected_objects[0]