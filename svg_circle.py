import math
from svg_rect import *

_C = 4.0 / 3.0 * (math.sqrt(2.0) - 1.0)


class CirclePoint:
    def __init__(self, x, y, r):
        self.x = x
        self.y = y
        self.r = r


class CurveCircle:
    def __init__(self, cp, angle=0):
        self.cp = cp
        self.angle = angle
        self.path = self.calc_curve()

    def rotate_curv_points(self, cp, points, angle):
        res = []
        for p in points:
            p1 = self.rotate_point(cp, p[0], p[1], angle)
            res.append(p1)
        return res

    @staticmethod
    def create_left_top_arc(cx, cy, r):
        result = []
        c = _C * r

        result.append((cx - r, cy - c))
        result.append((cx - c, cy - r))
        result.append((cx, cy - r))
        return result

    @staticmethod
    def create_right_top_arc(cx, cy, r):
        result = []
        c = _C * r

        result.append((cx + c, cy - r))
        result.append((cx + r, cy - c))
        result.append((cx + r, cy))
        return result

    @staticmethod
    def create_right_bottom_arc(cx, cy, r):
        result = []
        c = _C * r

        result.append((cx + r, cy + c))
        result.append((cx + c, cy + r))
        result.append((cx, cy + r))

        return result

    @staticmethod
    def create_left_bottom_arc(cx, cy, r):
        result = []
        c = _C * r

        result.append((cx - c, cy + r))
        result.append((cx - r, cy + c))
        result.append((cx - r, cy))

        return result

    def calc_curve(self):
        path = ""

        cx = self.cp.x
        cy = self.cp.y
        r = self.cp.r

        path += point((cx - r, cy))
        path += arc(CurveRect.calc_left_vert_line(cx - r, cy))

        path += arc(self.create_left_top_arc(cx, cy, r))
        path += arc(CurveRect.calc_top_horizontal_line(cx, cy - r, 0))

        path += arc(self.create_right_top_arc(cx, cy, r))
        path += arc(CurveRect.calc_right_vert_line(cx, cy, r, 0))

        path += arc(self.create_right_bottom_arc(cx, cy, r))
        path += arc(CurveRect.calc_bottom_horizontal_line(cx, cy, 0, r))

        path += arc(self.create_left_bottom_arc(cx, cy, r))

        return path

    def rotate_point(self, cp, px1, py1, angle):
        rad = math.radians(angle)
        x = cp.x + (px1 - cp.x) * math.cos(rad) - (py1 - cp.y) * math.sin(rad)
        y = cp.y + (px1 - cp.x) * math.sin(rad) + (py1 - cp.y) * math.cos(rad)
        return x, y

    def get_path(self):
        return self.path


if __name__ == '__main__':
    f = open("circle_in.json", "rb")
    buf = f.read()
    f.close()

    circle_obj = json.loads(buf)
    x = circle_obj["x"]
    y = circle_obj["y"]
    r = circle_obj["r"]
    circle = CirclePoint(x, y, r)
    curve = CurveCircle(circle)

    print curve.get_path()
