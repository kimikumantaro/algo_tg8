str = "ABABDABACDABABCABAB"
pat = "ABABCABAB"

def kmpSearch(pat, str):
    x = len(pat) # size of pattern
    y = len(str) # size of reference string

    lps = [0]*x # intialize lps[] to hold the longest prefix suffix values from pattern
    n = 0 # index for pat

    calculateLpsArray(pat, x, lps) # calculate the lps/pie array

    m = 0 # index for str

    flag = True
    while m < y:
        if pat[n] == str[m]:
            m += 1
            n += 1

        if n == x:
            print("Pattern found at index", (m-n))
            flag = False
            n = lps[n-1]

        elif m < y and pat[n] != str[m]:

            if n != 0:
                n = lps[n-1]
            else:
                m += 1
    else:
        if flag:
            print("Pattern not found")


def calculateLpsArray(pat, x, lps):
    j = 0 # backpointer on pattern

    lps[j] = 0 # first element in lps table must be zero
    i = 1 # frontpointer on pattern

                #x = 9
    while i < x: #"ABABCABAB" lps[0,0,1,2,0,1,2,3,4]
                             #pat[0,0,0,0,j,0,0,0,0]
        if pat[i] == pat[j]:
            j += 1
            lps[i] = j
            i += 1
        else:
            if j != 0:
                j = lps[j-1] # j pointer backwards, i pointer never backwards

            else:
                lps[i] = 0 # put 0 in lps[]
                i += 1 # then i is incremented

kmpSearch(pat, str)