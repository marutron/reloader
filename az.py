from typing import Optional


class Wall:
    filled: bool = True
    number: None
    neighbours: None
    orbit: None


class Cell:
    filled: bool
    number: int
    neighbours: dict[str, Optional["Cell"]]
    orbit: "Orbit"

    def __init__(self, number: int):
        self.filled = False
        self.number = number
        self.neighbours = {
            "ne": None,
            "e": None,
            "se": None,
            "sw": None,
            "w": None,
            "nw": None,
        }

    def __repr__(self):
        return str(self.__dict__)


class Orbit:
    number: int
    cells: dict[int, Cell]

    def __init__(self, number: int, cells: tuple):
        self.number = number
        self.cells = {}
        for cell_num in cells:
            self.cells.setdefault(cell_num, Cell(cell_num))

    def __repr__(self):
        return str(self.__dict__)

    def __hash__(self):
        return self.number

    def __eq__(self, other):
        return (
            True
            if isinstance(other, type(self)) and self.number == other.number
            else False
        )
