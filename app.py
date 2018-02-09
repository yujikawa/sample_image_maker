import os
from flask import Flask, jsonify, render_template
from PIL import Image

app = Flask(__name__)


@app.route("/images/<string:category>/<string:width_height>", methods=['GET'])
def maker(category, width_height):
    # requests
    (width, height) = width_height.split("x")
    img_file = make_image(category, width, height)

    return render_template('index.html', image_file=img_file)


@app.route("/images/categories", methods=['GET'])
def category():
    result = ['human', 'view']
    return jsonify(categories=result)


def make_image(category, width, height):

    original_image_file_name = "{}.jpg".format(category)
    original_image_file_path = os.path.join("static", category, original_image_file_name)
    if not os.path.isfile(original_image_file_path):
        return None

    resize_image_file_name = "{}_{}-{}.jpg".format(category, width, height)
    resize_image_file_path = os.path.join("static", category, resize_image_file_name)

    if os.path.isfile(resize_image_file_path):
        return os.path.join(category, resize_image_file_name)

    img = Image.open(original_image_file_path)
    img_resize = img.resize((int(width), int(height)))
    img_resize.save(resize_image_file_path)
    return os.path.join(category, resize_image_file_name)


if __name__ == "__main__":
    app.run(debug=True)