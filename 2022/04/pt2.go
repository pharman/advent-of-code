package main

import (
    "os"
    "strings"
    "fmt"
    "strconv"
 )

func main() {
    f, _ := os.ReadFile("./input")
    lines := strings.Split(string(f), "\n")
    partial_overlaps := 0
    for _, line := range lines {
        line := strings.Split(line, ",")
        group := [][]string{strings.Split(line[0], "-"), strings.Split(line[1], "-")}

        if overlaps(group[0], group[1]) {
            partial_overlaps++
            continue
        }
        if overlaps(group[1], group[0]) {
            partial_overlaps++
        }
    }
    fmt.Print(partial_overlaps)
}

//   23
//  1234
/// 1234
///  23
func overlaps(a []string, b []string) bool {
    x1, _ := strconv.Atoi(a[0])
    x2, _ := strconv.Atoi(a[1])
    x3, _ := strconv.Atoi(b[0])
    x4, _ := strconv.Atoi(b[1])

    return (x1 <= x3 && x2 >= x4) || (x1 <= x3 && x2 >= x3) || (x1 >= x3 && x2 <= x3)
}