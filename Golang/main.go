package main

import (
	"fmt"
)

var pl = fmt.Println

func main() {
	pl("5 + 4 =", 5+4)
	pl("5 - 4 =", 5-4)
	pl("5 / 4 =", 5/4)
	pl("5 * 4 =", 5*4)
	pl("5 % 4 =", 5%4)
	mInt := 1
	mInt++
	pl(mInt)
	mInt++
	pl(mInt)
	newInt := mInt + 23/4*2 - 4 + 6 + 9 - 5
	pl(newInt)

	newFloat := 3.14
	newFloat2 := 6.14
	pl(newFloat * newFloat2)

}
