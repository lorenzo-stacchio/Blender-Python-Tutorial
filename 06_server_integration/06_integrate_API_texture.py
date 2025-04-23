import bpy
import requests

server_url = "http://127.0.0.1:5000/download-texture"
response = requests.get(server_url)
home_dir = "C:/Users/Chiqu/Desktop/BLENDER SCRIPTING/Blender-Python-Tutorial/server_integration/downloaded/"

# Check if the request was successful
if response.status_code == 200:
    # Save the content to a local file
    with open(f'{home_dir}/downloaded_texture.png', 'wb') as f:
        f.write(response.content)
    print("Texture file downloaded successfully.")
else:
    print(f"Failed to download OBJ file. Status code: {response.status_code}")

# Import the OBJ file
cubemesh = bpy.data.objects.get("Cube")
image_path = f'{home_dir}/downloaded_texture.png'

# Crea un nuovo materiale
material_name = "MaterialeConTexture"
material = bpy.data.materials.new(name=material_name)
material.use_nodes = True

# Ottieni i nodi del materiale
nodes = material.node_tree.nodes
links = material.node_tree.links

# Rimuovi i nodi esistenti
nodes.clear()

# Crea i nodi necessari
output_node = nodes.new(type='ShaderNodeOutputMaterial')
bsdf_node = nodes.new(type='ShaderNodeBsdfPrincipled')
texture_node = nodes.new(type='ShaderNodeTexImage')

# Posiziona i nodi (opzionale, solo per organizzazione visiva)
output_node.location = (800, 0)
bsdf_node.location = (400, 0)
texture_node.location = (0, 0)

# Carica l'immagine e assegnala al nodo di texture
image = bpy.data.images.load(image_path)
texture_node.image = image

# Collega i nodi
links.new(texture_node.outputs['Color'], bsdf_node.inputs['Base Color'])
links.new(bsdf_node.outputs['BSDF'], output_node.inputs['Surface'])

# Assegna il materiale all'oggetto
if cubemesh.data.materials:
    # Sostituisci il primo materiale
    cubemesh.data.materials[0] = material
else:
    # Aggiungi il materiale
    cubemesh.data.materials.append(material)
    
print("Texture Loaded Succesfully")