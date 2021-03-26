def counting_sort(a):
   maximum = int(max(a))
   minimum = int(min(a))
   range1 = maximum - minimum + 1
   counting = [0] * range1
   out_a = [0] * len(a)

   for i in range(0, len(a)):
       counting[a[i]-minimum] += 1

   for i in range(1, len(counting)):
       counting[i] += counting[i-1]

   for i in range(len(a)-1, -1, -1):
       out_a[counting[a[i] - minimum] - 1] = a[i]
       counting[a[i] - minimum] -= 1

   for i in range(0, len(a)):
       a[i] = out_a[i]

   return a

# Counting sort in Python programming


def countingSort(array):
    size = len(array)
    output = [0] * size

    # Initialize count array
    count = [0] * 10

    # Store the count of each elements in count array
    for i in range(0, size):
        count[array[i]] += 1

    # Store the cummulative count
    for i in range(1, 10):
        count[i] += count[i - 1]
    print(count)
    # Find the index of each element of the original array in count array
    # place the elements in output array
    i = size - 1
    while i >= 0:
        output[count[array[i]] - 1] = array[i]
        count[array[i]] -= 1
        i -= 1

    # Copy the sorted elements into original array
    for i in range(0, size):
        array[i] = output[i]

def count_sort(lst):
    count = [0] * 10
    postion = [0] * 10

    # count times of each element appear in arr
    for index in range(len(lst)):
        count[lst[index]] += 1

    # cumulate each element count to calculate next item position and store
    for index in range(1, 10):
        postion[index] += count[index - 1] + postion[index - 1]

    result = [0] * len(lst)

    for index in range(0, len(lst)):
        result[postion[lst[index]]] = lst[index]
        postion[lst[index]] += 1
    return result

data = [4, 2, 2, 48, 3, 1,0]

print(count_sort(data))
countingSort(data)
print("Sorted Array in Ascending Order: ")
print(data)

a = [-5, -10, 0, -3, 8, 5, -1, 10]


print(counting_sort(a))