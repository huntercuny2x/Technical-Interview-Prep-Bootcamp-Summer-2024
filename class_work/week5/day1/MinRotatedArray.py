def findMin(nums):
        l,r=0,len(nums)-1

        while l<=r:
            mid=(l+r)//2
            if nums[l]<nums[r] or l == r:
                return nums[l]
            elif nums[l] <= nums[mid]:
                l=mid+1
            else :
                r=mid