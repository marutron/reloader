from az import Orbit, Cell, Wall
from tests.data import ltl_orbit_mapper
from tests.data import ltl_neighbours_mapper as mapper


if __name__ == "__main__":
    # use one wall object for all cells to reduce memory usage
    wall = Wall()
    cell_pool: dict[int, Cell] = {}

    # initiate orbits and cells
    orbit_pool = {
        num: Orbit(num, cells, cell_pool) for num, cells in ltl_orbit_mapper.items()
    }
    for num, cells in ltl_orbit_mapper.items():
        orbit_pool.setdefault(num, Orbit(num, cells, cell_pool))
    # define cell neighbors
    for cell in cell_pool.values():
        for key in mapper[cell.number]:
            if mapper[cell.number][key] != "wall":
                cell.neighbours[key] = cell_pool[mapper[cell.number][key]]
            else:
                cell.neighbours[key] = wall

    # try to fill AZ
    for orbit in orbit_pool.values():
        installed = orbit.install()
        if not installed:
            print(f"Cannot install in the orbit {orbit.number}")
        else:
            print(f"Installed in orbit: {orbit.number}, cell: {installed}")
    pass
