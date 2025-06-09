#  Given 2 arrays, create a function that let's a user know (true/false) whether these two arrays contain any common items
# For Example:
# const array1 = ['a', 'b', 'c', 'x'];//const array2 = ['z', 'y', 'i'];
# should return false.
# -----------
# const array1 = ['a', 'b', 'c', 'x'];//const array2 = ['z', 'y', 'x'];
# # should return true
#  2 parameters - arrays - no size limit
#  return true or false


def isCommonItems(list1,list2):
    object1={}

    for item in list1:
        object1[item]=True


    for item in list2:
        if item in object1:
            return 
        

#Using Set
def isCommonItems1(list1, list2):
    try:
        set2 = set(list2)
    except TypeError:
        raise ValueError("list2 contains unhashable elements (e.g., lists or dicts)")
    
    for item in list1:
        if item in set2:
            return True
    return False




# What tests would I write to make this function fail?

#     has_common_item_safe(5, [1, 2]) → should raise "list1 is not iterable".

#     has_common_item_safe([1, 2], 5) → should raise "list2 is not iterable".

#     has_common_item_safe([1, 2], [[3], 4]) → should raise "list2 contains unhashable elements".

#     has_common_item_safe([[1], 2], [2, 3]) → should raise "list1 contains unhashable elements".

#     has_common_item_safe(None, None) → should raise "list1 is not iterable".

#     has_common_item_safe([], []) → should return False.

#     has_common_item_safe([1, 2], [2, 3]) → should return True.

#     Pass empty iterables, generators, or custom iterable objects to verify behavior.


#Additional considerations to ask the interviewer

#     Can I assume inputs will always be iterables?

#     Can elements be unhashable or custom objects?

#     What should happen if inputs are empty or None?

#     Should I optimize for very large inputs?

#     Should I handle asynchronous iterables?

#     Is performance or memory usage critical here?





### Talking points to the interviewer:

# **1. Does it work?**

# * Yes, the function mostly works for well-formed, hashable, iterable inputs.
# * It correctly detects common elements between the two collections.
# * However, it can break or raise unclear errors for unhashable elements in `list1` or non-iterable inputs, which I’ve added checks for.

# **2. Different approaches?**

# * Using sets is efficient for membership checks — O(1) average time per lookup.
# * Another approach: convert both lists to sets and use set intersection (`bool(set(list1) & set(list2))`). This simplifies code but raises `TypeError` if unhashable elements exist in either list.
# * For very large inputs, or if inputs contain unhashable elements, a brute force nested loop might be needed but would be O(n\*m) — not scalable.
# * If inputs are sorted lists, a two-pointer approach could be efficient without hashing.
# * If inputs contain unhashable but comparable elements, custom hashing or equality functions might be used.

# **3. Is it readable?**

# * The code is readable and straightforward.
# * Adding helper functions (e.g., for iterable check) would improve clarity and reduce repetition.
# * Clear comments and meaningful error messages help maintainability.

# **4. What would I google to improve it?**

# * “Python check if object is iterable”
# * “Handling unhashable elements in Python sets”
# * “Python set intersection performance”
# * “Efficient algorithms to find common elements between two lists”
# * “Python membership test optimization”
# * “Handling async iterables in Python”

# **5. How can performance be improved?**

# * If input sizes differ greatly, convert the smaller list to a set for better memory and time efficiency.
# * Early exit as soon as a common item is found (already done).
# * For extremely large inputs, consider streaming and chunk processing to reduce memory.
# * If inputs are sorted, use two-pointer traversal instead of hashing.
# * If multiple queries are made on the same lists, caching sets can improve repeated calls.

# ---

# ### A question for the interviewer:

# *“Out of curiosity, what’s the most interesting or clever solution you’ve seen for finding common elements between two collections, especially when inputs might have unhashable elements or very large size?”*

# ---

# This kind of conversation shows:

# * Awareness of limitations and improvements
# * Familiarity with alternative algorithms
# * Interest in learning from others’ experience


