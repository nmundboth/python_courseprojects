import math
g = 9.81
pi = math.pi

def get_distance(velocity:float, angle:float)-> float:
    """
    Calculates the distance a projectile travels on a flat surface
    given its intial velocity, as well as the angle of fire relative
    to the x-axis. The angle is given in radian. This function assumes
    perfect physics, i.e., constant gravity, no air resistance, etc.

    >>> get_distance(0, 1)
    0.0
    >>> get_distance(1, 0)
    0.0
    >>> get_distance(10, 0.25*pi)
    10.19367991845056
    """
    angle_doubled = 2*angle
    distance_with_gravity = ((velocity)**2)*(math.sin(angle_doubled))
    distance = distance_with_gravity/g
    return distance

def degrees_to_radians(d:float)-> float:
    """
    Takes in an angle in degrees, d, and returns an equivalent
    angle in radians

    >>> degrees_to_radians(0)
    0.0
    >>> degrees_to_radians(180)
    3.141592653589793
    """
    angle_in_radians = (d*pi)/180
    return angle_in_radians

def get_radian_of(angle_string: str)-> float:
    """
    Takes in a valid input angle_str and returns the numerical value of the
    angle in radians.

    Examples:
    >>> get_radian_of("1.2r")
    1.2
    >>> get_radian_of("45d")
    0.7853981633974483
    """
    if angle_string[-1] == "d" or angle_string[-1] == "D":
        return degrees_to_radians(float(angle_string[:-1]))
    else:
        return float(angle_string[:-1])

def is_a_number(s:str)-> bool:
    """
    Returns True if and only if s is a string representing a positive number.

    Examples:
    >>> is_a_number("1")
    True
    >>> is_a_number("One")
    False
    >>> is_a_number("-3")
    False
    >>> is_a_number("3.")
    True
    >>> is_a_number("3.1.2")
    False
    >>> is_a_number("0")
    False
    >>> is_a_number("a.45")
    False
    >>> is_a_number("-14.6")
    False
    >>> is_a_number("    26 ")
    True
    >>> is_a_number("    2.4")
    True
    >>> is_a_number(" 6    . 7")
    False
    >>> is_a_number("   5. ")
    True
    >>> is_a_number("")
    False
    """
    if s.isalnum():
        if s.isdigit():
            return float(s) > 0.0
        else:
            return False
    elif not s.isalnum():
        ns = s.strip()
        if ns.isdigit():
            return float(ns) > 0.0
        elif s.count(".") == 1:
            new_s = ns.replace(".", "")
            if new_s.isdigit():
                return float(ns) > 0.0
            else:
                return False
        else:
            return False
    else:
        return False
        
    

def is_valid_angle(s:str)-> bool:
    """
    Returns True if and on(ly if s is a valid angle. See the assignment
    description and examples for more information regarding what's valid

    Examples:
    >>> is_valid_angle("85.3d")
    True
    >>> is_valid_angle("85.3.7D")
    False
    >>> is_valid_angle("90d")
    False
    >>> is_valid_angle("0.001r")
    True
    >>> is_valid_angle("1.5R")
    True   
    >>> is_valid_angle("br")
    False
    >>> is_valid_angle("")
    False
    >>> is_valid_angle("cd")
    False
    >>> is_valid_angle("70")
    False
    >>> is_valid_angle("1.3")
    False
    """
    if s == "" or s == '':
        return False
    elif s[-1] == "d" or s[-1] == "D":
        if is_a_number(s[:-1]) == True:
            if float(s[:-1]) < 90.0:
                return True
            else:
                return False
        else:
            return False
    elif s[-1] == "r" or s[-1] == "R":
        if is_a_number(s[:-1]) == True:
            if float(s[:-1]) < (pi/2):
                return True
            else:
                return False
        else:
            return False
    else:
        return False
        

def approx_equal(x, y, tol):
    """
    Returns True if and only if x and y are with tol of each other.

    Examples:
    >>> approx_equal(1,2,1)
    True
    >>> approx_equal(4,3,1)
    True
    >>> approx_equal(4,3,0.99)
    False
    >>> approx_equal(-1.5,1.5,3)
    True
    >>> approx_equal(3, 4, 2)
    True
    >>> approx_equal(-5, -7, 4)
    True
    """
    if x > y:
        return tol >= x-y
    else:
        return tol >= y-x
    

"""
DO NOT MODIFY THE CODE BELOW.

You are not required/expected to understand the following code.
If you're interested though, take a look.
"""
if __name__ == "__main__":
    while True:
        target = float(input("Enter a target distance: "))
        tol = float(input("Enter how close you need to be to your target: "))
        target_hit = False
        while not target_hit:
            valid_velocity = False
            while not valid_velocity:
                v = input("Enter a valid velocity: ")
                valid_velocity = is_a_number(v)   
            valid_angle = False
            v = float(v)
            while not valid_angle:
                theta = input("Enter a valid angle: ")
                valid_angle = is_valid_angle(theta)
            theta = get_radian_of(theta)
            d = get_distance(float(v), theta)
            target_hit = approx_equal(target, d, tol)
            if target_hit:
                print("Congratulations! You hit the target.")
            elif target > d:
                print("The shot hit short of the target, try again.")
            else: 
                print("The shot hit past the target, try again.")
            
                
