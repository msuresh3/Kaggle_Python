def prepared_for_weather(have_umbrella, rain_level, have_hood, is_workday):
    # Don't change this code. Our goal is just to find the bug, not fix it!
    return have_umbrella or rain_level < 5 and have_hood or not rain_level > 0 and is_workday
    #return False or True and False or not False and False
    #return True or True or True and True
    #return 0.0 < 5 #True
    #return 0.0 > 0 #False
    #return True and False #False
    #return True or False #True
    

# Change the values of these inputs so they represent a case where prepared_for_weather
# returns the wrong answer.
#have_umbrella = True
#rain_level = 0.0
#have_hood = True
#is_workday = True

have_umbrella = False
rain_level = 0.0
have_hood = False
is_workday = False

# Check what the function returns given the current values of the variables above
actual = prepared_for_weather(have_umbrella, rain_level, have_hood, is_workday)
#print(actual)

def is_negative(number):
    if number < 0:
        return True
    else:
        return False

def concise_is_negative(number):
    return(number < 0)
    # Your code goes here (try to keep it to one line!)

# Check your answer
print (concise_is_negative(-1))
print (concise_is_negative(0))
print (concise_is_negative(1))