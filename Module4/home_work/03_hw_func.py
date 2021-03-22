# Даны координаты центров двух окружностей (x1; y1) (x2; y2) и и их радиусы  R1 и R2.
# Находится ли одна окружность целиком внутри другой

# TODO: your code here
def distance(x1, y1, x2, y2):
    return ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** (1/2)


def circle_in_circle(x1, y1, x2, y2, r1, r2):
    return distance(x1, y1, x2, y2) <= r1 - r2


_x1 = 0
_y1 = 0
_r1 = 3
_x2 = 0
_y2 = 3
_r2 = 1

print(circle_in_circle(_x1, _y1, _x2, _y2, _r1, _r2))
