package main

// Newbie at golang ;-;

import (
	"fmt"
	"log"
	"os"
	"strconv"
	"strings"
)

func main() {
	input, err := os.ReadFile("input")
	if err != nil {
		log.Fatal(err)
	}

	calorieStacks := strings.Split(string(input), "\n\n")
	highestValue := 0
	for _, stack := range calorieStacks {
		calories := strings.Split(stack, "\n")
		total := 0

		for _, calorie := range calories {
			if calorie == "" {
				continue
			}
			value, err := strconv.Atoi(strings.TrimSpace(calorie))
			if err != nil {
				log.Fatal(err)
			}
			total += value
		}

		if total > highestValue {
			highestValue = total
		}
	}

	fmt.Println(highestValue)
}
