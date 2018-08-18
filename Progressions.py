# -*- coding: utf-8 -*-
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
    b = True
    tone = ''
    for i in range(0, len(c)-1):
        if(abs(c[i]-c[i+1]) != mj[i+1]): b = False
    if b == False: tone = 'Minor'
    if b == True: tone = 'Major'
    return keys[c[0]] + ' ' + tone
# Turns a progression into words
def pW(p):
    words = [] 
    for i in p:
        words.append(cW(i))
    return words
# Prints a progression
def printP(p):
    s = ''
    if type(p[0]) == str: 
        for i in range(0, len(p)-1):
            s+=p[i]+', '
        s+=p[len(p)-1]
    elif type(p[0]) == list:
        cs = []
        for i in p:
            cs.append(cW(i))
        for i in range(0, len(cs)-1):
            s+=cs[i]+', '
        s+=cs[len(cs)-1]
    print s
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
def printT(p1, k):
    p = transpose(p1)
    i = pW(p1)
    ii = pW(p)1
    
# Progressions – Two word entries, e.g. 'Gb Minor', not 'G Flat Minor'.
i = ['Db Minor', 'B Major', 'Gb Major']
i = transpose(i, 'C')
printP(i)
#ii = read(['G Minor', 'F Major', 'Eb Major', 'D Major'])
# iii = read(['C Minor', 'Eb Major', 'G Minor', 'F Major'])