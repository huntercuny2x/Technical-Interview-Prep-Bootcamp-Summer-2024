def lengthOfLongestSubstringBruteForce(s):
    #brute force
    max_length=0
    for l in range (len(s)):
        char_set=set()
        for r in range(l,len(s)):
            if s[r] in char_set:
                break
            else:
                char_set.add(s[r])
                max_length=max(max_length,len(char_set))
    return max_length


def lengthOfLongestSubstring(s):
    l,r,max_length = 0,0,0
    char_set=set() # keeps track of all characters between l and r
    while r< len(s):
        if s[r] in char_set:
            char_set.remove(s[l])
            l+=1
        
        else:
            char_set.add(s[r])
            max_length=max(max_length, len(char_set))
            r+=1

    return max_length
