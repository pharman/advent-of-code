package main

import (
    "os"
    "fmt"
    "strings"
    "strconv"
    "regexp"
 )

func main() {
    p1()
    p2()
}

func p1() {
    stack := make_stack()
    f, _ := os.ReadFile("./input")
    lines := strings.Split(string(f), "\n")
    stack = reorder(stack, lines, false)
    for i := 1; i < len(stack)+1; i++ {
        fmt.Print(stack[i][len(stack[i])-1])
    }
    print("\n")
}

func p2() {
    stack := make_stack()
    f, _ := os.ReadFile("./input")
    lines := strings.Split(string(f), "\n")
    stack = reorder(stack, lines, true)
    for i := 1; i < len(stack)+1; i++ {
        fmt.Print(stack[i][len(stack[i])-1])
    }
    print("\n")
}

func reorder(stack map[int][]string, lines []string, preserve_order bool) map[int][]string {
    for _, line := range lines {
        re := regexp.MustCompile("[0-9]+")
        matches := re.FindAll([]byte(line), -1)
        move, _ := strconv.Atoi(fmt.Sprintf("%s", matches[0]))
        col_a, _ := strconv.Atoi(fmt.Sprintf("%s", matches[1]))
        col_b, _ := strconv.Atoi(fmt.Sprintf("%s", matches[2]))
        additions := []string{}
        for i := 0; i < move; i++ {
            if len(stack[col_a]) > 0 {
                var x string
                x, stack[col_a] = stack[col_a][len(stack[col_a])-1], stack[col_a][:len(stack[col_a])-1]
                additions = append(additions, x)
            }
        }
        if preserve_order {
            reverse_additions := []string{}
            for i := range additions {
                reverse_additions = append(reverse_additions, additions[len(additions)-1-i])
            }
            additions = reverse_additions
        }
        stack[col_b] = append(stack[col_b], additions...)
    }
    return stack
}

func make_stack() map[int][]string {
    f, _ := os.ReadFile("./crates")
    lines := strings.Split(string(f), "\n")
    stack := make(map[int][]string)
    for key, line := range lines {
        for i := 0; i < len(line); i+=3 {
            crate := line[i+1:i+2]
            if stack[len(lines)-key] == nil {
                stack[len(lines)-key] = make([]string, 1)
            }
            stack[len(lines)-key] = append(stack[len(lines)-key], crate)
            i += 1
        }
    }
    new_stack := make(map[int][]string, len(stack))
    for i := 1; i < len(stack)+2; i++ {
        col := []string{}
        for x := 1; x < 10; x++ {
            if len(stack[x]) > i && stack[x][i] != " " {
                col = append(col, stack[x][i])
            }
        }
        new_stack[i] = col
    }

    return new_stack
}