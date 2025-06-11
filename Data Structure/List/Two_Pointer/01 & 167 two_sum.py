def has_pair_with_sum(numbers, target_sum):
    seen_numbers = set()
    for number in numbers:
        complement = target_sum - number
        if complement in seen_numbers:
            return True
        seen_numbers.add(number)
    return False



# To  return the indices
def two_sum(numbers, target_sum):
    index_map = {}
    for i, num in enumerate(numbers):
        complement = target_sum - num
        if complement in index_map:
            return [index_map[complement], i]
        index_map[num] = i




#Two Sum II -  Sorted array
# Two-Pointer Approach

#     Use two pointers: one starting from the beginning (left), one from the end (right)

#     Move pointers inward based on the sum

def two_sum(numbers,target_sum):
    left=0
    right=len(numbers)-1
    while(left<right):
        current_sum = numbers[left] + numbers[right]

        if current_sum==target_sum:
            return [left,right]
        elif (current_sum<target_sum):
            left=left+1
        else:
            right=right-1
    return []

arr=[1,2,3,4]
has_pair_with_sum(arr,5)




# 🔄 Summary: Unsorted vs Sorted Arrays
# Case	Best Approach	Time	Space	LeetCode Problem
# Unsorted	Hash map	O(n)	O(n)	#1
# Sorted	Two pointers	O(n)	O(1)	#167