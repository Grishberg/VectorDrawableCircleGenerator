import json
import svg_circle
from svg_methods import *


class RectParam:
    def __init__(self, x, y, w, h, r):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.r = r


class CurveRect:
    def __init__(self, rect):
        self.path = self.calc_curve(rect)

    def get_path(self):
        return self.path

    def calc_curve(self, cp):
        path = ""
        x = cp.x
        y = cp.y
        w = cp.w
        h = cp.h
        r = cp.r

        path += point((x, y + h - r))

        path += arc(self.calc_left_vert_line(x, y + r))

        path += arc(svg_circle.CurveCircle.create_left_top_arc(x + r, y + r, r))

        path += arc(self.calc_top_horizontal_line(x, y, w - r))

        path += arc(svg_circle.CurveCircle.create_right_top_arc(x + w - r, y + r, r))

        path += arc(self.calc_right_vert_line(x, y, w, h - r))

        path += arc(svg_circle.CurveCircle.create_right_bottom_arc(x + w - r, y + h - r, r))

        path += arc(self.calc_bottom_horizontal_line(x + r, y, w, h))

        path += arc(svg_circle.CurveCircle.create_left_bottom_arc(x + r, y + h - r, r))

        return path

    @staticmethod
    def calc_left_vert_line(x, y):
        return [(x, y), (x, y), (x, y)]

    @staticmethod
    def calc_right_vert_line(x, y, w, h):
        return [(x + w, y + h), (x + w, y + h), (x + w, y + h)]

    @staticmethod
    def calc_top_horizontal_line(x, y, w):
        return [(x + w, y), (x + w, y), (x + w, y)]

    @staticmethod
    def calc_bottom_horizontal_line(x, y, w, h):
        return [(x, y + h), (x, y + h), (x, y + h)]


if __name__ == '__main__':
    f = open("rect_in.json", "rb")
    buf = f.read()
    f.close()

    rect_obj = json.loads(buf)
    x = rect_obj["x"]
    y = rect_obj["y"]
    w = rect_obj["w"]
    h = rect_obj["h"]
    r = rect_obj["r"]
    rect = RectParam(x, y, w, h, r)
    curve = CurveRect(rect)

    print curve.get_path()
