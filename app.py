from flask import Flask, send_file, render_template, request, redirect

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



app.config["IMAGE_UPLOADS"] = "/Users/Danish Javed/Desktop/Flask/static/Images"
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
        
@app.route('/bacgroundremover')

def bacgroundremover():
    input_path = '/Users/Danish Javed/Desktop/Flask/static/Images/img.jpg' # input image path
    output_path = "/Users/Danish Javed/Desktop/Flask/static/Images/output.png" # output image path
    input = Image.open(input_path) # load image
    output = remove(input) # remove background
    output.save(output_path) # save image
    return render_template("background_page.html",filename="output.png")

if __name__ == '__app__':
    app.run(debug=True,host='0.0.0.0')
 



