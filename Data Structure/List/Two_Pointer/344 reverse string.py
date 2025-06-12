Python 
s = "hello"
reversed_s = s[::-1]  # "olleh"


def reverse(num):
    i=0
    j=len(num)-1
    while (i<j):
        num[i],num[j]=num[j],num[i]
        i+=1
        j-=1


def reverse_string(x: str):
    rev = ''
    for i in range(len(x) - 1, -1, -1):  #include 0 in loop
        rev = rev + x[i]
    return rev



#Leetcode 344
def reverse_integer(x: int) -> int:
    sign = -1 if x < 0 else 1
    x = abs(x)
    reversed_num = 0
    MAX_INT = 2**31 - 1

    while x > 0:
        digit = x % 10
        if reversed_num > MAX_INT // 10 or (reversed_num == MAX_INT // 10 and digit > 7):
            return 0
        reversed_num = reversed_num * 10 + digit
        x //= 10

    return sign * reversed_num if -2**31 <= reversed_num <= MAX_INT else 0



## 🧾 **Reverse Integer – Interview Cheat Sheet (Printable Version)**

Use this cheat sheet to **practice** the "Reverse Integer" problem confidently in mock interviews or whiteboarding sessions.

---

### 🔍 **Problem Summary**
- Reverse digits of a **32-bit signed integer**
- Return `0` if reversed number overflows 32-bit range

**Constraints:**
- Input range: `-2³¹` to `2³¹ - 1`  
- i.e., from **-2147483648** to **2147483647**

---

### 🧠 **Edge Cases to Consider**

| Case              | Example       | Output |
|-------------------|---------------|--------|
| Positive number   | `123`         | `321`  |
| Negative number   | `-123`        | `-321` |
| Ends with zero    | `120`         | `21`   |
| Zero              | `0`           | `0`    |
| Overflow          | `2147483647`  | `0`    |

---

### 🛠️ **Recommended Approach**
Use **modulo `%` and division `//`** to extract and build digits.

#### Why?
- No string conversion
- Efficient for large systems
- Manages overflow manually

---

### 📋 **Step-by-Step Plan**

1. **Save the sign**: `sign = -1 if x < 0 else 1`
2. **Work with absolute value**: `x = abs(x)`
3. **Initialize reversed_num**: `reversed_num = 0`
4. **Loop while x > 0**:
   - Get last digit → `digit = x % 10`
   - Remove last digit → `x = x // 10`
   - **Check for overflow before updating reversed_num**
   - Update → `reversed_num = reversed_num * 10 + digit`
5. **Apply sign and return result**: `return sign * reversed_num`

---

### ⚠️ **Overflow Check (Critical!)**

```python
MAX_INT = 2**31 - 1  # Max allowed 32-bit signed int

if reversed_num > MAX_INT // 10 or (reversed_num == MAX_INT // 10 and digit > 7):
    return 0
```

> This prevents overflow **before it happens**.

---

### ✅ **Final Code Template**

```python
def reverse_integer(x: int) -> int:
    sign = -1 if x < 0 else 1
    x = abs(x)
    reversed_num = 0
    MAX_INT = 2**31 - 1

    while x > 0:
        digit = x % 10
        x = x // 10

        if reversed_num > MAX_INT // 10 or (reversed_num == MAX_INT // 10 and digit > 7):
            return 0

        reversed_num = reversed_num * 10 + digit

    return sign * reversed_num
```

---

### 🧮 **Time & Space Complexity**

| Metric             | Value        | Explanation |
|--------------------|--------------|-------------|
| Time Complexity    | `O(log₁₀ n)` | One loop per digit |
| Space Complexity   | `O(1)`       | Constant space used |


