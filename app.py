from flask import Flask, render_template, request, redirect, url_for, send_file
import torch
from gfpgan import GFPGANer
from PIL import Image
import cv2
import os

app = Flask(__name__, static_url_path='/static')

# Configure paths
input_image_folder = './input_images'
output_image_folder = './restored_images'
model_path = './GFPGANv1.4.pth'

# Ensure folders exist
os.makedirs(input_image_folder, exist_ok=True)
os.makedirs(output_image_folder, exist_ok=True)

# Initialize the GFPGANer model
restorer = GFPGANer(
    model_path=model_path,
    upscale=1,  # Keep 1 to maintain the original size
    arch='clean',
    channel_multiplier=2,
    bg_upsampler=None
)

@app.route('/')
def index():
    restored_image_url = None
    return render_template('index.html', restored_image_url=restored_image_url)

@app.route('/upload', methods=['POST'])
def upload_image():
    if 'file' not in request.files:
        return "No file part", 400
    
    file = request.files['file']
    if file.filename == '':
        return "No selected file", 400
    
    if file:
        # Save the uploaded file
        input_image_path = os.path.join(input_image_folder, file.filename)
        file.save(input_image_path)
        
        # Load the input image
        img = cv2.imread(input_image_path, cv2.IMREAD_COLOR)

        if img is None:
            return "Failed to load image", 400

        # Perform restoration using GFPGAN
        cropped_faces, restored_img, restored_faces = restorer.enhance(
            img, has_aligned=False, only_center_face=False
        )

        if isinstance(restored_img, list) and len(restored_img) > 0:
            restored_img = restored_img[0]  # Get the first restored image from the list
        else:
            return "Restoration failed", 500

        # Convert restored image from BGR (OpenCV format) to RGB (PIL format)
        restored_img = Image.fromarray(cv2.cvtColor(restored_img, cv2.COLOR_BGR2RGB))

        # Define output image path
        output_image_path = os.path.join(output_image_folder, f'restored_{file.filename}')
        restored_img.save(output_image_path)
        
        # Generate URL for the restored image and download link
        restored_image_url = url_for('restored_image', filename=f'restored_{file.filename}')
        download_link = url_for('download_image', filename=f'restored_{file.filename}')
        
        # Pass the URL and download link to the template
        return render_template('index.html', restored_image_url=restored_image_url, download_link=download_link)

@app.route('/restored/<filename>')
def restored_image(filename):
    return send_file(os.path.join(output_image_folder, filename), mimetype='image/png')

@app.route('/download/<filename>')
def download_image(filename):
    return send_file(os.path.join(output_image_folder, filename), as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)
