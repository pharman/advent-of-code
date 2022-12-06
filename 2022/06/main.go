package main

import (
    "os"
    "fmt"
    "strings"
    "bufio"
 )

func main() {
    p1()
    p2()
}

func p1() {
    calc(4)
}

func p2() {
    calc(14)
}

func calc(l int) {
    f, _ := os.ReadFile("./input")
    s := bufio.NewScanner(strings.NewReader(string(f)))
    s.Split(bufio.ScanRunes)
    var prev string
    var i int = 0
    for s.Scan() {
        prev += s.Text()
        if len(prev) == l {
            if unique(prev) {
                fmt.Print(i +1, "\n")
                return
            }
            prev = prev[1:l]
        }
        i++
    }
}

func unique(str string) bool {
    for _, char := range str {
        if strings.Count(str, string(char)) > 1 {
            return false
        }
    }
    return true
}