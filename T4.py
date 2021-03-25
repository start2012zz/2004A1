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
a = [-5, -10, 0, -3, 8, 5, -1, 10]


print(counting_sort(a))