from flask import Flask, send_file
import os

app = Flask(__name__)

@app.route('/download-glb')
def download_obj():
    # Path to the OBJ file
    obj_path = os.path.join(app.root_path, 'models', 'stable.glb')

    # Check if the file exists
    if not os.path.isfile(obj_path):
        return "OBJ file not found.", 404

    # Serve the file for download
    return send_file(
        obj_path,
        as_attachment=True,
        download_name='generated_model.obj',
        mimetype='text/plain'
    )


@app.route('/download-texture')
def download_texture():
    # Path to the OBJ file
    texture_path = os.path.join(app.root_path, 'images', 'minecraft.png')

    # Check if the file exists
    if not os.path.isfile(texture_path):
        return "Texture file not found.", 404

    # Serve the file for download
    return send_file(
        texture_path,
        as_attachment=True,
        download_name='texture.png',
        mimetype='text/plain'
    )
    
if __name__ == '__main__':
    app.run(debug=True)
