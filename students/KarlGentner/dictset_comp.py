#!/usr/bin/python


# Displays the given dictionary
def displayDict(a_dict):
    for key, value in a_dict.iteritems():
        print(u"{key} : {value}").format(key=key, value=value)


# Displays the given set
def displaySet(a_set):
    for x in a_set:
        print x,


        # Displays the current set
def displayListSet(list):
    for x in range(len(list)):
        print list[x]


# construct dictionary
food_prefs = {u"name": u"Chris",
              u"city": u"Seattle",
              u"cake": u"chocolate",
              u"fruit": u"mango",
              u"salad": u"greek",
              u"pasta": u"lasagna"}
print u"\nDictionary 'food_prefs':"
displayDict(food_prefs)


# 1. Print the dict by passing it to a string format method, so that you get something like:
# “Chris is from Seattle, and he likes chocolate cake, mango fruit, greek salad, and lasagna pasta”

# 2.  Using a list comprehension, build a dictionary of numbers from zero to fifteen and the hexadecimal equivalent (string is fine).
nums = range(16)
hexnums = [hex(x) for x in nums]
z = dict(zip(nums, hexnums))
print u"\nDictionary 'z' with keys 0 to 15 and hexadecimal equivalent values:"
displayDict(z)

# 3. Do the previous entirely with a dict comprehension – should be a one-liner


# 4. Using the dictionary from item 1: Make a dictionary using the same keys but with the number of ‘a’s in each value.
# You can do this either by editing the dict in place, or making a new one. If you edit in place, make a copy first!
e = {key: value.count('a') for key, value in food_prefs.iteritems()}
print u"\nDictionary 'e' : a copy of dictionary 'food_prefs' with the number of a's in each value:"
displayDict(e)


# 5. Create sets s2, s3 and s4 that contain numbers from zero through twenty, divisible 2, 3 and 4.
# 5-1. Do this with one set comprehension for each set.
s2 = {i for i in range(21) if i % 2 == 0}
s3 = {i for i in range(21) if i % 3 == 0}
s4 = {i for i in range(21) if i % 4 == 0}

print u"\n\nSet s2:"
displaySet(s2)
print u"\n\nSet s3:"
displaySet(s3)
print u"\n\nSet s4:"
displaySet(s4)


# 5-2. What if you had a lot more than 3? – Don’t Repeat Yourself (DRY)
# 5-2-i. create a sequence that holds all three sets
# 5-2-ii. loop through that sequence to build the sets up – so no repeated code.
lsthree = [{}, {}, {}]
for x in range(len(lsthree)):
    lsthree[x] = {i for i in range(21) if i % (x+2) == 0}
print u"\n\nList with sets s2, s3, and s4:"
displayListSet(lsthree)


# 5c Extra credit: do it all as a one-liner by nesting a set comprehension inside a list comprehension. (OK, that may be getting carried away!)
lsthree = [{i for i in range(21) if i % (x+2) == 0} for x in range(3)]
print u"\n\nOne liner - List with sets s2, s3, and s4:"
displayListSet(lsthree)


# Also, how about a function that creates these set based on parameters
def divSetGen(n=3, m=20):
    """Return a list of 'n' sets that each contains numbers from 0 to 'm', divisible by the list index + 2 """
    return [{i for i in range(m+1) if i % (x+2) == 0} for x in range(n)]
lsfive = divSetGen(5)
print u"\n\nFunction returns - List with sets s2, s3, s4, s5, and s6:"
displayListSet(lsfive)
