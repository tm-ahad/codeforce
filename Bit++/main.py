n = int(input())
r = 0

for _ in range(n):
   inst = input()
   r += inst.count('++') - inst.count('--')

print(r)