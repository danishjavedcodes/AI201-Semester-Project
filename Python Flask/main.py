from flask import Flask, send_file, render_template, request, redirect
app = Flask(__name__)
import base64
import io  
import os
from werkzeug.utils import secure_filename
import pathlib
import cv2
import matplotlib.pyplot as plt
import numpy as np

def generate_custom_name(original_file_name):
    return "my_custom_file_name" + pathlib.Path(original_file_name).suffix



app.config["IMAGE_UPLOADS"] = "/Users/u2021605/Desktop/Python Flask/static/Images"
app.config["ALLOWED_IMAGE_EXTENSIONS"] = ["PNG","JPG","JPEG"]

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/upload', methods=['GET', "POST"])
def upload():
    if request.method == "POST":
        image = request.files['file']
        

        if image.filename == '':
            print("Image must have name")
            return redirect(request.url)

        filename = "img.jpg"
        
        basedir = os.path.abspath(os.path.dirname(__file__))
        image.save(os.path.join(basedir,app.config["IMAGE_UPLOADS"],filename))
        
        

        return render_template("Filters_Page.html",filename=filename)
        
    return render_template('Filters_Page.html')

@app.route('/redirect')
def redirect():
    return render_template('Filters_Page.html')

@app.route('/Emboss')
def Emboss():
    input_path = '/Users/u2021605/Desktop/Python Flask/static/images/img.jpg' # input image path
    output_path = "/Users/u2021605/Desktop/Python Flask/static/images/output.png"
    loaded_img = cv2.imread(input_path)
    loaded_img = cv2.cvtColor(loaded_img,cv2.COLOR_BGR2RGB)
    plt.figure(figsize=(8,8))
    plt.imshow(loaded_img,cmap="gray")
    plt.axis("off")
    Emboss_Kernel = np.array([[0,-1,-1],[1,0,-1],[1,1,0]])
    Emboss_Effect_Img = cv2.filter2D(src=loaded_img, kernel=Emboss_Kernel, ddepth=-1)
    plt.figure(figsize=(8,8))
    plt.imshow(Emboss_Effect_Img,cmap="gray")
    plt.axis("off")
    plt.savefig(output_path)
    return render_template('Filters_Page.html',filename="output.png")


@app.route('/Sharpen')
def Sharpen():
    input_path = '/Users/u2021605/Desktop/Python Flask/static/images/img.jpg' # input image path
    output_path = "/Users/u2021605/Desktop/Python Flask/static/images/output.png"
    loaded_img = cv2.imread(input_path)
    loaded_img = cv2.cvtColor(loaded_img,cv2.COLOR_BGR2RGB)    
    Sharpen_Kernel = np.array([[-1, -1, -1], [-1, 9, -1], [-1, -1, -1]])
    Sharpen_Effect_Img = cv2.filter2D(src=loaded_img, kernel=Sharpen_Kernel, ddepth=-1)
    plt.figure(figsize=(8,8))
    plt.imshow(Sharpen_Effect_Img,cmap="gray")
    plt.axis("off")
    plt.savefig(output_path)
    return render_template('Filters_Page.html',filename="output.png")

@app.route('/Sepia')
def Sepia():
    input_path = '/Users/u2021605/Desktop/Python Flask/static/images/img.jpg' # input image path
    output_path = "/Users/u2021605/Desktop/Python Flask/static/images/output.png"
    loaded_img = cv2.imread(input_path)
    loaded_img = cv2.cvtColor(loaded_img,cv2.COLOR_BGR2RGB)    
    Sepia_Kernel = np.array([[0.272, 0.534, 0.131],[0.349, 0.686, 0.168],[0.393, 0.769, 0.189]])
    Sepia_Effect_Img = cv2.filter2D(src=loaded_img, kernel=Sepia_Kernel, ddepth=-1)
    plt.figure(figsize=(8,8))
    plt.imshow(Sepia_Effect_Img,cmap="gray")
    plt.axis("off")
    plt.savefig(output_path)
    return render_template('Filters_Page.html',filename="output.png")

@app.route('/Blur')
def Blur():
    input_path = '/Users/u2021605/Desktop/Python Flask/static/images/img.jpg' # input image path
    output_path = "/Users/u2021605/Desktop/Python Flask/static/images/output.png"
    loaded_img = cv2.imread(input_path)
    loaded_img = cv2.cvtColor(loaded_img,cv2.COLOR_BGR2RGB)    
    Blur_Effect_Img = cv2.GaussianBlur(loaded_img, (35, 35), 0)
    plt.figure(figsize=(8,8))
    plt.imshow(Blur_Effect_Img,cmap="gray")
    plt.axis("off")
    plt.savefig(output_path)
    return render_template('Filters_Page.html',filename="output.png")

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0')
