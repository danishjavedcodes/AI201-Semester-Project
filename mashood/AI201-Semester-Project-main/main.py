from flask import Flask, send_file, render_template, request, redirect

app = Flask(__name__)
# from rembg import remove
from PIL import Image
import base64
import io  
import os
from werkzeug.utils import secure_filename
import pathlib
def generate_custom_name(original_file_name):
    return "my_custom_file_name" + pathlib.Path(original_file_name).suffix



app.config["IMAGE_UPLOADS"] = "/Users/u2021605/Desktop/mashood/AI201-Semester-Project-main/static/Images"
app.config["ALLOWED_IMAGE_EXTENSIONS"] = ["PNG","JPG","JPEG"]

#apps


@app.route('/')
def home():
    return render_template('index.html')

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

@app.route('/upload_image_resizer', methods=['GET', "POST"])
def upload_image_resizer():
    if request.method == "POST":
        image = request.files['file']
        if image.filename == '':
            print("Image must have name")
            return redirect(request.url)

        filename = "img.jpg"
        
        basedir = os.path.abspath(os.path.dirname(__file__))
        image.save(os.path.join(basedir,app.config["IMAGE_UPLOADS"],filename))
        
        

        return render_template("resizer.html",filename=filename)
        
    return render_template('resizer.html')

@app.route('/bacgroundremover')

def bacgroundremover():
    print("cout")

    return render_template("resizer.html",filename="output.jpg")

@app.route('/resize_img',methods=['Get','POST'])
def resize_img():
    
    if request.method=='POST':
        Height=request.form['Height']
        Height = int(Height)
        Width=request.form['Width']
        Width = int(Width)
        input_path = '/Users/u2021605/Desktop/mashood/AI201-Semester-Project-main/static/Images/img.jpg'
        out_path = '/Users/u2021605/Desktop/mashood/AI201-Semester-Project-main/static/Images/output.png'
        image = Image.open(input_path)
        image.thumbnail((Height, Width))
        rgb_im = image.convert('RGB')
        rgb_im.save(out_path)
    return render_template("resizer.html",filename="output.png")
if __name__ == '__main__':
    app.run(debug=True)
