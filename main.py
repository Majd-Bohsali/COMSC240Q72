from functools import reduce

def getSum(numbers, n): 
     
    sumsList = []
    for startIndex in range(0, len(numbers) - n + 1): 
        sumsList.append(reduce(lambda x, y: x + y, numbers[startIndex: startIndex + n]))
    
    return max(sumsList)


if __name__ == "__main__":
    numbers = [1, 2, 3, 4, 5]
    n = 3
    print("Numbers: ", numbers, "n: ", n, "Maximum sum: ", getSum(numbers, n))
    
    numbers = [9, 10, 11, 10, 2]
    n = 3
    print("Numbers: ", numbers, "n: ", n, "Maximum sum: ", getSum(numbers, n))
    
    numbers = [5, 4, 3, 2, 1]
    n = 3
    print("Numbers: ", numbers, "n: ", n, "Maximum sum: ", getSum(numbers, n))
    
    numbers = [9, 10, 11, 10, 2]
    n = 1
    print("Numbers: ", numbers, "n: ", n, "Maximum sum: ", getSum(numbers, n))