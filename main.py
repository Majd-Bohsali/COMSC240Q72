from functools import reduce

def getSum(numbers, n): 
     
    sumsList = []
    for startIndex in range(0, len(numbers) - n + 1): 
        sums = reduce(lambda x, y: x + y, numbers[startIndex: startIndex + n])
        print(sum)
    
    return 0


if __name__ == "__main__":
    numbers = [1, 2, 3, 4 ,5]
    n = 3
    getSum(numbers, n)