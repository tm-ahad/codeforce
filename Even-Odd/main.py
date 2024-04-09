def remove_element(arr, element):
    found = False
    i = 0
    while i < len(arr):
        if arr[i] == element:
            found = True
            del arr[i]
        else:
            i += 1
    if not found:
        print("Element not found in the array.")

def main():
    test = int(input())
    pri = ""

    for t in range(test):
        _ = int(input())
        arr = list(map(int, input().split()))

        alice_turn = True
        scores = [0, 0]

        while len(arr) != 0:
            big_odd = max((x for x in arr if x % 2 != 0), default=-1)
            big_even = max((x for x in arr if x % 2 == 0), default=-1)

            big = max(big_odd, big_even)
            print(big_odd, big_even, big)
            is_even = big == big_even

            if alice_turn == is_even:
                scores[int(alice_turn)] += big
        
            remove_element(arr, big)
        
        if scores[1] > scores[0]:
            pri += "Alice\n"
        elif scores[1] < scores[0]:
            pri += "Bob\n"
        else:
            pri += "Tie\n"

    print(pri, end='')

if __name__ == "__main__":
    main()
