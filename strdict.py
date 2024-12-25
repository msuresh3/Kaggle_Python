#planets = ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune']
#planet_to_initial = {planet: planet[0] for planet in planets}
#print(planet_to_initial)
#for planet, initial in planet_to_initial.items():
#    print("{} begins with \"{}\"".format(planet.rjust(10), initial))
#######

#numbers = {'one':1, 'two':2, 'three':3,'eleven': 11}
#numbers['one'] = 'Pluto'
#for k in numbers:
#    print("{} = {}".format(k, numbers[k]))
#######

#a = ""
#a = "it's ok"
#a = 'it\'s ok'
#a = """hey"""
#a = '\n'
#length = len(a)
#print(length)
#######

def is_valid_zip(zip_code):
    """Returns whether the input string is a valid (5 digit) zip code
    """
    count = 0
    digit_str = ['0','1','2','3','4','5','6','7','8','9']
    for char in zip_code:
        for digit in digit_str:
            if (char == digit):
                count = count + 1
    return (count == 5)
    #return len(zip_code) == 5 and zip_code.isdigit()
#print(is_valid_zip('1234x'))
####################

#claim = "Pluto plan is a planet! plan"
#claim.lower()
#print(claim.index('plan'))

def word_search(doc_list, keyword):
    """
    Takes a list of documents (each document is a string) and a keyword. 
    Returns list of the index values into the original list for all documents 
    containing the keyword.

    Example:
    doc_list = ["The Learn Python Challenge Casino.", "They bought a car", "Casinoville"]
    >>> word_search(doc_list, 'casino')
    >>> [0]
    """
    # list to hold the indices of matching documents
    indices = [] 
    # Iterate through the indices (i) and elements (doc) of documents
    for i, doc in enumerate(doc_list):
        # Split the string doc into a list of words (according to whitespace)
        tokens = doc.split()
        # Make a transformed list where we 'normalize' each word to facilitate matching.
        # Periods and commas are removed from the end of each word, and it's set to all lowercase.
        normalized = [token.rstrip('.,').lower() for token in tokens]
        # Is there a match? If so, update the list of matching indices.
        if keyword.lower() in normalized:
            indices.append(i)
    return indices

doc_list = ["The Learn Python Challenge casino.", "They bought a car", "Casino"]
print(word_search(doc_list, 'casino'))
 