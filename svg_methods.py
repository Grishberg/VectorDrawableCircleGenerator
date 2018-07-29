def p2s(p):
    x = p[0]
    y = p[1]
    return '%.3f' % round(x, 3) + "," '%.3f' % round(y, 3)


def point(p):
    return " M " + p2s(p)


def arc(p):
    return " C " + p2s(p[0]) + " " + p2s(p[1]) + " " + p2s(p[2])
