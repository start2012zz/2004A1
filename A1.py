transactions = [11, 1, 3, 1, 4, 19, 5, 7, 19]


def best_interval1(transactions, t):
    if transactions == []:
        return (0, 0)
    greatest = 0
    best_int = 0
    for number in range(max(transactions) + 1):
        boundary = number + t
        count = 0
        for index in range(len(transactions)):
            if boundary >= transactions[index] >= number:
                count += 1
        if count > greatest:
            greatest = count
            best_int = number
    return (best_int, greatest)


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
    while max1 / exp > 1:
        countingSort(arr, exp)
        exp *= 10


def best_interval(transactions, t):
    bestC = 0
    count = 0
    bestStart = 0
    timeTmp = t
    if transactions == []:
        return (bestStart, count)
    radixSort(transactions)

    for i in range(len(transactions) -1, -1, -1):
        value = transactions[i] - transactions[i - 1]
        if timeTmp - value >= 0:
            count += 1
            if count > bestC:
                bestC = count
                bestStart = transactions[i]
        else:
            count = 0
            timeTmp = t
            value = 0

    return (bestStart, bestC)


if __name__ == '__main__':

    # print(best_interval([1, 5, 5], 5))
    # print(best_interval([1, 5, 5], 5) == (0, 3))  # (0 - 5) contains 3 items
    # print(best_interval([1, 5], 5) == (0, 2))  # (0 - 5) contains 2 items
    # print(best_interval([1], 5) == (0, 1))  # (0 - 1) contains 1 items
    # print(best_interval([1], 1) == (0, 1))  # (0 - 1) contains 1 items
    # print(best_interval([1, 2, 3, 4, 5, 6, 7], 0) == (1, 1))
    # print(best_interval([11, 1, 3, 1, 4, 10, 5, 7, 10], 5) == (0, 5))
    # print(best_interval([11, 1, 3, 1, 4, 10, 5, 7, 10], 6) == (1, 6))
    # print(best_interval([], 6) == (0, 0))
    # print(best_interval([0], 2) == (0, 1))
    # print(best_interval([0], 1) == (0, 1))
    # print(best_interval([0], 4) == (0, 1))
    # print(best_interval([0, 2, 3], 4) == (0, 3))
    # print(best_interval([0, 2, 3], 0) == (0, 1))
    # print(best_interval([0], 0) == (0, 1))
    # print(best_interval([1], 1) == (0, 1))
    # print(best_interval(
    #     [11, 1, 3, 1, 4, 10, 5, 7, 10, 11, 11, 11, 12, 11, 11, 11, 13, 13, 13, 14, 14, 14, 14, 15, 15, 15, 15, 16],
    #     5) == (10, 21))
    # print(best_interval([11, 1, 3, 1, 4, 10, 5, 7, 10], 11) == (0, 9))
    # print(best_interval([1, 2, 35, 1233, 44444, 10002, 44445, 44446], 3))
    # print(best_interval([1, 2, 35, 1233, 44444, 1002, 44445, 44446], 3) == (44443, 3))
    print(best_interval([1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2], 0))
    print(best_interval([1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2], 0) == (2, 10))

