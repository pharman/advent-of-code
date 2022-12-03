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

    for i := 0; i < len(lines); i++ {
        lines[i] = remove_dupes(lines[i])
    }
    for i := 0; i < len(lines); i++ {
        chars := lines[i] + lines[i+1] + lines[i+2]

        i += 2
        for _, c := range strings.Split(chars, "") {
            if strings.Count(chars, c) > 2 {
                duplicates = append(duplicates, get_alphabet_score(c, alphabet))
                break
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

func remove_dupes(line string) string {
    chars := strings.Split(line, "")
    char_map := make(map[string]string)
    for _, i := range chars {
        if _, ok := char_map[i]; !ok {
            char_map[i] = i
        }
    }
    keys := []string{}
    for k := range char_map {
        keys = append(keys, k)
    }
    return strings.Join(keys, "")
}