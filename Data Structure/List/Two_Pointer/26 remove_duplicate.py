# Core Logic:

#     If nums[j] is different from nums[i]:
#         It's a new unique element.
#         Advance i (i += 1).
#         Copy nums[j] to nums[i] (nums[i] = nums[j]).
#     If nums[j] is the same as nums[i]:
#         It's a duplicate.
#         Do nothing (just let j advance)


def remove_duplicates_return_list(nums):
    if not nums:
        return []

    i = 0  # Points to the last unique element
    for j in range(1, len(nums)):
        if nums[i] != nums[j]:
            i += 1
            nums[i] = nums[j]

    return nums[:i+1]



    "Since the array is sorted, any duplicates will be adjacent. This allows us to solve the problem efficiently using a two-pointer approach. " 
     

    "We use one pointer i to track the position of the last unique element, and another pointer j to scan through the array. When num[i] != num[j], it means we’ve found a new unique value. We increment i and update num[i] with this new value. " 
     

    "This keeps all the unique elements compacted at the beginning of the array without using extra space. Finally, we return the subarray from index 0 to i + 1 — which contains all the unique values in order. " 
     
