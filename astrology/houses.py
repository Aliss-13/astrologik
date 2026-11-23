def get_equal_houses(ascendant):

    houses = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

    houses_longitudes = []
    for house_number in houses:
        house_longitude = (ascendant + (house_number-1)*30) % 360
        houses_longitudes.append(house_longitude)

    return houses_longitudes


def get_porphyre_houses(ascendant, ic, descendant, mc):

    quadrants = [
    (ascendant, ic),
    (ic, descendant),
    (descendant, mc),
    (mc, ascendant)
    ]

    houses_longitudes_porphyre = []

    for start, end in quadrants:
        arc = (end - start) % 360
        step = arc / 3
            
        for i in range(0, 3):
            longitude = (start + i*step) %360
            houses_longitudes_porphyre.append(longitude)

    return houses_longitudes_porphyre