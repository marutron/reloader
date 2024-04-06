from az import Orbit
from test.data import ltl_orbit_mapper

if __name__ == "__main__":
    orbit_pool: dict[int, Orbit] = {}
    for num, cells in ltl_orbit_mapper.items():
        orbit_pool.setdefault(num, Orbit(num, cells))
    pass
