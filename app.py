import os
from io import BytesIO
from flask import Flask, jsonify, render_template, helpers
from PIL import Image

app = Flask(__name__)


@app.route("/images/<string:category>/<string:width_height>", methods=['GET'])
def maker(category, width_height):
    # requests
    (width, height) = width_height.split("x")
    buf = make_image(category, width, height)
    response = helpers.make_response(buf.getvalue())
    response.headers["Content-type"] = "Image"
    return response


@app.route("/images/categories", methods=['GET'])
def category():
    result = ['human', 'view']
    return jsonify(categories=result)


def make_image(category, width, height):

    original_image_file_name = "{}.jpg".format(category)
    original_image_file_path = os.path.join("static", category, original_image_file_name)
    if not os.path.isfile(original_image_file_path):
        return None

    img = Image.open(original_image_file_path)
    #img.thumbnail((int(width), int(height)))
    img = img.resize((int(width), int(height)))
    buf = BytesIO()
    img.save(buf, 'png')
    img.close()

    return buf


if __name__ == "__main__":
    app.run(debug=True)