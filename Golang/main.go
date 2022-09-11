package main

import (
	"fmt"
	"unicode/utf8"
)

var pl = fmt.Println

func main() {
	rStr := "abcdefg"
	pl("Rune Count", utf8.RuneCountInString(rStr))

}
