from typing import Optional


class Cell:
    number: int
    neighbours: dict[str, Optional["Cell" | str]]
    orbit: "Orbit"

    def __init__(self, number: int):
        self.number = number
        self.neighbours = {
            "ne": None,
            "e": None,
            "se": None,
            "sw": None,
            "w": None,
            "nw": None,
        }


class Orbit:
    number: int
    cells: dict[int, Cell]

    def __init__(self, number: int, mapper: dict):
        self.number = number
        for cell_num in mapper[number]:
            self.cells.setdefault(cell_num, Cell(cell_num))

    def __hash__(self):
        return self.number

    def __eq__(self, other):
        return (
            True
            if isinstance(other, type(self)) and self.number == other.number
            else False
        )
