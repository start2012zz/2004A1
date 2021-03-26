def countingSort(arr, exp1):
    n = len(arr)

    # The output array elements that will have sorted arr
    output = [0] * (n)

    # initialize count array as 0
    count = [0] * (10)

    # Store count of occurrences in count[]
    for i in range(0, n):
        index = (arr[i] / exp1)
        count[int(index % 10)] += 1

    # Change count[i] so that count[i] now contains actual
    # position of this digit in output array
    for i in range(1, 10):
        count[i] += count[i - 1]

    # Build the output array
    i = n - 1
    while i >= 0:
        index = (arr[i] / exp1)
        output[count[int(index % 10)] - 1] = arr[i]
        count[int(index % 10)] -= 1
        i -= 1

    # Copying the output array to arr[],
    # so that arr now contains sorted numbers
    i = 0
    for i in range(0, len(arr)):
        arr[i] = output[i]


# Method to do Radix Sort
def radixSort(arr):
    # Find the maximum number to know number of digits
    max1 = max(arr)

    # Do counting sort for every digit. Note that instead
    # of passing digit number, exp is passed. exp is 10^i
    # where i is current digit number
    exp = 1
    while max1 / exp > 0:
        countingSort(arr, exp)
        exp *= 10


def best_interval(transactions, t):
    bestC = 0
    count = 0
    bestStart = 0
    timeTmp = t
    if transactions == []:
        return (bestStart, count)
    bigMin = 0
    radixSort(transactions)
    for i in range(len(transactions) - 1, -1, -1):
        value = transactions[i] - transactions[i - 1]
        if value < 0:
            value = -value

        if timeTmp - value >= 0:

            timeTmp = timeTmp - value
            count += 1
            if count > bestC:
                bestC = count
                bestStart = transactions[i]
                if bestStart<bigMin:
                    bigMin=bestStart
        else:
            count = 0
            timeTmp = t

    if bestStart - t >= 0:
        bestStart = bestStart - t
    else:
        bestStart = 0
    return (bestStart, bestC)

if __name__ == '__main__':
   print(best_interval([1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2], 0))
   print(best_interval([0], 2))
   print(best_interval([0], 1) == (0, 1))
   print(best_interval([0], 4) == (0, 1))
   print(best_interval([0, 2, 3], 4))
   print(best_interval([0, 2, 3], 4) == (0, 3))
   print(best_interval([0, 2, 3], 0) )
   print(best_interval([0, 2, 3], 0) == (0, 1))
   print(best_interval([0], 0) == (0, 1))
   print(best_interval([1], 1))
   print(best_interval([1], 1) == (0, 1))
