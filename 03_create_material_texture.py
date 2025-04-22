import os
import bpy
import config 


sep_len = 20 
print("-" * sep_len + "Creo Texture e Assegno a Cubo" + "-" * sep_len) ### ignore this, just for formatting prints

# Aggiunta di un cubo

cubemesh = bpy.data.objects.get("Cube") ### prendo cubo esistente nella scena

print(cubemesh.name)

## CHANGE WORKING DIR 

curr_dir = "C:/Users/Chiqu/Desktop/BLENDER SCRIPTING/Blender-Python-Tutorial/"

image_path = curr_dir + "images/minecraft.png"

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