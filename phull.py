from __future__ import annotations

class Point:

    def __init__(self, x: float, y: float):
        self._x = x
        self._y = y

    def __str__(self) -> str:
        return "(" + str(self._x) + "," + str(self._y) + ")"

    def __repr__(self) -> str:
        return self.__str__()

    def leftof(self, X: Point) -> bool:
        return self._x < X._x

    def rightof(self, X: Point) -> bool:
        return not self.leftof(X)

    def below(self, X: Point) -> bool:
        return self._y < X._y

    def above(self, X: Point) -> bool:
        return not self.below(X)
    @staticmethod
    def is_upper_triangle(A: Point, B: Point, C:Point) -> bool:
        assert A.leftof(B) and B.leftof(C)
        abslope = (B._y - A._y)/(B._x - A._x)
        acslope = (C._y - A._y)/(C._x - A._x)
        return abslope > acslope
    @staticmethod
    def is_lower_triangle(A: Point, B: Point, C: Point) -> bool:
        assert A.leftof(B) and B.leftof(C)
        return not Point.is_upper_triangle(A,B,C)

def convex_hull(S):
    S.sort(key=lambda Q: Q._x)
    upperhull = []
    lowerhull = []
    for P in S:
        upperhull.append(P)
        lowerhull.append(P)

        while len(upperhull) >= 3 and not Point.is_upper_triangle(upperhull[-3], upperhull[-2], upperhull[-1]):
            del upperhull[-2]
        while len(lowerhull) >= 3 and not Point.is_lower_triangle(lowerhull[-3], lowerhull[-2], lowerhull[-1]):
            del lowerhull[-2]
    upperhull.reverse()
    del upperhull[0]
    return lowerhull + upperhull