from typing import List

def get_average_elevation(m: List[List[int]]) -> float:
    """
    Returns the average elevation across the elevation map m.

    Examples
    >>> get_average_elevation([])
    0.0
    >>> m = [[1,2,3],[4,5,6],[7,8,9]]
    >>> get_average_elevation(m)
    5.0
    >>> m = [[1,2,2,5],[4,5,4,8],[7,9,9,1],[1,2,1,4]]
    >>> get_average_elevation(m)
    4.0625
    """
    leng_list = 0.0
    total = 0.0
    new_total = 0.0
    for l in m:
        for i in l:
            total += i
        if len(l) == 0.0:
            new_total = 0.0
        else:
            leng_list += len(l)
            new_total = total/leng_list
        
    return new_total
    

def find_peak(m: List[List[int]]) -> List[int]:
    """
    Given an non-empty elevation map m, returns the cell of the
    highest point in m.

    Examples (note some spacing has been added for human readablity)
    >>> m = [[1,2,3],
             [9,8,7],
             [5,4,6]]
    >>> find_peak(m)
    [1,0]
    >>> m = [[6,2,3],
             [1,8,7],
             [5,4,9]]
    >>> find_peak(m)
    [2,2]
    """
    lst = [0,0]
    l = []
    for j in range(len(m)):
        for k in range(len(m[j])):
            i = 0
            while i < len(m):
                l.append(max(m[i]))
                highest = max(l)
                i += 1
            if highest == m[j][k]:
                lst[0] = j
                lst[1] = k

    return lst
    

def is_sink(m: List[List[int]], c: List[int]) -> bool:
    """
    Returns True if and only if c is a sink in m.

    Examples (note some spacing has been added for human readablity)
    >>> m = [[1,2,3],
             [2,3,3],
             [5,4,3]]
    >>> is_sink(m, [0,0])
    True
    >>> is_sink(m, [2,2])
    True
    >>> is_sink(m, [3,0])
    False
    >>> m = [[1,2,3],
             [2,1,3],
             [5,4,3]]
    >>> is_sink(m, [1,1])
    True
    >>> is_sink(m, [0,1])
    False
    """
    if (0 <= c[0] < len(m) and 0 <= c[1] < len(m)):
        for i in range(-1, 2):
            for j in range(-1, 2):
                if not (i == 0 and j == 0):
                    if (0 <= c[0] + i < len(m) and 0 <= c[1] + j < len(m)):
                        if m[c[0] + i][c[1] + j] < m[c[0]][c[1]]:
                            return False
        return True
            
    return False
    

def find_local_sink(m: List[List[int]], start: List[int]) -> List[int]:
    """
    Given a non-empty elevation map, m, starting at start,
    will return a local sink in m by following the path of lowest
    adjacent elevation.

    Examples (note some spacing has been added for human readablity)
    >>> m = [[ 5,70,71,80],
             [50, 4,30,90],
             [60, 3,35,95],
             [10,72, 2, 1]]
    >>> find_local_sink(m, [0,0])
    [3,3]
    >>> m = [[ 5,70,71,80],
             [50, 4, 5,90],
             [60, 3,35, 2],
             [ 1,72, 6, 3]]
    >>> find_local_sink(m, [0,3])
    [2,3]
    >>> m = [[9,2,3],
             [6,1,7],
             [5,4,8]]
    >>> find_local_sink(m, [1,1])
    [1,1]
    """
    c = start
    while is_sink(m, c) == False:
        c = lowest_sink(m, c)
    return c
    
