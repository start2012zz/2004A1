transactions = [11, 1, 3, 1, 4, 19, 5, 7, 19]


def best_interval(transactions, t):
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


if __name__ == '__main__':
    print(best_interval([1, 5, 6], 5) == (1, 3))  # (0 - 5) contains 2 items but (1 - 6) contains 3 items
    print(best_interval([1, 5, 5], 5) == (0, 3))  # (0 - 5) contains 3 items
    print(best_interval([1, 5], 5) == (0, 2))  # (0 - 5) contains 2 items
    print(best_interval([1], 5) == (0, 1))  # (0 - 1) contains 1 items
    print(best_interval([1], 1) == (0, 1))  # (0 - 1) contains 1 items
    print(best_interval([1, 2, 3, 4, 5, 6, 7], 0) == (1, 1))
    print(best_interval([11, 1, 3, 1, 4, 10, 5, 7, 10], 5) == (0, 5))
    print(best_interval([11, 1, 3, 1, 4, 10, 5, 7, 10], 6) == (1, 6))
    print(best_interval([], 6) == (0, 0))
    print(best_interval([0], 2) == (0, 1))
    print(best_interval([0], 1) == (0, 1))
    print(best_interval([0], 4) == (0, 1))
    print(best_interval([0, 2, 3], 4) == (0, 3))
    print(best_interval([0, 2, 3], 0) == (0, 1))
    print(best_interval([0], 0) == (0, 1))
    print(best_interval([1], 1) == (0, 1))
    print(best_interval([0], 1) == (0, 1))
    print(best_interval([0, 0, 0, 0, 0], 1) == (0, 5))  #######
    print(best_interval(
        [11, 1, 3, 1, 4, 10, 5, 7, 10, 11, 11, 11, 12, 11, 11, 11, 13, 13, 13, 14, 14, 14, 14, 15, 15, 15, 15, 16],
        5) == (10, 21))
    print(best_interval([11, 1, 3, 1, 4, 10, 5, 7, 10], 11) == (0, 9))
    print(best_interval([1, 1, 1, 1, 1, 1, 1, 1], 0) == (1, 8))
    print(best_interval([1,2,35,1233,44444,10002,44445,44446],3))
    print(best_interval([1,2,35,1233,44444,1002,44445,44446],3)==(44443,3))
    print(best_interval([1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2], 0) == (2, 10))
# if count>len(transactions)/2: