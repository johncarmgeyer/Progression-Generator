# The 12 keys in array form
keys1 = ['A', 'Bb', 'B', 'C', 'Db', 'D', 'Eb', 'E', 'F', 'Gb', 'G', 'Ab']
keys = keys1+keys1[0:12]
# Tones, quantified
mj = [0, 4, 7]
mn = [0, 3, 7]
# Loops through a list and adds a set quantity to each index
def add(lst, amount):
    l1 = []
    for i in lst:
        l1.append(i+amount)
    return l1
# Returns the index of a key's index in the 'keys' list
def search(k):
    c = 0
    for i in keys1:
        if(k==i): return c
        c+=1
    return -1
# Converts chords in two-word format to an array of numbers
def convert(c):
    key = search(c.split(' ')[0])
    tone = c.split(' ')[1]
    if tone == 'Minor':
        return add(mn, key)
    elif tone == 'Major':
        return add(mj, key)
# Processes an array of chords, i.e. a progression, and returns the progression in numerical form
def read(p):
    cs = []
    for i in p:
        cs.append(convert(i))
    cs1 = []
    for i in cs:
        cs1.append(add(i, -cs[0][0]))
    cs2 = []
    cs2.append(cs1[0])
    for i in range(0, len(cs1)-1):
        if(abs(cs1[i][0]-cs1[i+1][0]) > 6):
            cs2.append(add(cs[i+1], -16))
        else:
            cs2.append(cs1[i+1])
    return cs2
# Turns a chord into words
def cW(c):
    a = True
    for i in range(0, len(c)-1):
        if(abs(c[i]-c[i+1]) != abs(mj[i]-mj[i+1])): a = False
    b = True
    for i in range(0, len(c)-1):
        if(abs(c[i]-c[i+1]) != abs(mn[i]-mn[i+1])): b = False
    tone = ''
    if a == True: tone = 'Major'
    elif b == True: tone = 'Minor'
    else: tone == 'Null'
    return keys[c[0]] + ' ' + tone
# Prints a progression
def printP(p):
    s = ''
    cr = ' | '
    if type(p[0]) == str: 
        for i in range(0, len(p)-1):
            if(len(p[i]) == 7): cr='  | '
            else: cr = ' | '
            s+=p[i]+cr
        s+=p[len(p)-1]
    elif type(p[0]) == list:
        cs = []
        for i in p:
            cs.append(cW(i))
        for i in range(0, len(cs)-1):
            if(len(cs[i]) == 7): cr='  | '
            else: cr = ' | '
            s+=cs[i]+cr
        s+=cs[len(cs)-1]
    return s
# Transposes progressions from one key to another
# 'k' is either a key, e.g. 'D', or a numerical value.
def transpose(p1, k):
    p = read(p1)
    if type(k) == int: 
        p2 = []
        val = k+search(p1[0].split(' ')[0])
        if(val > 6): val = val-12
        for i in p:
            p2.append(add(i, val))
        return p2
    if type(k) == str: 
        p3 = []
        val = search(k)
        if(val > 6): val = val-12
        for i in p:
            p3.append(add(i, val))
        return p3
# Prints a two-progression transposition 
count = 0
def printT(p1, k):
    global count
    count+=1
    p = transpose(p1, k)
    i = printP(p1)
    ii = printP(p)
    print str(count)+'.\n'+i+' \n\n'+ii+'\n'
    
# Progressions – Two word entries, e.g. 'Gb Minor', not 'G Flat Minor'.
i = ['Db Minor', 'B Major', 'Gb Major']
ii = ['G Minor', 'F Major', 'Eb Major', 'D Major']
iii = ['C Minor', 'Eb Major', 'G Minor', 'F Major']
# Function Implementation
# Transposition Values: [-27, 25]
printT(i, -1)
printT(ii, 4)
printT(iii, -8)
