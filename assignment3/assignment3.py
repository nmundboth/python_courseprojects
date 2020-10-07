from typing import List, Dict, Tuple

def create_profile_dictionary(file_name: str) \
        -> Dict[int, Tuple[str, List[int], List[int]]]:
    """
    Opens the file "file_name" in working directory and reads the content into a
    profile dictionary as defined on Page 2 Functions 1.

    Note, some spacing has been added for human readability.
    
    >>> create_profile_dictionary("profiles.txt")
    {100: ('Mulan', [300, 500], [200, 400]), 
    200: ('Ariel', [100, 500], [500]), 
    300: ('Jasmine', [500], [500, 100]), 
    400: ('Elsa', [100, 500], []), 
    500: ('Belle', [200, 300], [100, 200, 300, 400])}
    """
    profiles = open(file_name, "r")
    profiles_dict = {}
    lines = profiles.readlines()
    i = 0
    j = 1
    k = 2
    l = 3
    while (i <= len(lines) and j <= len(lines) and k <= len(lines) and\
           l <= len(lines)):
        profiles_dict[int(lines[i].replace("\n", ""))] = \
                                                 (str(lines[j].replace("\n", "")), \
                                                  str_to_int(lines[k]),\
                                                  str_to_int(lines[l]))
        i += 5
        j += 5
        k += 5
        l += 5
    profiles.close()
    return profiles_dict


def create_chirp_dictionary(file_name: str) \
        -> Dict[int, Tuple[int, str, List[str], List[int], List[int]]]:
    """
    Opens the file "file_name" in working directory and reads the content into a
    chirp dictionary as defined on Page 2 Functions 2.

    Note, some spacing has been added for human readability.
    
    >>> create_chirp_dictionary("chirps.txt")
    {100000: (
        400, 
        'Does not want to build a %SnowMan %StopAsking',
        ['SnowMan', 'StopAsking'], 
        [100, 200, 300], 
        [400, 500]), 
    100001: (
        200, 
        'Make the ocean great again.', 
        [''], 
        [], 
        [400]), 
    100002: (
        500, 
        "Help I'm being held captive by a beast!  %OhNoes", 
        ['OhNoes'], 
        [400], 
        [100, 200, 300]), 
    100003: (
        500, 
        "Actually nm. This isn't so bad lolz :P %StockholmeSyndrome", 
        ['StockholmeSyndrome'], 
        [400, 100], 
        []), 
    100004: (
        300, 
        'If some random dude offers to %ShowYouTheWorld do yourself a favour and %JustSayNo.', 
        ['ShowYouTheWorld', 'JustSayNo'], 
        [500, 200], 
        [400]), 
    100005: (
        400, 
        'LOLZ BELLE.  %StockholmeSyndrome  %SnowMan', 
        ['StockholmeSyndrome', 'SnowMan'], 
        [], 
        [200, 300, 100, 500])}
    100006: (
        500, 
        'LOLZ BELLE.  %StockholmeSyndrome  %SnowMan', 
        ['StockholmeSyndrome', 'SnowMan'], 
        [], 
        [200, 300, 100, 500])}
    """
    chirps = open(file_name, "r")
    chirps_dict = {}
    lines = chirps.readlines()
    i = 0
    j = 1
    k = 2
    l = 3
    m = 4
    n = 5
    while (i <= len(lines) and j <= len(lines) and k <= len(lines) and\
           l <= len(lines)):
        chirps_dict[int(lines[i].replace("\n", ""))] = \
                                                 (int(lines[j].replace("\n", "")), \
                                                  str(lines[k].replace("\n", "")),\
                                                  lines[l].replace("\n", "").split(","),\
                                                  str_to_int(lines[m]),\
                                                  str_to_int(lines[n]))
        i += 7
        j += 7
        k += 7
        l += 7
        m += 7
        n += 7
    chirps.close()
    return chirps_dict

def get_top_chirps( \
        profile_dictionary: Dict[int, Tuple[str, List[int], List[int]]], \
        chirp_dictionary: Dict[int, Tuple[int, str, List[str], List[int], List[int]]],
        user_id: int)\
        -> List[str]:
    """
    Returns a list of the most liked chirp for every user user_id follows.
    See Page 3 Function 3 of th .pdf.
    >>> profile_dictionary = create_profile_dictionary("profiles.txt")
    >>> chirp_dictionary   = create_chirp_dictionary("chirps.txt")
    >>> get_top_chirps(profile_dictionary, chirp_dictionary, 300)
    ["Actually nm. This isn't so bad lolz :P %StockholmeSyndrome"]
    >>> get_top_chirps( profiles, chirps, 500 )
    ['Make the ocean great again.', 
    'If some random dude offers to %ShowYouTheWorld do yourself a favour and %JustSayNo.', 
    'Does not want to build a %SnowMan %StopAsking']
    """
    lst = []
    for key in profile_dictionary:
        if key == user_id:
            l = profile_dictionary[user_id][2]
            for i in l:
                top_chirp(chirp_dictionary, i)
                if not(top_chirp(chirp_dictionary, i) == None):
                    lst.append(top_chirp(chirp_dictionary, i))
    return lst
    
