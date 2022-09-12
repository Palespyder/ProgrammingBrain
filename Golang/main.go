package main

import (
	"fmt"
)

var pl = fmt.Println

func main() {

	var x float64
	x = 20.0
	pl(x)
	fmt.Printf("x is of type %T\n", x)

}
