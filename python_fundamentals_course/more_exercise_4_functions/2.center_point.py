from math import floor

def center_point(x1, y1, x2, y2):
    closest_1 = abs(x1) + abs(y1)
    closest_2 = abs(x2) + abs(y2)
    if closest_1 == closest_2:
        return f"({floor(x1)}, {floor(y1)})"
    if closest_1 > closest_2:
        return f"({floor(x2)}, {floor(y2)})"
    if closest_1 < closest_2:
        return f"({floor(x1)}, {floor(y1)})"


x1 = float(input())
y1 = float(input())
x2 = float(input())
y2 = float(input())
print(center_point(x1, y1, x2, y2))