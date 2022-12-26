from flask import Flask, send_file, render_template, request, redirect
import cv2
import numpy as np
app = Flask(__name__)
from rembg import remove
from PIL import Image
import base64
import io  
import os
from werkzeug.utils import secure_filename
import pathlib
def generate_custom_name(original_file_name):
    return "my_custom_file_name" + pathlib.Path(original_file_name).suffix



app.config["IMAGE_UPLOADS"] = "/Users/Ifran/Desktop/AI/AI201-Semester-Project/static/Images/"
app.config["ALLOWED_IMAGE_EXTENSIONS"] = ["PNG","JPG","JPEG"]

#apps


@app.route('/')
def home():
    return render_template('index.html')

@app.route('/upload_image_collage', methods=['GET', "POST"])
def upload_image_collage():
    filename1 = ""
    if request.method == "POST":
        image1 = request.files['file1']
        image2 = request.files['file2']
        image3 = request.files['file3']
        image4 = request.files['file4']

        if image1.filename == '' or image2.filename == '' or image3.filename == '' or image4.filename == '':
            print("Image must have name")
            return redirect(request.url)

        filename1 = "img1.jpg"
        filename2 = "img2.jpg"
        filename3 = "img3.jpg"
        filename4 = "img4.jpg"

        basedir = os.path.abspath(os.path.dirname(__file__))
        image1.save(os.path.join(basedir,app.config["IMAGE_UPLOADS"],"img1.jpg"))
        image2.save(os.path.join(basedir,app.config["IMAGE_UPLOADS"],filename2))
        image3.save(os.path.join(basedir,app.config["IMAGE_UPLOADS"],filename3))
        image4.save(os.path.join(basedir,app.config["IMAGE_UPLOADS"],filename4))
        
    image1=cv2.imread("C:/Users/Ifran/Desktop/AI/AI201-Semester-Project/static/Images/img1.jpg")
    image2=cv2.imread("C:/Users/Ifran/Desktop/AI/AI201-Semester-Project/static/Images/img2.jpg")
    image3=cv2.imread("C:/Users/Ifran/Desktop/AI/AI201-Semester-Project/static/Images/img3.jpg")
    image4=cv2.imread("C:/Users/Ifran/Desktop/AI/AI201-Semester-Project/static/Images/img4.jpg")

    image1=cv2.resize(image1,(200,200))
    image2=cv2.resize(image2,(200,200))
    image3=cv2.resize(image3,(200,200))
    image4=cv2.resize(image4,(200,200))
    
    Horizontal1=np.hstack([image1,image2])
    Horizontal2=np.hstack([image3,image4])

    Vertical_attachment=np.vstack([Horizontal1,Horizontal2])

    cv2.imwrite("C:/Users/Ifran/Desktop/AI/AI201-Semester-Project/static/Images/img1.jpg",Vertical_attachment)

    return render_template('collage.html', filename = filename1)

@app.route('/background_page')
def background_page():
    return render_template('background_page.html')

@app.route('/upload_image', methods=['GET', "POST"])
def upload_image():
    if request.method == "POST":
        image = request.files['file']
        

        if image.filename == '':
            print("Image must have name")
            return redirect(request.url)

        filename = "img.jpg"
        
        basedir = os.path.abspath(os.path.dirname(__file__))
        image.save(os.path.join(basedir,app.config["IMAGE_UPLOADS"],filename))
        
        

        return render_template("background_page.html",filename=filename)
        
    return render_template('background_page.html')
        
@app.route('/bacgroundremover')

def bacgroundremover():
    input_path = '/Users/Ifran/Desktop/AI/AI201-Semester-Project/static/Images/img.jpg' # input image path
    output_path = "/Users/Ifran/Desktop/AI/AI201-Semester-Project/static/Images/output.png" # output image path
    input = Image.open(input_path) # load image
    output = remove(input) # remove background
    output.save(output_path) # save image
    return render_template("background_page.html",filename="output.png")

if __name__ == '__main__':
    app.run(debug=True)