package main

import (
	"fmt"
	"strings"
)

var pl = fmt.Println

func main() {
	sV1 := "A Word"
	replacer := strings.NewReplacer("A", "Another")
	sV2 := replacer.Replace(sV1)
	pl(sV2)
	pl("Length: ", len(sV2))
	pl("Contains Another: ", strings.Index(sV2, "Another"))
	pl("o index: ", strings.Index(sV2, "o"))

}
