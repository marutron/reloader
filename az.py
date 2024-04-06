class Wall:
    filled: bool = True
    number: None
    neighbours: None
    orbit: None

    def __init__(self):
        self.filled = True
        self.number = None
        self.neighbours = None
        self.orbit = None

    def __repr__(self):
        return str(self.__dict__)


class Cell:
    filled: bool
    number: int
    neighbours: dict[str, "Cell | Wall"]
    orbit: "Orbit"

    def __init__(self, number: int, orbit: "Orbit", cell_pool: dict):
        self.filled = False
        self.number = number
        self.neighbours = {}
        self.orbit = orbit
        cell_pool.setdefault(self.number, self)

    def __repr__(self):
        return f"number: {self.number}, orbit: {self.orbit}"


class Orbit:
    number: int
    cells: dict[int, Cell]

    def __init__(self, number: int, cells: tuple, cell_pool: dict):
        self.number = number
        self.cells = {}
        for cell_num in cells:
            self.cells.setdefault(cell_num, Cell(cell_num, self, cell_pool))

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
