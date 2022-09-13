package main

import (
	"fmt"
)

var pl = fmt.Println

func main() {

	var x float64 = 20.0

	y := 42
	pl(x)
	pl(y)
	fmt.Printf("x is of type %T\n", x)
	fmt.Printf("y is of type %T\n", y)

}
