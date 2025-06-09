from typing import List

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        counter=0
        length=len(nums)
        for i in range (length):
            print("for",i,nums[i])
            if nums[i]==0:
                nums.pop(i)
                print("pop",i)
                counter+=1
        if counter>0:
            for i in range(counter):
                nums.append(0)



a=Solution()
my_list = [0,0,1]  
print("Before:", my_list)
a.moveZeroes(my_list)
print("After:", my_list)
