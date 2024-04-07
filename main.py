from az import Orbit, Cell, Wall

# from tests.data.ltl import ltl_orbit_mapper as orbit_mapper
# from tests.data.ltl import ltl_neighbours_mapper as mapper
from tests.data.mid import mid_neighbours_mapper as mapper
from tests.data.mid import mid_orbit_mapper as orbit_mapper

if __name__ == "__main__":
    # use one wall object for all cells to reduce memory usage
    wall = Wall()
    cell_pool: dict[int, Cell] = {}

    # initiate orbits and cells
    orbit_pool = {
        num: Orbit(num, cells, cell_pool) for num, cells in orbit_mapper.items()
    }
    for num, cells in orbit_mapper.items():
        orbit_pool.setdefault(num, Orbit(num, cells, cell_pool))
    # define cell neighbors
    for cell in cell_pool.values():
        for key in mapper[cell.number]:
            if mapper[cell.number][key] != "wall":
                cell.neighbours[key] = cell_pool[mapper[cell.number][key]]
            else:
                cell.neighbours[key] = wall

    # try to fill AZ
    while not all(orbit.filled for orbit in orbit_pool.values()):
        # Todo rework to center-periphery filling
        #  check all non-filled central orbits after any install in periphery orbit.
        #  Maybe it would works, but mostly priority - to start use MCTS because this algorithm mustn't work always
        for orbit in orbit_pool.values():
            if not orbit.filled:
                installed = orbit.install()
                if not installed:
                    print(f"Cannot install in the orbit {orbit.number}")
                else:
                    for elm in installed:
                        print(f"Installed in orbit: {orbit.number}, cell: {elm}")
