# Implementing Luhn's algorithm on SIN numbers.
# Idea: https://www.geeksforgeeks.org/luhn-algorithm/
def check_sin(num):
    # A SIN number has 9 digits
    if (len(str(num)) != 9):
        print("Invalid SIN! Please enter a valid SIN.")
        return False
    
    # Source:
    # https://www.geeksforgeeks.org/python-convert-number-to-list-of-integers/
    sin = [int(i) for i in str(num)]

    # Get a new list to be added to get modulo 10
    d = 1
    while (d < len(sin) - 1):
        new_num = sin[d]*2
        if (new_num > 9):
            total = 0
            for n in str(new_num):
                total += int(n)
            new_num = total
        sin[d] = new_num
        d += 2

    # Checks if SIN is valid    
    s = 0
    for digit in sin:
        s += digit
    if (s % 10 != 0):
        print("Invalid SIN! Please enter a valid SIN.")
        return False
    print("Thank you for providing your SIN number.")
    return True

# Implementing Luhn's algorithm on credit card numbers. Only for Visa and
# MasterCard
def check_card(num):
    # MasterCard has 16 digits and Visa has 19 digits
    # https://smallbusiness.chron.com/identify-credit-card-account-number-61050.html
    if (len(str(num)) != 16 or len(str(num)) != 19):
        print("Invalid number! Please enter a valid credit card number.")
        return False
    
    # Source:
    # https://www.geeksforgeeks.org/python-convert-number-to-list-of-integers/
    card = [int(i) for i in str(num)]

    # Get a new list to be added to get modulo 10
    d = 1
    while (d < len(card) - 1):
        new_num = card[d]*2
        if (new_num > 9):
            total = 0
            for n in str(new_num):
                total += int(n)
            new_num = total
        card[d] = new_num
        d += 2

    # Checks if SIN is valid    
    s = 0
    for digit in card:
        s += digit
    if (s % 10 != 0):
        print("Invalid number! Please enter a valid credit card number.")
        return False
    
    print("Thank you for providing your credit card number.")
    return True

# Checks card type
def check_type(num):
    if (check_card(num) == True):
        if (len(str(num)) == 16 and str(num)[0] == '5'):
            return "This is a MasterCard."
        elif (len(str(num)) == 19 and str(num)[0] == '4'):
            return "This is a Visa."

    return "It is either another card or it is an invalid card."
