package main

import (
	"fmt"
	"strconv"
)

func main() {
	var n int
	fmt.Scan(&n)

	for i := 0; i < n; i++ {
		var word string
		fmt.Scan(&word)
		start := 1

		for start < len(word) && word[start] == '0' {
			start++
		}

		if start >= len(word) {
			fmt.Println("-1")
			continue
		}

		s, f := word[:start], word[start:]
		sn, err1 := strconv.Atoi(s)
		fn, err2 := strconv.Atoi(f)

		if err1 != nil || err2 != nil {
			fmt.Println("Error converting to integers")
			return
		}

		if sn >= fn {
			fmt.Println("-1")
			continue
		}

		fmt.Println(s, f)
	}
}