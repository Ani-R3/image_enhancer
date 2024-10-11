# Image_Enhancer
Overview
This project enhances images using AI-based techniques. It leverages GFPGAN for face restoration, improving image quality while maintaining the original size.

Features
AI-powered image enhancement.
Utilizes pre-trained models for face restoration.
Easy setup with virtual environment and pre-configured dependencies.
Setup Instructions
1. Clone the Repository

git clone https://github.com/Ani-R3/image_enhancer.git

cd image-enhancer

2. Create a Python Virtual Environment
Before proceeding, ensure you have Python installed. Create a virtual environment to manage project dependencies:


Copy code

python -m venv venv

source venv/bin/activate  # For Linux/macOS
or

venv\Scripts\activate  # For Windows

3. Install Required Libraries
Install all the dependencies listed in the requirements.txt file:


Copy code
pip install -r requirements.txt

4. Download Pre-Trained Model

You need to download the pre-trained model required for GFPGAN face restoration. Run the following command to download the model:


Copy code

wget https://github.com/TencentARC/GFPGAN/releases/download/v1.3.0/GFPGANv1.4.pth -O ./GFPGANv1.4.pth
Make sure you have the GFPGAN library installed before running the command:

Copy code

pip install gfpgan

5. Run the Project
   
After setting up, you can run the image enhancer by executing the appropriate Python scripts in the project. For example:

Copy code
python main.py
Notes
Ensure your Python version is compatible with the libraries (Python 3.7 or higher recommended).
If you encounter any issues related to large files or GitHub LFS limits, consider hosting large models externally and linking them in the project.
