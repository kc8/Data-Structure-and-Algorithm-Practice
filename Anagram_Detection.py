def anagramSolution(s1, s2):
   """
        This is n^2 
    """
    stillOk = True
    if len(s1) != len(s2):
        stillOk = False
    
    alist = list(s2)
    pos1 = 0

    while pos1 < len(s1) and stillOk: #Go through s1 n times
        pos2 = 0
        found = False
        while pos2 < len(alist) and not found: #Go though s2 n times
            if s1[pos1] == alist[pos2]:
                found = True
            else:
                pos2 = pos2 + 1
        
        if found: 
                alist[pos2] = None
        else: 
                stillOk = False 
        
        pos1 = pos1 + 1
    return stillOk

print(anagramSolution('abcd', 'dcba'))

def anagramSolution2(s1, s2):
    """
    The sorting operation is iether n^2 or nlogn. So it is not just n because of our 
    loop through the string

    """
    alist1 = list(s1)
    alist2 = list(s2)

    alist1.sort() #Has a cost
    alist2.sort() #has a cost

    pos = 0
    matches = True

    while pos < len(s1) and matches: #loop through n times
        if alist1[pos] == alist2[pos]:
            pos = pos + 1
        else: 
            matches = False
    return matches

print(anagramSolution2('abcde', 'edcba'))

def anagramSolution4(s1, s2):
    """
    Count and Compare. Takes advatnage of knowing the fact that an anagram will have the same number
    of a's, b's and c's etc. 
    This solution is n 

    """

    c1 = [0]*26
    c2 = [0]*26

    for i in range(len(s1)):
        pos = ord(s1[i]-ord('a'))
        c1[pos] = c1[pos] + 1
    
    for i range(len(s2)):
        pos = ord(s2[i]-ord('a'))
        c2[pos] = c2[pos] + 1
    
    j = 0 
    stillOk = True
    while j<26 and stillOk: 
        if c1[j] == c2[j]:
            j += 1
        else: 
            stillOk = False

    return stillOk

print(anagramSolution4('apple', 'pleep'))