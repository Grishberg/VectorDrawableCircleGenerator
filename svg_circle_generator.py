import json
import math

C = 4.0 / 3.0 * (math.sqrt(2.0) - 1.0)


class CirclePoint:
    def __init__(self, x, y, r):
        self.x = x
        self.y = y
        self.r = r


class CurveCircle:
    def __init__(self, cp):
        self.points = []
        for p in self.calc_curve1(cp):
            self.points.append(p)

        for p in self.calc_curve2(cp):
            self.points.append(p)

        for p in self.calc_curve3(cp):
            self.points.append(p)

        for p in self.calc_curve4(cp):
            self.points.append(p)

    def calc_curve1(self, cp):
        x0 = cp.x + cp.r
        y0 = cp.y

        x1 = cp.x + cp.r
        y1 = cp.y + C * cp.r

        x2 = cp.x + C * cp.r
        y2 = cp.y + cp.r

        x3 = cp.x
        y3 = cp.y + cp.r

        return (x0, y0), (x1, y1), (x2, y2), (x3, y3)

    def calc_curve2(self, cp):
        x0 = cp.x
        y0 = cp.y + cp.r

        x1 = cp.x + C * cp.r
        y1 = cp.y + cp.r

        x2 = cp.x + cp.r
        y2 = cp.y + C * cp.r

        x3 = cp.x + cp.r
        y3 = cp.y

        return (x0, y0), (x1, y1), (x2, y2), (x3, y3)

    def calc_curve3(self, cp):
        x0 = cp.x
        y0 = cp.y - cp.r

        x1 = cp.x - C * cp.r
        y1 = cp.y - cp.r

        x2 = cp.x - cp.r
        y2 = cp.y - C * cp.r

        x3 = cp.x - cp.r
        y3 = cp.y

        return (x0, y0), (x1, y1), (x2, y2), (x3, y3)

    def calc_curve4(self, cp):
        x0 = cp.x - cp.r
        y0 = cp.y

        x1 = cp.x - cp.r
        y1 = cp.y - C * cp.r

        x2 = cp.x - C * cp.r
        y2 = cp.y - cp.r

        x3 = cp.x
        y3 = cp.y - cp.r

        return (x0, y0), (x1, y1), (x2, y2), (x3, y3)


def rotate_point(cp, px1, py1, angle):
    rad = math.radians(angle)
    x = cp.x + (px1 - cp.x) * math.cos(rad) - (py1 - cp.y) * math.sin(rad)
    y = cp.y + (px1 - cp.x) * math.sin(rad) + (py1 - cp.y) * math.cos(rad)
    return x, y


def rotate_curv_points(cp, points, angle):
    res = []
    for p in points:
        p1 = rotate_point(cp, p[0], p[1], angle)
        res.append(p1)
    return res


def calc_circle_point(cp, angle):
    x = cp.x + cp.r * math.sin(math.radians(angle))
    y = cp.y + cp.r * math.cos(math.radians(angle))
    return x, y


f = open("in.json", "rb")
buf = f.read()
f.close()

circle_obj = json.loads(buf)
x = circle_obj["x"]
y = circle_obj["y"]
r = circle_obj["r"]
circle = CirclePoint(x, y, r)

x0, y0 = calc_circle_point(circle, 180)
x1, y1 = calc_circle_point(circle, 180 - 30)
x2, y2 = calc_circle_point(circle, 90 + 30)
x3, y3 = calc_circle_point(circle, 90)

print x1, y1
print x2, y2

points = calc_curve1(circle)
rotated_curv = rotate_curv_points(circle, points, 180)
print rotated_curv
