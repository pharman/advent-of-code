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
        their_choice := get_shape_score(game[0])
        score += get_points(their_choice, choice)
    }
    fmt.Print(score)
}

func get_shape_score(a string) int {
    scores := map[string]int{
        "A": 1,
        "B": 2,
        "C": 3,
        "X": 1,
        "Y": 2,
        "Z": 3,
    }
    return scores[a]
}

func get_points(a int, b int) int {
    // 1 lose, 2 draw, 3 win
    loses := make([][]int, 0)
    loses = append(loses, []int{1, 3})
    loses = append(loses, []int{2, 1})
    loses = append(loses, []int{3, 2})

    wins := make([][]int, 0)
    wins = append(wins, []int{1, 2})
    wins = append(wins, []int{2, 3})
    wins = append(wins, []int{3, 1})

    if (b == 1) {
       return find_shape(a, loses)
    }
    if (b == 2) {
       return a + 3
    }
    if (b == 3) {
       played_shape := find_shape(a, wins)
       return played_shape + 6
    }
    return 0
}

func find_shape(shape int, scores [][]int) int {
    for _, i := range scores {
        if shape == i[0] {
            return i[1]
        }
    }
    return 0
}