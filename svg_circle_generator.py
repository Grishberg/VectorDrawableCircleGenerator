import json
import math

_C = 4.0 / 3.0 * (math.sqrt(2.0) - 1.0)


class CirclePoint:
    def __init__(self, x, y, r):
        self.x = x
        self.y = y
        self.r = r


class CurveCircle:
    def __init__(self, cp, angle=0):
        self.points = self.calc_curve(cp)
        if angle <> 0:
            self.points = self.rotate_curv_points(cp, self.points, angle)

    def rotate_curv_points(self, cp, points, angle):
        res = []
        for p in points:
            p1 = self.rotate_point(cp, p[0], p[1], angle)
            res.append(p1)
        return res

    def calc_curve(self, cp):
        result = []
        cx = cp.x
        cy = cp.y
        r = cp.r
        c = _C * r

        result.append((cx - r, cy))
        result.append((cx - r, cy - c))
        result.append((cx - c, cy - r))
        result.append((cx, cy - r))
        result.append((cx + c, cy - r))
        result.append((cx + r, cy - c))
        result.append((cx + r, cy))
        result.append((cx + r, cy + c))
        result.append((cx + c, cy + r))
        result.append((cx, cy + r))
        result.append((cx - c, cy + r))
        result.append((cx - r, cy + c))
        result.append((cx - r, cy))

        return result

    def rotate_point(self, cp, px1, py1, angle):
        rad = math.radians(angle)
        x = cp.x + (px1 - cp.x) * math.cos(rad) - (py1 - cp.y) * math.sin(rad)
        y = cp.y + (px1 - cp.x) * math.sin(rad) + (py1 - cp.y) * math.cos(rad)
        return x, y

f = open("in.json", "rb")
buf = f.read()
f.close()

circle_obj = json.loads(buf)
x = circle_obj["x"]
y = circle_obj["y"]
r = circle_obj["r"]
circle = CirclePoint(x, y, r)
curve = CurveCircle(circle)

print curve.points
