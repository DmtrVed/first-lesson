class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f"Point({self.x}, {self.y})"
class Polygon:
    def __init__(self, points):
        if len(points) < 3:
            raise ValueError("Многоугольник должен иметь минимум 3 вершины")
        self._points = [Point(p.x, p.y) for p in points]

    @property
    def points(self):
        return [Point(p.x, p.y) for p in self._points]

    def perimeter(self):
        total = 0.0
        n = len(self._points)
        for i in range(n):
            a = self._points[i]
            b = self._points[(i + 1) % n]
            total += ((a.x - b.x) ** 2 + (a.y - b.y) ** 2) ** 0.5
        return total

    def area(self):
        s = 0.0
        n = len(self._points)
        for i in range(n):
            a = self._points[i]
            b = self._points[(i + 1) % n]
            s += a.x * b.y - b.x * a.y
        return abs(s) / 2

    def move(self, dx, dy):
        for p in self._points:
            p.x += dx
            p.y += dy

    def bounding_box(self):
        xs = [p.x for p in self._points]
        ys = [p.y for p in self._points]
        return (min(xs), min(ys), max(xs), max(ys))

    def is_convex(self):
        n = len(self._points)
        signs = []
        for i in range(n):
            a = self._points[i - 1]          # предыдущая
            b = self._points[i]              # текущая
            c = self._points[(i + 1) % n]    # следующая
            cross = (b.x - a.x) * (c.y - b.y) - (b.y - a.y) * (c.x - b.x)
            if cross > 0:
                signs.append(1)
            elif cross < 0:
                signs.append(-1)
        return len(set(signs)) <= 1

    def __len__(self):
        return len(self._points)

    def __lt__(self, other):
        return self.area() < other.area()

    def __repr__(self):
        return f"Polygon({self._points})"