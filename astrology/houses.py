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



def get_planet_position_in_house(houses, longitudes):

    planets_in_houses = {}

    for i in range (0, 12):
        house_number = i + 1
        end = houses[(i + 1) % 12]
        start = houses[i]

        for name, longitude in longitudes.items():

            in_house = False

            if start < end:
                if start <= longitude < end:
                    in_house = True

            if start > end:
                if start <= longitude < 360 or 0 <= longitude < end:
                    in_house = True
                    
            if in_house:
                planets_in_houses[name] = house_number

    return planets_in_houses


def get_houses_longitudes(ascendant, ic, descendant, mc, choice=None):

    houses_longitudes = None

    if choice == "1":
        print("PLACIDUS : en construction")
        
    elif choice == "2":
        houses_longitudes = get_equal_houses(ascendant)

    elif choice == "3":
        houses_longitudes = get_porphyre_houses(ascendant, ic, descendant, mc)

    elif choice == "4":
        print("SIGNES ENTIERS : en construction")

    return houses_longitudes


