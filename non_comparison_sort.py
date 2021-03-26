# -*- coding:UTF-8 -*-
# 开发人员:start
# 开发时间:
# 文件名称:non_comparison_sort.PY
# 开发工具:PyCharm

def count_sort(lst,base):
    count = [0] * 10
    postion = [0] * 10

    # count times of each element appear in arr

    for index in range(len(lst)):
        temIndex=lst[index]/base
        temIndex=int(temIndex)
        count[temIndex%10] += 1

    # cumulate each element count to calculate next item position and store
    for index in range(1, 10):
        postion[index] += count[index - 1] + postion[index - 1]

    result = [0] * len(lst)

    for index in range(0, len(lst)):

        result[postion[int(lst[index]%10)]] = lst[index]
        postion[int(lst[index]%10)] += 1


    for i in range(len(lst)):
        lst[i]=result[i]



def radixSort(lst):
    max_element = max(lst)

    # Apply counting sort to sort elements based on place value.
    divide = 1

    count_sort(lst, divide)
    count_sort(lst, 10)
    return lst

data = [14, 22, 12, 4]

print(radixSort(data))
print(data)