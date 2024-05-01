inp = int(input(""))
pr = ""

def maxBeauty(arr: list[int]):
    arr = sorted(arr)
    res = 0

    for i in range(1, len(arr)):
        num = arr[i] - arr[i-1]
        if num > 0 : res += num
 
    return res

for i in range(inp):
    _ = input()
    arr = list(map(lambda a: int(a), input().split(' ')))

    pr += str(maxBeauty(arr)) + '\n'

print(pr)
