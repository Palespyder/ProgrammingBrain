package main

import (
	"fmt"
)

var pl = fmt.Println

func main() {

	const LENGTH int = 10

	var x float64 = 20.0

	y := 42
	pl(x)
	pl(y)
	fmt.Printf("x is of type %T\n", x)
	fmt.Printf("y is of type %T\n", y)
	fmt.Printf("LENGTH is of type %T\n", LENGTH)

}
