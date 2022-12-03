package main

import (
    "os"
    "strings"
    "fmt"
 )

func main() {
    f, _ := os.ReadFile("./input")
    lines := strings.Split(string(f), "\n")
    var duplicates []int
    alphabet := []string{}
    for i := 'a'; i <= 'z'; i++ {
        alphabet = append(alphabet, string(i))
    }
    for i := 'A'; i <= 'Z'; i++ {
        alphabet = append(alphabet, string(i))
    }
    for _, line := range lines {
        left_side := strings.Split(line[0:len(line) / 2], "")
        right_side := strings.Split(line[len(line) / 2:len(line)], "")
        out:
        for _, char := range left_side {
            for _, char2 := range right_side {
                if char == char2 {
                    duplicates = append(duplicates, get_alphabet_score(char, alphabet))
                    break out
                }
            }
        }
    }

    var total int
    for _, i := range duplicates {
        total += i
    }
    fmt.Print(total)
}

func get_alphabet_score(char string, alphabet []string) int {
    for i, c := range alphabet {
        if c == char {
            return i + 1
        }
    }
    return 0
}