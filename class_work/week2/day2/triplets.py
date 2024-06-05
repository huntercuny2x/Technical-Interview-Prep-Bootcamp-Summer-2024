# Given an array of n distinct integers, d = [d[0], d[1], …, d[n−1]], and an 
# integer threshold, t, how many (a, b, c) index triplets exist that satisfy
# both of the following conditions?

# d[a] < d[b] < d[c]
# d[a] + d[b] + d[c] ≤ t

def triplets(d, t):
    d=sorted(d)
    count=0
    for i in range(len(d)-2):
        l, r = i+1, len(d)-1 
        while l<r:
            if d[i]+d[l]+d[r] <= t:
                count+=(r-l)
                l+=1
            else:
                r-=1
    return count


# test 1 
print(triplets([1,2,3,4,5], 8))

# test 2
print(triplets([1,2,3,4,6], 8))

# test 2
print(triplets( [3, 1, 2, 4], 7))