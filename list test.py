###
def purple_shell(racers):
    """Given a list of racers, set the first place racer (at the front of the list) to last
    place and vice versa.
    
    >>> r = ["Mario", "Bowser", "Luigi"]
    >>> purple_shell(r)
    >>> r
    ["Luigi", "Bowser", "Mario"]
    """
    racers[0],racers[-1] = racers[-1],racers[0]
    print (racers)

r = ["Mario", "Bowser", "Luigi"]
#print (r)
#purple_shell(r)

####
a = [1, 2, 3]
b = [1, [2, 3]]
c = []
d = [1, 2, 3][1:]
#print (len(a))
#print (len(b))
#print (len(c))
#print (len(d))

###
#party_attendees = ['Adela', 'Fleda', 'Owen', 'May', 'Mona', 'Gilbert', 'Ford']
party_attendees = ['Adela', 'Fleda', 'Owen', 'May', 'Mona', 'Gilbert']

def fashionably_late(arrivals, name):
    """Given an ordered list of arrivals to the party and a name, return whether the guest with that
    name was fashionably late.
    """
    #late = []
    if(((len(arrivals)%2)) == 1):
        mid = int(len(arrivals)/2)+1
    else:
        mid = int(len(arrivals)/2)
    late = arrivals[mid:-1]
    print (late)
    #return (name in late)
    return (None)

print (fashionably_late(party_attendees,'Adela'))
#print (fashionably_late(party_attendees,'Fleda'))
#print (fashionably_late(party_attendees,'Owen'))
#print (fashionably_late(party_attendees,'May'))
#print (fashionably_late(party_attendees,'Mona'))
#print (fashionably_late(party_attendees,'Gilbert'))
#print (fashionably_late(party_attendees,'Ford'))

