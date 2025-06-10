def linear_search():
    def linear(array, target):
        for i in range(len(array)):
            if array[i] == target:
                return i
        return -1 

array = [3, 5, 2, 8, 1]
print(linear_search(array, 8))