# Python program for implementation of Radix Sort
# A function to do counting sort of arr[] according to
# the digit represented by exp.

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


def max_subarray(A):
	max_ending_here = max_so_far = A[0]

	for x in A[1:]:
		max_ending_here = max(x, max_ending_here + x)
		max_so_far = max(max_so_far, max_ending_here)
	return max_so_far
def maxSum(arr,t):
	ret=0
	totoal=0
	for i in range(t):
		totoal=max(totoal+arr[i],arr[i])
		ret=max(ret,totoal)
	return ret


def best_interval1(transactions, t):
	radixSort(transactions)
	hoels = [0] * (max(transactions) - min(transactions) + 1)
	for i in range(len(transactions)):
		hoels[transactions[i] - min(transactions)] += 1

	subArr=[]
	for i in range(len(hoels)+1-t):
		subArr.append(hoels[i:i+t])
	count=0
	bestI=0
	ax=max_subarray(subArr)
	for i in range(len(subArr)):
		if subArr[i]==ax:
			bestI=i
	for i in range(len(ax)):
		count+=ax[i]


	return bestI,count


def best_interval(transactions, t):
	radixSort(transactions)
	bestC = 0;
	count = 0
	bestStart = 0
	timeTmp = t
	for i in range(len(transactions) - 1, -1, -1):
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

	# currentC=0;
	# bestC=0;
	# bestStart=0
	# tempT=t
	# for index in range(0,len(transactions)-1):
	# 	value=transactions[index]-transactions[index+1]
	# 	print(index,value)
	# 	if tempT-value>=0:
	#
	# 		currentC+=1
	# 		print(currentC)
	# 		if currentC>bestC:
	# 			bestC=currentC
	#
	# 	else:
	# 		value=0
	# 		tempT=t
	# 		currentC=0

	return bestStart, bestC


# Driver code
arr = [170, 45, 75, 90, 802, 24, 2, 66]
arr=[10,17,30]
print(best_interval(arr, 20))  # == (0, 3)
# Function Call
radixSort(arr)

# This code is contributed by Mohit Kumra
# Edited by Patrick Gallagher
