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

    def ready(self) -> bool:
        """Is the cell ready for fuel assembly installation?"""
        mapper = {
            1: not any(nbr.filled for nbr in self.neighbours.values()),
            2: (
                all([self.neighbours["se"].filled, self.neighbours["nw"].filled])
                and not all(
                    [
                        self.neighbours["ne"].filled,
                        self.neighbours["e"].filled,
                        self.neighbours["sw"].filled,
                        self.neighbours["w"].filled,
                    ]
                )
            )
            or (
                all([self.neighbours["e"].filled, self.neighbours["w"].filled])
                and not all(
                    [
                        self.neighbours["nw"].filled,
                        self.neighbours["ne"].filled,
                        self.neighbours["se"].filled,
                        self.neighbours["sw"].filled,
                    ]
                )
            )
            or (
                all([self.neighbours["sw"].filled, self.neighbours["ne"].filled])
                and not all(
                    [
                        self.neighbours["e"].filled,
                        self.neighbours["se"].filled,
                        self.neighbours["w"].filled,
                        self.neighbours["nw"].filled,
                    ]
                )
            ),
            3: (
                all(
                    [
                        self.neighbours["nw"].filled,
                        self.neighbours["e"].filled,
                        self.neighbours["sw"].filled,
                    ]
                )
                and not all(
                    [
                        self.neighbours["ne"].filled,
                        self.neighbours["se"].filled,
                        self.neighbours["w"].filled,
                    ]
                )
            )
            or (
                all(
                    [
                        self.neighbours["ne"].filled,
                        self.neighbours["se"].filled,
                        self.neighbours["w"].filled,
                    ]
                )
                and not all(
                    [
                        self.neighbours["nw"].filled,
                        self.neighbours["e"].filled,
                        self.neighbours["sw"].filled,
                    ]
                )
            ),
            4: all(
                [
                    self.neighbours["se"].filled,
                    self.neighbours["sw"].filled,
                    self.neighbours["nw"].filled,
                    self.neighbours["ne"].filled,
                ]
            )
            and not all([self.neighbours["w"].filled, self.neighbours["e"].filled]),
            5: (
                all(
                    [
                        self.neighbours["ne"].filled,
                        self.neighbours["w"].filled,
                        self.neighbours["sw"].filled,
                        self.neighbours["se"].filled,
                    ]
                )
                and not all([self.neighbours["nw"].filled, self.neighbours["e"].filled])
            )
            or (
                all(
                    [
                        self.neighbours["e"].filled,
                        self.neighbours["nw"].filled,
                        self.neighbours["w"].filled,
                        self.neighbours["sw"].filled,
                    ]
                )
                and not all(
                    [self.neighbours["ne"].filled, self.neighbours["se"].filled]
                )
            )
            or (
                all(
                    [
                        self.neighbours["se"].filled,
                        self.neighbours["ne"].filled,
                        self.neighbours["nw"].filled,
                        self.neighbours["w"].filled,
                    ]
                )
                and not all([self.neighbours["e"].filled, self.neighbours["sw"].filled])
            )
            or (
                all(
                    [
                        self.neighbours["sw"].filled,
                        self.neighbours["e"].filled,
                        self.neighbours["ne"].filled,
                        self.neighbours["nw"].filled,
                    ]
                )
                and not all([self.neighbours["w"].filled, self.neighbours["se"].filled])
            )
            or (
                all(
                    [
                        self.neighbours["w"].filled,
                        self.neighbours["se"].filled,
                        self.neighbours["e"].filled,
                        self.neighbours["ne"].filled,
                    ]
                )
                and not all(
                    [self.neighbours["nw"].filled, self.neighbours["sw"].filled]
                )
            )
            or (
                all(
                    [
                        self.neighbours["nw"].filled,
                        self.neighbours["sw"].filled,
                        self.neighbours["se"].filled,
                        self.neighbours["e"].filled,
                    ]
                )
                and not all([self.neighbours["w"].filled, self.neighbours["ne"].filled])
            ),
            6: all(nbr.filled for nbr in self.neighbours.values()),
        }

        # Fixme расширить АЗ
        if not self.filled and any(mapper[key] for key in mapper.keys()):
            return True
        else:
            return False


class Orbit:
    number: int
    cells: dict[int, Cell]

    def __init__(self, number: int, cells: tuple[int], cell_pool: dict):
        self.number = number
        self.cells = {cell_num: Cell(cell_num, self, cell_pool) for cell_num in cells}

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

    def install(self) -> int | None:
        """Install fuel assembly in orbit"""
        ready = []
        for cell in self.cells.values():
            if cell.ready():
                ready.append(cell)
                if ready:
                    # Todo use MCTS for filling
                    ready[0].filled = True
                    return ready[0].number
        return None
