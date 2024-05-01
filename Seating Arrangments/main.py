# NOT TESTED YET

from math import floor

inp = int(input())
pri = ""

def seating_arrangements(arr: list[int]) -> str:
    i = len(arr)
    res = ""
    i2 = 0

    while abs(i-i2) > 1:
        arr.insert(i, arr[i2])
        del arr[i2]

        i -= 2
        i2 += 1

    for el in arr:
        res += f"{el} "

    return res;

for _ in range(inp):
    input()
    arr = list(map(lambda a: int(a), input().split(" ")))
    pri += seating_arrangements(arr) + "\n"

print(pri)
