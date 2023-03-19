from flask import Flask, request, render_template
import os
from PIL import Image
import imagehash
import ahashForApp

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def upload_form():
    return render_template("index.html")

files_list = os.listdir("./static")

@app.route("/form", methods=['POST', 'GET'])
def nextPage():
    if request.method=="POST":
        img = request.form.get("testImage")
        print(img)
        similar = ahashForApp.ahashing(img)

        imglist = []
        for i in range(len(similar)):
            idx = similar[i]
            imglist.append(files_list[idx])
            print(imglist)

        return render_template('result.html', imglist = imglist)

    # # Render the HTML form if no input image is provided
    # return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)