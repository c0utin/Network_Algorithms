package main

import (
	"fmt"
	"strings"
)

func byteStuffing(input string) {
	flagByte := "FLAG"
	escapeByte := "E"

	x := strings.ReplaceAll(input, escapeByte, escapeByte+escapeByte)
	y := strings.ReplaceAll(x, flagByte, escapeByte+flagByte)

	fmt.Printf("Frame: %s%s%s\n", flagByte, y, flagByte)
}

func main() {
	byteStuffing("EEBZ")
}
