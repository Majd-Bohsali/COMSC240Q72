def getSum(numbers, n): 
     
    sumsList = []
    for startIndex in range(0, len(numbers) - n + 1): 
        print("startIndex: ", startIndex)
    
    return 0


if __name__ == "__main__":
    numbers = [1, 2, 3, 4 ,5]
    n = 3
    getSum(numbers, n)