package main

import (
	"fmt"
	"log"
	"os"
	"sort"
	"strconv"
	"strings"
)

func main() {
	input, err := os.ReadFile("input")
	if err != nil {
		log.Fatal(err)
	}

	calorieStacks := strings.Split(string(input), "\n\n")
	values := make([]int, len(calorieStacks))
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

		values = append(values, total)
	}

	sort.Sort(sort.Reverse(sort.IntSlice(values)))

	fmt.Println(values[0] + values[1] + values[2])
}