def can_hike_to(m: List[List[int]], s: List[int], d: List[int], supplies: int) -> bool:
    """
    Given an elevation map m, a start cell s, a destination cell d, and
    the an amount of supplies returns True if and only if a hiker could reach
    d from s using the strategy dscribed in the assignment .pdf. Read the .pdf
    carefully. Assume d is always south, east, or south-east of s. The hiker
    never travels, north, west, nor backtracks. 

    Examples (note some spacing has been added for human readablity)
    >>> m = [[1,4,3],
             [2,3,5],
             [5,4,3]]
    >>> can_hike_to(m, [0,0], [2,2], 4)
    True
    >>> can_hike_to(m, [0,0], [0,0], 0)
    True
    >>> can_hike_to(m, [0,0], [2,2], 3)
    False
    >>> m = [[1,  1,100],
             [1,100,100],
             [1,  1,  1]]
    >>> can_hike_to(m, [0,0], [2,2], 4)
    False
    >>> can_hike_to(m, [0,0], [2,2], 202)
    True
    >>> can_hike_to(m, [0,1], [2,2], 200)
    True
    >>> can_hike_to(m, [0,1], [2,2], 1)
    False
    >>> can_hike_to(m, [0,1], [2,1], 200)
    True
    >>> can_hike_to(m, [0,1], [0,2], 1)
    False
    """
    while s != d:
        if supplies >= 0:
            #Goes east since s[0] in same row as d[0]
            if (s[0] == d[0] and 0 <= s[1] + 1 < len(m)):
                supplies -= abs((m[s[0]][s[1] + 1] - m[s[0]][s[1]]))
                s[1] = s[1] + 1
            #Goes south since s[1] in same row as d[1]
            elif (s[1] == d[1] and 0 <= s[0] + 1 < len(m)):
                supplies -= abs((m[s[0] + 1][s[1]] - m[s[0]][s[1]]))
                s[0] = s[0] + 1
            elif (0 <= s[0] + 1 < len(m) and 0 <= s[1] + 1 < len(m)):
                #Goes east when south < east or east = south
                if (m[s[0] + 1][s[1]] >= m[s[0]][s[1] + 1]):
                    supplies -= abs((m[s[0]][s[1] + 1] - m[s[0]][s[1]]))
                    s[1] = s[1] + 1
                #Goes south when south < east
                else:
                    supplies -= abs((m[s[0] + 1][s[1]] - m[s[0]][s[1]]))
                    s[0] = s[0] + 1
            #Goes south when cannot go east anymore
            elif not (0 <= s[1] + 1 < len(m)):
                supplies -= abs((m[s[0] + 1][s[1]] - m[s[0]][s[1]]))
                s[0] = s[0] + 1
            #Goes east when cannot go to south anymore
            elif not (0 <= s[0] + 1 < len(m)):
                supplies -= abs((m[s[0]][s[1] + 1] - m[s[0]][s[1]]))
                s[1] = s[1] + 1
        else:
            return False
    return (s == d and supplies >= 0)


def rotate_map(m: List[List[int]]) -> None:
    """
    Rotates the orientation of an elevation map m 90 degrees counter-clockwise.
    See the examples to understand what's meant by rotate.

    Examples (note some spacing has been added for human readablity)
    >>> m = [[1,2,3],
             [2,3,3],
             [5,4,3]]
    >>> rotate_map(m)
    >>> m
    [[3,3,3],
     [2,3,4],
     [1,2,5]]
    >>> m = [[5,9,1,8],
             [2,4,5,7],
             [6,3,3,2],
             [1,7,6,3]]
    >>> rotate_map(m)
    >>> m
    [[8,7,2,3],
     [1,5,3,6],
     [9,4,3,7],
     [5,2,6,1]]
    """
    rows = len(m)
    
    cols = len(m[0])
    rotate = []
    for col in range(cols):
        rotate_row = []
        for row in range(rows):
            rotate_row.append(m[row][col])

        rotate.append(rotate_row)
    m.clear()
    m.extend(rotate[::-1])

def lowest_sink(m: List[List[int]], start: List[int]) -> List[int]:
    #Finds the lowest sink in the main and adjacent cells. Designed
    #for find_local_sink
    
    """
    """
    
    c = start
    lst = []
    if is_sink(m, c) == False:
        for i in range(-1, 2):
            for j in range(-1, 2):
                if not (i == 0 and j == 0):
                    if (0 <= c[0] + i < len(m) and 0 <= c[1] + j < len(m)):
                        lst.append(m[c[0] + i][c[1] + j])
        new = min(lst)
        for k in range(len(m)):
            for l in range(len(m[k])):
                if new == m[k][l]:
                    c[0] = k
                    c[1] = l
    return c

"""
You are not required to understand or use the code below. It is there for
curiosity and testing purposes.
"""
def create_real_map()-> List[List[int]]:
    """
    Creates and returns an elevation map from the real world data found
    in the file elevation_data.csv.

    Make sure this .py file and elevation_data.csv are in the same directory
    when you run this function to ensure it works properly.
    """
    data = open("elevation_data.csv")
    m = []
    for line in data:
        m.append(line.split(","))
    data.close()
    for i in range(len(m)):
        for j in range(len(m[i])):
            m[i][j] = int(m[i][j])
    return m
    









    