def create_tag_dictionary( \
        chirp_dictionary: Dict[int, Tuple[int, str, List[str], List[int], List[int]]]) \
        -> Dict[str, Dict[int, List[str]]]:
    """
    Creates a dictionary that keys tags to tweets that contain them.

    Note, some spacing has been added for human readability.
    
    >>> chirp_dictionary = create_chirp_dictionary("chirps.txt")
    >>> create_tag_dictionary(chirp_dictionary)
    {'SnowMan': {
        400: ['Does not want to build a %SnowMan %StopAsking', 'LOLZ BELLE.  %StockholmeSyndrome  %SnowMan']}, 
    'StopAsking': {
        400: ['Does not want to build a %SnowMan %StopAsking']}, 
    '': {
        200: ['Make the ocean great again.']}, 
    'OhNoes': {
        500: ["Help I'm being held captive by a beast!  %OhNoes"]}, 
    'StockholmeSyndrome': {
        500: ["Actually nm. This isn't so bad lolz :P %StockholmeSyndrome"], 
        400: ['LOLZ BELLE.  %StockholmeSyndrome  %SnowMan']}, 
    'ShowYouTheWorld': {
        300: ['If some random dude offers to %ShowYouTheWorld do yourself a favour and %JustSayNo.']}, 
    'JustSayNo': {
        300: ['If some random dude offers to %ShowYouTheWorld do yourself a favour and %JustSayNo.']}}
    """
    d = {}
    tag_l = tags(chirp_dictionary)
    for k in tag_l:
        d[k] = {}
        for key in chirp_dictionary:
            sm = d[k]
            for ky in chirp_dictionary[key][2]:
                if k == ky.strip():
                    if chirp_dictionary[key][0] not in sm:
                        sm[chirp_dictionary[key][0]] = [chirp_dictionary[key][1]]
                    else:
                        sm[chirp_dictionary[key][0]].append(chirp_dictionary[key][1])
    return d

def get_tagged_chirps( \
        chirp_dictionary: Dict[int, Tuple[int, str, List[str], List[int], List[int]]], \
        tag: str) \
        -> List[str]:
    """
    Returns a list of chirps containing specified tag.
    >>> chirp_dictionary = create_chirp_dictionary("chirps.txt")
    >>> get_tagged_chirps(chirp_dictionary, "SnowMan")
    ['Does not want to build a %SnowMan %StopAsking', 
    'LOLZ BELLE.  %StockholmeSyndrome  %SnowMan']
    """
    tag_d = create_tag_dictionary(chirp_dictionary)
    l = []
    for k in tag_d:
        if k == tag:
            for key in tag_d[k]:
                for v in tag_d[k][key]:
                    l.append(v)
    return l


#Helper function for profile and chirp dictionaries.
#Returns "stringed" integers as a list of integers.
def str_to_int(string: str) -> List[int]:
    lst = []
    for num in string.replace("\n", "").split(","):
        if num == '':
            return []
        lst.append(int(num))
    return lst

#Helper function for tag dictionary.
#Creates a list of user ids without repetition of user ids.
def tags( \
    chirp_dictionary: Dict[int, Tuple[int, str, List[str], List[int], List[int]]]) \
        -> List[str]:
    l = []
    lst = []
    flat = []
    for k in chirp_dictionary:
        l.append(chirp_dictionary[k][2])
        for sublist in l:
            for item in sublist:
                it = str(item).replace(' ','')
                flat.append(it)
                for i in flat:
                    if i not in lst:
                        lst.append(i)
    return lst    

#Takes the chirp with the highest like.
def top_chirp( \
    chirp_dictionary: Dict[int, Tuple[int, str, List[str], List[int], List[int]]],
        i: int)\
        -> str:
    e = 0
    s = None
    for k in chirp_dictionary:
        if i == chirp_dictionary[k][0]:
            tup = chirp_dictionary.get(k)
            if len(tup[3]) >= e:
                e = len(tup[3])
                s = tup[1]
    return s
