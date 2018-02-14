# Sample image maker

It is a Web tool to create sample images.

# Install

```
$ git clone https://github.com/yujikawa/sample_image_maker.git
$ cd sample_image_maker
$ pip install -r requirements.txt
```

# Usage
```
## Example
$ cd sample_image_maker
$ mkdir static/images/dog
$ cp ~/picture/dog.jpg static/images/dog/dog.jpg
$ python app.py
```

# API doc
|URI|method|Example|
|----|-----|-------|
|http://localhost/images/categories|GET||
|http://localhost/images/:category|GET|:category = dog|
|http://localhost/images/:category/:size|GET|:category = dog <br> :size=200x200|
