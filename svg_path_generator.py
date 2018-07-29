from svg_circle import *
from svg_rect import *


def process_rect(shape):
    name = shape["name"]
    x = shape["x"]
    y = shape["y"]
    w = shape["w"]
    h = shape["h"]
    r = shape["r"]
    rect_param = RectParam(x, y, w, h, r)
    path = CurveRect(rect_param).get_path()

    return '<string name="' + name + '">' + path + '</string>'


def process_circle(shape):
    name = shape["name"]
    x = shape["x"]
    y = shape["y"]
    r = shape["r"]
    circle_param = CirclePoint(x, y, r)
    path = CurveCircle(circle_param).get_path()
    return '<string name="' + name + '">' + path + '</string>'


if __name__ == '__main__':
    f = open("in.json", "rb")
    buf = f.read()
    f.close()

    obj = json.loads(buf)
    shapes = obj["shapes"]
    for shape in shapes:

        shape_type = shape["type"]
        res = ""
        if shape_type == 'rect':
            res = process_rect(shape)
        elif shape_type == 'circle':
            res = process_circle(shape)
        print res
