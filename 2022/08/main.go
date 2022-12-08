package main

import (
    "os"
    "fmt"
    "strings"
    "strconv"
)

func main() {
//     p1()
    p2()
}

func p2() {
    f, _ := os.ReadFile("./input")
    lines := strings.Split(string(f), "\n")
    tree_map := parse(lines)
    max_trees := 0
    for i := 0; i < len(tree_map); i++ {
        for x := 0; x < len(tree_map[i]); x++ {
            num_trees := calc_trees(x, i, tree_map)
            if (num_trees > max_trees) {
                max_trees = num_trees
            }
        }
    }
    fmt.Print(max_trees, "\n")
}

func p1() {
    f, _ := os.ReadFile("./input")
    lines := strings.Split(string(f), "\n")
    tree_map := parse(lines)

    num_visible := (len(tree_map) + len(tree_map[0]) -2) * 2
    exterior := (len(tree_map) + len(tree_map[0]) -2) * 2
    for i := 1; i < len(tree_map) -1; i++ {
        for x := 1; x < len(tree_map[i]) -1; x++ {
            if is_visible(x, i, tree_map) {
                num_visible += 1
            }
        }
    }
    fmt.Print(num_visible, exterior, num_visible - exterior, "\n")
}

func parse(lines []string) [][]int {
    tree_map := [][]int{}
    for _, line := range lines {
        row := strings.Split(line, "")
        row_int := []int{}
        for _, char := range row {
            int_val, _ := strconv.Atoi(char)
            row_int = append(row_int, int_val)
        }
        tree_map = append(tree_map, row_int)
    }
    return tree_map
}

func is_visible(x int, i int, tree_map [][]int) bool {
    visible_left, visible_right, visible_up, visible_down := true, true, true, true

    if (tree_map[i][x] == 0) {
        return false
    }

    for y := x -1; y >= 0; y-- {
        if tree_map[i][x] <= tree_map[i][y] {
            visible_left = false
        }
    }
    for y := x +1; y < len(tree_map[i]); y++ {
        if tree_map[i][x] <= tree_map[i][y] {
            visible_right = false
        }
    }
    for y := i -1; y >= 0; y-- {
        if tree_map[i][x] <= tree_map[y][x] {
            visible_up = false
        }
    }
    for y := i +1; y < len(tree_map); y++ {
        if tree_map[i][x] <= tree_map[y][x] {
            visible_down = false
        }
    }
    return visible_left || visible_right || visible_up || visible_down
}

func calc_trees(x int, i int, tree_map [][]int) int {
    trees_left, trees_right, trees_up, trees_down := 0, 0, 0, 0
    for y := x -1; y >= 0; y-- {
        trees_left +=1
        if tree_map[i][x] <= tree_map[i][y] {
            break
        }
    }
    for y := x +1; y < len(tree_map[i]); y++ {
        trees_right += 1
        if tree_map[i][x] <= tree_map[i][y] {
            break
        }
    }
    for y := i -1; y >= 0; y-- {
        trees_up += 1
        if tree_map[i][x] <= tree_map[y][x] {
            break
        }
    }
    for y := i +1; y < len(tree_map); y++ {
        trees_down += 1
        if tree_map[i][x] <= tree_map[y][x] {
            break
        }
    }

    return trees_left * trees_right * trees_up * trees_down
}