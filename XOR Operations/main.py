n = input()
nums = input().split(" ")
max = 0
st = set(nums)
lenSt = len(st)

def factorial_iterative(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

for n in nums:
   c = nums.count(n)

   if c > max:
      max = c

if lenSt == len(nums):
   print(factorial_iterative(lenSt))
elif lenSt == 0:
   print(1)
else:
   if c >= 1:
      print(lenSt*lenSt)
   else:
      print(factorial_iterative(lenSt))