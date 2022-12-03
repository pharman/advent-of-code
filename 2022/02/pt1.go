package main

import (
    "os"
    "strings"
    "fmt"
 )

func main() {
    f, _ := os.ReadFile("./input")
    lines := strings.Split(string(f), "\n")
    score := 0
    for _, line := range lines {
        game := strings.Split(line, " ")
        choice := get_shape_score(game[1])
        score += did_win(game[0], choice)
    }
    fmt.Print(score)
}

func get_shape_score(a string) int {
    scores := map[string]int{
        "X": 1,
        "Y": 2,
        "Z": 3,
    }
    return scores[a]
}
func did_win(a string, b int) int {
    letters := map[int]string{
        1: "A",
        2: "B",
        3: "C",
    }

    if a == letters[b] {
        return b + 3
    }
    if a == "A" && b == 2 {
        return b + 6
    }
    if a == "B" && b == 1  {
        return b
    }
    if a == "A" && b == 3 {
        return b
    }
    if a == "C" && b == 1 {
        return b + 6
    }
    if a == "B" && b == 1 {
        return b
    }
    if a == "B" && b == 3 {
        return b + 6
    }
    if a == "C" && b == 1 {
        return b + 6
    }
    if a == "C" && b == 2 {
        return b
    }
    return 0
}