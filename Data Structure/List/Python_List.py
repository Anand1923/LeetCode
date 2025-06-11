class MyArray:
    def __init__(self):
        self.data = {}

    def get(self, index):
        return self.data.get(index)

    def push(self, item):
        self.data[len(self.data)] = item

    def pop(self):
        last_key = len(self.data) - 1
        del self.data[last_key]

    def delete(self, index):
        #delete the key
        del self.data[index]
        # Reindex the array
        temp = {}
        i = 0
        for key in sorted(self.data.keys()):
            temp[i] = self.data[key]
            i += 1
        self.data = temp

# Usage
arr = MyArray()
arr.push(10)
arr.push(20)
arr.push(30)
arr.delete(1)
print(arr.data)  # Output: {0: 10, 1: 30}









i=0 , j=1



i=1 , j=1


