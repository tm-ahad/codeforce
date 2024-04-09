n = int(input())
res = 0

def convBool(s):
   if s == '1':
      return True;
   return False;

for _ in range(n):
   spl = input().split(" ")
   a, b, c = int(spl[0]), int(spl[1]), int(spl[2])

   res += (a + b + c >= 2)
print(res)