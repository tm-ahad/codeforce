n = int(input())

for _ in range(n):
   word = input()
   wordlen = len(word)

   if wordlen > 10:
      print (f"{word[0]}{wordlen-2}{word[wordlen-1]}")
   else:
      print(word)