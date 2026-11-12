def angular_distance(longitude_1, longitude_2):
    difference = abs(longitude_1 - longitude_2)
    min_angular_distance = min(360 - difference, difference)
    return min_angular_distance