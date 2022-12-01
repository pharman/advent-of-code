package main

import (
    "os"
    "strings"
    "strconv"
    "sort"
 )

func main() {
    var elves [][]string
    f, _ := os.ReadFile("./input")
    lines := strings.Split(string(f), "\n")
    var elf []string
    for _, line := range lines {
        if line == "" {
            elves = append(elves, elf)
            elf = nil
        }
        elf = append(elf, line)
    }
    elves = append(elves, elf)
    var top_3_elves []int
    max := 0
    for _, elf := range elves {
        current := 0
        for _, food := range elf {
            int_food, _ := strconv.Atoi(food)
            current += int_food
        }

        if len(top_3_elves) < 3 {
            top_3_elves = append(top_3_elves, current)
        } else {
            for _, top := range top_3_elves {
                if current > top {
                    top_3_elves = append(top_3_elves, current)
                    sort.Slice(top_3_elves, func(a, b int) bool {
                        return top_3_elves[a] < top_3_elves[b]
                    })

                    if len(top_3_elves) > 3 {
                        top_3_elves = top_3_elves[len(top_3_elves)-3:]
                    }
                    break
                }
            }
        }

    }
    for _, top := range top_3_elves {
        max += top
    }
    print(max)
}