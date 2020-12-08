package main

import (
	"bufio"
	"fmt"
	"log"
	"os"
	"path/filepath"
	"strconv"
)

var filename, _ = filepath.Abs("1/input.txt")

func main() {
	data := readLines(filename)
	fmt.Println(firstAnswer(data))
	fmt.Println(secondAnswer(data))

}

func firstAnswer(inputData []string) int {
	for _, x := range inputData {
		var first, _ = strconv.Atoi(x)
		for _, y := range inputData {
			var second, _ = strconv.Atoi(y)
			if first + second == 2020 {
				var result = first * second
				return result
			}
		}
	}
	return 0
}

func secondAnswer(inputData []string) int {
	for _, x := range inputData {
		var first, _ = strconv.Atoi(x)
		for _, y := range inputData {
			var second, _ = strconv.Atoi(y)
			for _, z := range inputData {
				var third, _ = strconv.Atoi(z)
				if first + second + third == 2020 {
					var result = first * second * third
					return result
				}
			}
		}
	}
	return 0
}

func readLines(inputFilename string) []string {
	file, err := os.Open(inputFilename)

	if err != nil {
		log.Printf("Failed to open file")
		log.Fatal(err)
	}
	scanner := bufio.NewScanner(file)
	scanner.Split(bufio.ScanLines)
	var text []string

	for scanner.Scan() {
		text = append(text, scanner.Text())
	}
	file.Close()
	return text
}