# We have an array of strings. Consider each string as a zero-indexed array of
# characters. All of the characters will be in the range ascii[a-z] which have 
# decimal values in the range [97-122]. These decimal values are called ordinal
# values and will be referred to as ord[a]=97 for example.
# Given an array of strings s = [s[0],s[1],...s[n-1]], and an integer m, we
# calculate a value of each s[i] of length len(s[i]) as:
# value[i] = ord[s[i][0]]^m × ord[s[i][1]]^m × … × ord[s[i][len(s[i])-1]^m
# Perform the calculation on each string, sum them up, and determine whether 
# their sum is EVEN or ODD.


def oddString(str_arr,m):
    sum = 0
    for s in str_arr:
        product=1
        for c in s:
            product*=ord(c)**m
        sum+=product
    print(sum)
    return 'EVEN' if sum%2==0 else 'ODD'


def oddString2(str_arr,m):
    sum = 0
    for s in str_arr:
        product=1
        for c in s:
            product*=(ord(c)%10)**m
        sum+=(product%10)
    print(sum)
    return 'EVEN' if sum%2==0 else 'ODD'


def oddString3(str_arr,m):
    sum = 0
    for s in str_arr:
        product=1
        for c in s:
            if ord(c) % 2 == 0:
                product=0
                break
        sum+=product
    print(sum)
    return 'EVEN' if sum%2==0 else 'ODD'

# # test 1 (seem to be wrong in file)
# print(oddString(['abc','abcd'],2))
# print(oddString2(['abc','abcd'],2))
# print(oddString3(['abc','abcd'],2))

# # test 2 (seem to be wrong in file)
# print(oddString(['aceace', 'ceceaa', 'abdbdbdbakjkljhkjh'],2))
# print(oddString2(['aceace', 'ceceaa', 'abdbdbdbakjkljhkjh'],2))
# print(oddString3(['aceace', 'ceceaa', 'abdbdbdbakjkljhkjh'],2))

# # test 3 (seem to be wrong in file)
# print(oddString(["azbde", " abcher", " acegk"],2))
# print(oddString2(["azbde", " abcher", " acegk"],2))
# print(oddString3(["azbde", " abcher", " acegk"],2))

# # test 4 (good to go)
# print(oddString(['austin', 'dallas', 'houston'],3))
# print(oddString2(['austin', 'dallas', 'houston'],3))
# print(oddString3(['austin', 'dallas', 'houston'],3))

# # test 5 (good to go) (forced odd case)
# print(oddString(['aaaaa', 'ccccc', 'eeeee', 'gggg', 'iiii'],4))
# print(oddString2(['aaaaa', 'ccccc', 'eeeee', 'gggg', 'iiii'],4))
# print(oddString3(['aaaaa', 'ccccc', 'eeeee', 'gggg', 'iiii'],4))

# test 6 (good to go) 
#print(oddString(['aaaaa', 'ccccc', 'eeeee', 'gggg', 'iiii'],1000))
print(oddString2(['aaaaa', 'ccccc', 'eeeee', 'gggg', 'iiii'],1000000000))
print(oddString3(['aaaaa', 'ccccc', 'eeeee', 'gggg', 'iiii'],1000000000))