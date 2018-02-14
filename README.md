# Sample image maker

It is a Web tool to create sample images.
![result](https://camo.qiitausercontent.com/4ddf521d4818e2b737316ce1d14af833d2ec484d/68747470733a2f2f71696974612d696d6167652d73746f72652e73332e616d617a6f6e6177732e636f6d2f302f3139393434352f30613133623237612d613165622d346165342d346563612d3864353739643665643861362e676966)

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
