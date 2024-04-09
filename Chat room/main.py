inp = input()
red = "hello"
ind = 0

for c in inp:
   if c == red[ind]:
      ind += 1

      if ind == len(red):
         print('YES')
         exit(0)

print('NO')