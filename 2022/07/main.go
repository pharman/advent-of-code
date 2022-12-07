package main

import (
    "os"
    "fmt"
    "strings"
    "regexp"
    "strconv"
    "sort"
 )

func main() {
    p1_2()
//     p2()
}

var all_dirs []int

const MAX_DIR_SIZE = 100000
const REQUIRED_FREE_SPACE = 30000000

func p1_2() {
    f, _ := os.ReadFile("./input")
    lines := strings.Split(string(f), "\n")
    bytes, dirs, _ := recurse(lines, 0, 0)
    fmt.Print(bytes, dirs, "\n\n")
    sort.Slice(all_dirs, func(i, j int) bool {
        return all_dirs[i] < all_dirs[j]
    })
    free := 70000000 - bytes
    for _, dir := range all_dirs {
        if free + dir > REQUIRED_FREE_SPACE {
            fmt.Print(dir, "\n")
            os.Exit(0)
        }
    }
}

func recurse(lines []string, dirs int, acc int) (int, int, int) {
    bytes := 0
    for index, line := range lines {
        if index < acc {
            continue
        }
        acc += 1
        if line == "$ cd .." {
            break
        } else if len(line) >= 4 && line[0:4] == "$ cd" {
            subdir_bytes, subdir_dirs, lines_read :=  recurse(lines, 0, acc)
            acc = lines_read
            bytes += subdir_bytes
            dirs += subdir_dirs
        } else if line[0] >= '0' && line[0] <= '9' {
            re := regexp.MustCompile("[0-9]+")
            matches := re.FindAll([]byte(line), -1)
            num_bytes, _ := strconv.Atoi(string(matches[0]))
            bytes += num_bytes
        }
    }
    all_dirs = append(all_dirs, bytes)
    if bytes < MAX_DIR_SIZE {
        fmt.Print(bytes, "\n")
        return bytes, dirs + 1, acc
    }
    return bytes, dirs, acc
}
