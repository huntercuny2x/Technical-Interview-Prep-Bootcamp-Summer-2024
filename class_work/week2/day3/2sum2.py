def twoSum2(numbers, target):
    l, r = 0, len(numbers)-1
    while l<r:
        check_num = numbers[l]+numbers[r]
        if target == check_num:
            return [l+1,r+1]
        if target < check_num:
            r=r-1
        elif target > check_num:
            l=l+1

