import os
from io import BytesIO
from flask import Flask, jsonify, helpers
from PIL import Image, ImageDraw, ImageFont

app = Flask(__name__)

STATIC_IMAGE_PATH = "static/images"


@app.route("/images/<string:category>/<string:width_height>", methods=['GET'])
def maker_resize(category, width_height):
    """
    Make Sample Image
    :param category:
    :param width_height:
    :return: Content-type=Image
    """
    try:
        (width, height) = width_height.split("x")
        buf = _make_resize_image(category, width, height)
        return _make_response(buf)
    except Exception as e:
        buf = _make_no_image()
        return _make_response(buf)



@app.route("/images/<string:category>", methods=['GET'])
def maker_original(category):
    """
    Make Sample Image
    :param category:
    :return: Content-type=Image
    """
    try:
        buf = _make_original_image(category)
        return _make_response(buf)
    except Exception as e:
        buf = _make_no_image()
        return _make_response(buf)



@app.route("/images/categories", methods=['GET'])
def category():
    """
    Get Image Categories
    :return: categories list
    """
    result = os.listdir(STATIC_IMAGE_PATH)
    return jsonify(categories=result)


# functions

def _make_resize_image(category, width, height):
    """
    Make Sample Image(byte)
    :param category:
    :param width:
    :param height:
    :return: Image(byte)
    """
    width = int(width)
    height = int(height)

    original_image_file_name, original_image_file_path = _get_original_file(category)

    if not os.path.isfile(original_image_file_path):
        return None

    img = Image.open(original_image_file_path)
    # resize
    img = img.resize((width, height))
    img, buf = _make_image_buffer(img)
    img.close()

    return buf


def _make_original_image(category):
    """
    Make original image
    :param category:
    :return:
    """

    original_image_file_name, original_image_file_path = _get_original_file(category)

    if not os.path.isfile(original_image_file_path):
        return None
    img = Image.open(original_image_file_path)
    img, buf = _make_image_buffer(img)
    img.close()

    return buf


def _make_image_buffer(img, text="SAMPLE"):
    """
    Make image buffer
    :param img: PIL
    :return: img, buf
    """
    draw = ImageDraw.Draw(img)
    font = ImageFont.truetype("font/Lovelo Black.otf", 30)
    draw.text((0, 0), text, font=font, fill=(255, 255, 255, 100))
    buf = BytesIO()
    img.save(buf, 'jpeg')
    return img, buf


def _make_response(buf):
    """
    Make response
    :param buf:
    :return: response
    """
    response = helpers.make_response(buf.getvalue())
    response.headers["Content-type"] = "Image"
    return response


def _get_original_file(category):
    """
    Get original file
    :param category:
    :return: original_image_file_name, original_image_file_path
    """
    original_image_file_name = "{}.jpg".format(category)
    original_image_file_path = os.path.join(STATIC_IMAGE_PATH, category, original_image_file_name)
    return original_image_file_name, original_image_file_path


def _make_no_image():
    """
    Make no image
    :return: buf
    """
    img = Image.new("RGB", (512, 512), (128, 128, 128))
    img, buf = _make_image_buffer(img, "NO IMAGE")
    return buf


if __name__ == "__main__":
    app.run(debug=True)