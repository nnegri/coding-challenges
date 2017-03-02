
def find_illuminated_column(lamps, n, illuminated):
    for lamp in lamps:
        x = lamp[0]
        y = lamp[1]
        while y < n:
            illuminated.append((x, y))
            y += 1

    for lamp in lamps:
        x = lamp[0]
        y = lamp[1]
        while y >= 0:
            illuminated.append((x, y))
            y -= 1

    return illuminated

def find_illuminated_row(lamps, n, illuminated):
    for lamp in lamps:
        x = lamp[0]
        y = lamp[1]
        while x < n:
            illuminated.append((x, y))
            x += 1

    for lamp in lamps:
        x = lamp[0]
        y = lamp[1]
        while x >= 0:
            illuminated.append((x, y))
            x -= 1

    return illuminated

def find_illuminated_diag(lamps, n, illuminated):
    # northeast
    for lamp in lamps:
        x = lamp[0]
        y = lamp[1]
        while x < n and y < n:
            illuminated.append((x, y))
            x += 1
            y += 1

    # southwest
    for lamp in lamps:
        x = lamp[0]
        y = lamp[1]
        while x >= 0 and y >= 0:
            illuminated.append((x, y))
            x -= 1
            y -= 1

    # northwest
    for lamp in lamps:
        x = lamp[0]
        y = lamp[1]
        while x >= 0 and y < n:
            illuminated.append((x, y))
            x -= 1
            y += 1

    # southeast
    for lamp in lamps:
        x = lamp[0]
        y = lamp[1]
        while x < n and y >= 0:
            illuminated.append((x, y))
            x += 1
            y -= 1

    return illuminated

def find_illuminated(lamps, n):

    illuminated = []

    #for each point, add all points in column north to illuminated
    #for each point, add all points in column south to illuminated
    illuminated = find_illuminated_column(lamps, n, illuminated)

    #for each point, add all points in row east to illuminated
    #for each point, add all points in row west illuminated
    illuminated = find_illuminated_row(lamps, n, illuminated)

    #for each point, add all points diagonally sw # ne to illuminated
    #for each point, add all points diagonally nw # se to illuminated
    illuminated = find_illuminated_diag(lamps, n, illuminated)

    return set(illuminated) #makes lookup faster, but conversion is still O(n)


def find_if_point_illumninated(illuminated, point):

    if point in illuminated:
        return True

    return False

def grid_illumination(lamps, n, point):

    illuminated = find_illuminated(lamps, n)

    return find_if_point_illumninated(illuminated, point)


print grid_illumination([(0,2)], 3, (1,0))



