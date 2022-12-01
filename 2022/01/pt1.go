package main

import (
    "os"
    "strings"
    "strconv"
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
    max := 0
    for _, elf := range elves {
        current := 0
        for _, food := range elf {
            int_food, _ := strconv.Atoi(food)
            current += int_food
            if current > max {
                max = current
            }
        }
    }
    print(max)
}