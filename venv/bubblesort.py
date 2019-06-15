def sort(nums):
    print(nums)
    for i in range(len(nums)-1,0,-1):
        for j in range(i):
            if nums[j]>nums[j+1]:
                t=nums[j]
                nums[j]=nums[j+1]
                nums[j+1]=t
        print(nums)
    #print(nums)






nums=[6,5,4,3,2,1]
sort(nums)
#print(nums)
