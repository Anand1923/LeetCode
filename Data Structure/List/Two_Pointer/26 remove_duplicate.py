# Core Logic:

#     If nums[j] is different from nums[i]:
#         It's a new unique element.
#         Advance i (i += 1).
#         Copy nums[j] to nums[i] (nums[i] = nums[j]).
#     If nums[j] is the same as nums[i]:
#         It's a duplicate.
#         Do nothing (just let j advance)


def remove_dup(num):
    if not num:
        return 0
    i=0
    for j in range(1,len(num)):
        if num[i]!=num[j]:
            i+=1
            num[i]=num[j]
