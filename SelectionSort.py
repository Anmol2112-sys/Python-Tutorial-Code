def Selectionsort(nums):
       for i in range(len(nums)):
            min_pos=i
            for j in range(i+1,len(nums)):
                  if nums[j]<nums[min_pos]:
                        min_pos=j
            nums[i],nums[min_pos]=nums[min_pos],nums[i]

            
nums=[64,25,12,22,111]
Selectionsort(nums)
print("Sorted array:",nums)