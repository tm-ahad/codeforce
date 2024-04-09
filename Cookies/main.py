n = int(input())
cookies = input()
spl = cookies.split(' ')
res = 0
sum = 0

for n in spl:
   sum += int(n)

for n in spl:
   if (sum - int(n)) % 2 == 0:
      res += 1

print(res)
