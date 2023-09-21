import math

orbits = [(1, 3), (2.5, 10), (7, 2), (6, 6), (4, 3)]


def find_farthest_orbit(list_of_orbits):
    areas = list()

    for orbit in list_of_orbits:
        if orbit[0] == orbit[1]:
            areas.append(0)
        else:
            areas.append(math.pi * orbit[0] * orbit[1])

    return list_of_orbits[areas.index(max(areas))]


print(*find_farthest_orbit(orbits))
